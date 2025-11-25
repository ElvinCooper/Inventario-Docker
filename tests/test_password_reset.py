import pytest
from flask_jwt_extended import create_access_token
from datetime import timedelta
from unittest.mock import patch


class TestPasswordReset:
    """Tests para endpoints de reset de contraseña"""

    @pytest.mark.integration
    def test_request_reset_success(self, client, test_user, auth_headers):
        """Test solicitar reset con email válido"""

        with patch('services.email_service.send_password_reset_email') as mock_email:
            response = client.post(
                '/api/v1/password/reset',
                json={'email': test_user.email},
                headers=auth_headers
            )

            assert response.status_code == 200
            data = response.get_json()
            assert data['success'] is True
            assert 'instrucciones' in data['message'].lower()

            # Verificar que se intentó enviar email
            mock_email.assert_called_once()

    @pytest.mark.integration
    def test_request_reset_invalid_email(self, client, auth_headers):
        """Test solicitar reset con email inexistente"""

        response = client.post(
            '/api/v1/password/reset',
            json={'email': 'noexiste@example.com'},
            headers=auth_headers
        )

        # Debe retornar éxito por seguridad (no revelar emails)
        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True

    @pytest.mark.integration
    def test_request_reset_missing_email(self, client, auth_headers):
        """Test solicitar reset sin email"""

        response = client.post(
            '/api/v1/password/reset',
            json={},
            headers=auth_headers
        )

        assert response.status_code == 422  # Validation error

    @pytest.mark.integration
    def test_request_reset_rate_limit(self, client, test_user, auth_headers):
        """Test rate limiting (3 por hora)"""

        with patch('services.email_service.send_password_reset_email'):
            # Hacer 4 requests (el límite es 3)
            for i in range(4):
                response = client.post(
                    '/api/v1/password/reset',
                    json={'email': test_user.email},
                    headers=auth_headers
                )

                if i < 3:
                    assert response.status_code == 200
                else:
                    assert response.status_code == 429  # Too many requests

    @pytest.mark.integration
    def test_confirm_reset_success(self, client, app, test_user, auth_headers):
        """Test confirmar reset con token válido"""

        with app.app_context():
            # Generar token válido
            token = create_access_token(
                identity=test_user.id_usuario,
                expires_delta=timedelta(hours=1),
                additional_claims={'type': 'password_reset'}
            )

        response = client.put(
            '/api/v1/password/reset',
            json={
                'token': token,
                'new_password': 'newpassword123'
            },
            headers=auth_headers
        )

        assert response.status_code == 200
        data = response.get_json()
        assert data['success'] is True
        assert 'actualizada' in data['message'].lower()

    @pytest.mark.integration
    def test_confirm_reset_expired_token(self, client, app, test_user, auth_headers):
        """Test confirmar reset con token expirado"""

        with app.app_context():
            # Token expirado (0 segundos)
            token = create_access_token(
                identity=test_user.id_usuario,
                expires_delta=timedelta(seconds=-1),
                additional_claims={'type': 'password_reset'}
            )

        response = client.put(
            '/api/v1/password/reset',
            json={
                'token': token,
                'new_password': 'newpassword123'
            },
            headers=auth_headers
        )

        assert response.status_code == 400
        data = response.get_json()
        assert 'expirado' in data['message'].lower()

    @pytest.mark.integration
    def test_confirm_reset_invalid_token(self, client, auth_headers):
        """Test confirmar reset con token inválido"""

        response = client.put(
            '/api/v1/password/reset',
            json={
                'token': 'token_invalido_12345',
                'new_password': 'newpassword123'
            },
            headers=auth_headers
        )

        assert response.status_code == 400

    @pytest.mark.integration
    def test_confirm_reset_wrong_token_type(self, client, app, test_user, auth_headers):
        """Test confirmar reset con token de tipo incorrecto"""

        with app.app_context():
            # Token normal (no de password_reset)
            token = create_access_token(
                identity=test_user.id_usuario,
                expires_delta=timedelta(hours=1)
            )

        response = client.put(
            '/api/v1/password/reset',
            json={
                'token': token,
                'new_password': 'newpassword123'
            },
            headers=auth_headers
        )

        assert response.status_code == 400
        data = response.get_json()
        assert 'inválido' in data['message'].lower()

    @pytest.mark.integration
    def test_confirm_reset_short_password(self, client, app, test_user, auth_headers):
        """Test confirmar reset con contraseña muy corta"""

        with app.app_context():
            token = create_access_token(
                identity=test_user.id_usuario,
                expires_delta=timedelta(hours=1),
                additional_claims={'type': 'password_reset'}
            )

        response = client.put(
            '/api/v1/password/reset',
            json={
                'token': token,
                'new_password': '123'  # Muy corta
            },
            headers=auth_headers
        )

        assert response.status_code == 422  # Validation error