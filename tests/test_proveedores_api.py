"""Tests para endpoints de proveedores"""
import pytest
from decimal import Decimal
from app.app.models import Proveedor

pytestmark = pytest.mark.integration


@pytest.fixture
def sample_proveedor(db):
    """Crea un proveedor de prueba"""
    proveedor = Proveedor(
        nombre_proveedor='Tech Supplies Inc',
        contact='555-1234',
        direccion='123 Tech Street',
        telefono='8294685123',
        email='contact@techsupplies.com',
        status=True
    )
    db.session.add(proveedor)
    db.session.commit()
    return proveedor


class TestProveedorEndpoints:
    """Tests para endpoints de proveedores"""

    def test_get_all_proveedores_empty(self, client, auth_headers):
        """Test: Listar proveedores vacío"""
        response = client.get('/api/v1/proveedores', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)

        assert isinstance(data['proveedores'], list)
        assert data['total'] == 0

    def test_get_all_proveedores_with_data(self, client, sample_proveedor, auth_headers):
        """Test: Listar proveedores con datos"""
        response = client.get('/api/v1/proveedores', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()
        assert data['total'] > 0
        assert data['proveedores'][0]['nombre_proveedor'] == "Tech Supplies Inc"

    def test_get_proveedor_by_id(self, client, sample_proveedor, auth_headers):
        """Test: Obtener proveedor por ID"""
        response = client.get(f'/api/v1/proveedores/{sample_proveedor.id_proveedor}', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()
        assert data['nombre_proveedor'] == "Tech Supplies Inc"
        assert data['email'] == 'contact@techsupplies.com'

    def test_get_proveedor_not_found(self, client, auth_headers):
        """Test: Proveedor no encontrado"""
        response = client.get('/api/v1/proveedores/99999999-9999-9999-9999-999999999999', headers=auth_headers)

        assert response.status_code == 404

    def test_create_proveedor(self, client, auth_headers):
        """Test: Crear proveedor"""
        new_proveedor = {
            'nombre_proveedor': 'Office Supplies Co',
            'contact': '555-5678',
            'direccion': '456 Office Ave',
            'email': 'info@officesupplies.com',
            'telefono':  '8294685123',
            'status': True
        }

        response = client.post(
            '/api/v1/proveedor/create',
            json=new_proveedor,
            headers=auth_headers
        )

        assert response.status_code == 201
        data = response.get_json()
        assert data['nombre_proveedor'] == 'Office Supplies Co'

    # def test_create_proveedor_duplicate_email(self, client, sample_proveedor, auth_headers):
    #     """Test: No crear proveedor con email duplicado"""
    #     duplicate_proveedor = {
    #         'nombre_proveedor': 'Another Company',
    #         'contact': '555-9999',
    #         'direccion': '789 New St',
    #         'email': 'contact@techsupplies.com',  # Email duplicado
    #         'telefono': '8294685123',
    #         'status': True
    #     }
    #
    #     response = client.post(
    #         '/api/v1/proveedor/create',
    #         json=duplicate_proveedor,
    #         headers=auth_headers
    #     )
    #
    #     assert response.status_code == 400     # debo crear la validacion de no duplicacion de email de proveedor.

    def test_update_proveedor(self, client, sample_proveedor, auth_headers):
        """Test: Actualizar proveedor"""
        updated_data = {
            'contact': '555-NEW1',
            'direccion': 'New Address 123'
        }

        response = client.put(
            f'/api/v1/proveedor/update/{sample_proveedor.id_proveedor}',
            json=updated_data,
            headers=auth_headers
        )

        assert response.status_code == 200
        data = response.get_json()
        assert data['contact'] == '555-NEW1'

    def test_delete_proveedor(self, client, sample_proveedor, auth_headers):
        """Test: Eliminar proveedor"""
        response = client.delete(
            f'/api/v1/proveedor/delete/{sample_proveedor.id_proveedor}',
            headers=auth_headers
        )

        assert response.status_code == 204

        # Verificar que no existe
        get_response = client.get(f'/api/v1/proveedor/{sample_proveedor.id_proveedor}')
        assert get_response.status_code == 404