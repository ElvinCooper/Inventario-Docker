"""Tests para endpoints de movimientos"""
import pytest
from decimal import Decimal
from app.app.models import Movimientos, Producto, Categoria

pytestmark = pytest.mark.integration


# @pytest.fixture
# def sample_movimiento(db, sample_product):
#     """Crea un movimiento de prueba"""
#     movimiento = Movimientos(
#         id_producto=sample_product.id_producto,
#         tipo_movimiento='entrada',
#         cantidad=50,
#         motivo='Compra inicial'
#     )
#     db.session.add(movimiento)
#     db.session.commit()
#     return movimiento      # debo crear un endpoint para creacion de movimientos.


class TestMovimientosEndpoints:
    """Tests para endpoints de movimientos"""

    def test_get_all_movimientos_empty(self, client, auth_headers):
        """Test: Listar movimientos vacío"""
        response = client.get('/api/v1/movimientos', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert data['total'] == 0

    def test_get_all_movimientos_with_data(self, client, sample_movimiento, auth_headers):
        """Test: Listar movimientos con datos"""
        response = client.get('/api/v1/movimientos', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()
        assert data['total'] > 0
        assert data['movimientos'][0]['tipo_movimiento'] == 'Salida'

    def test_get_movimiento_by_id(self, client, sample_movimiento, auth_headers):
        """Test: Obtener movimiento por ID"""
        response = client.get(f'/api/v1/movimiento/{sample_movimiento.id_movimiento}', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()
        assert data['tipo_movimiento'] == 'Salida'
        assert int(data['cantidad']) == 50

    # def test_create_movimiento_entrada(self, client, sample_product, auth_headers):
    #     """Test: Crear movimiento de entrada"""
    #     stock_inicial = sample_product.stock_actual
    #
    #     new_movimiento = {
    #         'id_producto': sample_product.id_producto,
    #         'tipo_movimiento': 'entrada',
    #         'cantidad': 20,
    #         'motivo': 'Reabastecimiento'
    #     }
    #
    #     response = client.post(
    #         '/api/v1/movimientos',
    #         json=new_movimiento,
    #         headers=auth_headers
    #     )
    #
    #     assert response.status_code == 201 # debo crear ese endpoint.

        # Verificar que aumentó el stock
        # product_response = client.get(f'/api/v1/productos/{sample_product.id_producto}')
        # product_data = product_response.get_json()
        # assert product_data['stock_actual'] == stock_inicial + 20

    # def test_create_movimiento_salida(self, client, sample_product, auth_headers):
    #     """Test: Crear movimiento de salida"""
    #     stock_inicial = sample_product.stock_actual
    #
    #     new_movimiento = {
    #         'id_producto': sample_product.id_producto,
    #         'tipo_movimiento': 'salida',
    #         'cantidad': 5,
    #         'motivo': 'Venta'
    #     }
    #
    #     response = client.post(
    #         '/api/v1/movimientos',
    #         json=new_movimiento,
    #         headers=auth_headers
    #     )
    #
    #     assert response.status_code == 201
    #
    #     # Verificar que disminuyó el stock
    #     product_response = client.get(f'/api/v1/productos/{sample_product.id_producto}')
    #     product_data = product_response.get_json()
    #     assert product_data['stock_actual'] == stock_inicial - 5

    # def test_create_movimiento_invalid_producto(self, client, auth_headers):
    #     """Test: Crear movimiento con producto inválido"""
    #     new_movimiento = {
    #         'id_producto': '99999999-9999-9999-9999-999999999999',
    #         'tipo_movimiento': 'entrada',
    #         'cantidad': 10,
    #         'motivo': 'Test'
    #     }
    #
    #     response = client.post(
    #         '/api/v1/movimientos',
    #         json=new_movimiento,
    #         headers=auth_headers
    #     )
    #
    #     assert response.status_code == 404