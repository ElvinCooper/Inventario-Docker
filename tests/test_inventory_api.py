"""
Tests de integración para los endpoints de la API.
"""
import pytest
from app.models import Producto
from decimal import Decimal
# Marcar tests como integración
pytestmark = pytest.mark.integration


class TestProductEndpoints:
    """Tests para endpoints de productos"""

    def test_get_all_products_empty(self, client, auth_headers):
        """Test: Obtener productos cuando la BD está vacía"""
        response = client.get('/api/v1/productos', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()

        # verificar que es un diccionario
        assert isinstance(data, dict)

        # verificar que el total de elementos es 0
        assert data['total'] == 0

        # verificar que la clave que contiene la lista de productos está vacía.
        assert isinstance(data['productos'], list)
        assert len(data['productos']) == 0



    def test_get_all_products_with_data(self, client, sample_product, auth_headers):
        """Test: Obtener productos cuando hay datos"""
        response = client.get('/api/v1/productos', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()

        assert data['total'] == 1

        # acceder a la lista de productos dentro del diccionario
        productos_list = data['productos']

        assert productos_list[0]['nombre_producto'] == 'Laptop'

    def test_get_product_by_id(self, client, sample_product, auth_headers):
        """Test: Obtener un producto específico por ID"""
        response = client.get(f'/api/v1/productos/{sample_product.id_producto}', headers=auth_headers)

        assert response.status_code == 200
        data = response.get_json()
        assert data['id_producto'] == sample_product.id_producto
        assert data['nombre_producto'] == 'Laptop'

    def test_get_product_not_found(self, client, auth_headers):
        """Test: Obtener un producto que no existe"""
        response = client.get('/api/v1/products/9999', headers=auth_headers)

        assert response.status_code == 404

    def test_create_product(self, client, sample_category, auth_headers):
        """Test: Crear un nuevo producto"""
        new_product = {
            'nombre_producto': 'Mouse',
            'descripcion': 'Wireless mouse',
            "imagen_url": "https://www.cafesantodomingo.com.do/imagenprueba",
            "codigo_barras": "434973445467486",
            'precio': 29.99,
            'stock_actual': 50,
            "stock_minimo": 25,
            'id_categoria': sample_category.id_categoria,
            'status':True
        }

        response = client.post(
            '/api/v1/productos/create',
            json=new_product,
            headers=auth_headers
        )

        assert response.status_code == 201
        data = response.get_json()
        assert data['nombre_producto'] == 'Mouse'
        assert Decimal(data['precio']) == Decimal("29.99")
        assert  data['stock_actual']
        assert data['stock_minimo'] == 25
        assert data['id_categoria'] == sample_category.id_categoria
        assert data['status']

    def test_create_product_invalid_data(self, client, sample_category, auth_headers):
        """Test: Crear producto con datos inválidos"""
        invalid_product = {
            'nombre_producto': '',
            'descripcion': 'Wireless mouse',
            "imagen_url": "https://www.cafesantodomingo.com.do/imagenprueba",
            "codigo_barras": "434973445467486",
            'precio': -10,
            'stock_actual': 50,
            "stock_minimo": 25,
            'id_categoria': sample_category.id_categoria,
            'status': True
        }

        response = client.post(
            '/api/v1/productos/create',
            json=invalid_product,
            headers=auth_headers
        )

        assert response.status_code == 422

    def test_update_product(self, client, sample_product, auth_headers):
        """Test: Actualizar un producto existente"""
        updated_data = {
            'nombre_producto': "my new product",
            'descripcion': "this is a test product",
            "precio": 244.99,
            "stock_actual": 42
        }

        response = client.put(
            f'/api/v1/productos/update/{sample_product.id_producto}',
            json=updated_data,
            headers=auth_headers
        )

        assert response.status_code == 200
        data = response.get_json()
        assert data['nombre_producto'] == "my new product"
        assert data['descripcion'] == "this is a test product"
        assert Decimal(data['precio']) == Decimal("244.99")
        assert data['stock_actual'] == 42


    def test_delete_product(self, client, sample_product, auth_headers):
        """Test: Eliminar un producto"""
        response = client.delete(
            f'/api/v1/productos/delete/{sample_product.id_producto}', headers=auth_headers)

        assert response.status_code == 200

        # Verificar que ya no existe
        get_response = client.get(f'/api/v1/productos/{sample_product.id_producto}', headers=auth_headers)
        assert get_response.status_code == 404


# class TestCategoryEndpoints:
#     """Tests para endpoints de categorías"""
#
#     def test_get_all_categories(self, client, sample_category):
#         """Test: Obtener todas las categorías"""
#         response = client.get('/api/categories')
#
#         assert response.status_code == 200
#         data = response.get_json()
#         assert len(data) >= 1
#         assert data[0]['name'] == 'Electronics'
#
#     def test_create_category(self, client, auth_headers):
#         """Test: Crear una nueva categoría"""
#         new_category = {
#             'name': 'Books',
#             'description': 'Books and publications'
#         }
#
#         response = client.post(
#             '/api/categories',
#             json=new_category,
#             headers=auth_headers
#         )
#
#         assert response.status_code == 201
#         data = response.get_json()
#         assert data['name'] == 'Books'
#
#
# class TestInventoryEndpoints:
#     """Tests para endpoints de inventario"""
#
#     def test_get_low_stock_products(self, client, db, sample_category):
#         """Test: Obtener productos con stock bajo"""
#         # Crear producto con stock bajo
#         low_stock_product = Product(
#             name='Low Stock Item',
#             description='Test',
#             price=10.00,
#             stock=2,  # Stock bajo
#             category_id=sample_category.id
#         )
#         db.session.add(low_stock_product)
#         db.session.commit()
#
#         response = client.get('/api/inventory/low-stock')
#
#         assert response.status_code == 200
#         data = response.get_json()
#         assert len(data) >= 1
#         assert any(p['name'] == 'Low Stock Item' for p in data)
