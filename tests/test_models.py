"""
Tests unitarios para los modelos de la base de datos.
"""
from decimal import Decimal
from werkzeug.security import generate_password_hash, check_password_hash
import pytest
from app.app.models import Producto, Categoria, Usuario, Proveedor, Movimientos

# Marcar tests como unitarios
pytestmark = pytest.mark.unit


class TestProductModel:
    """Tests para el modelo Producto"""

    def test_create_product(self, db, sample_category):
        """Test: Crear un producto básico"""
        product = Producto(
            nombre_producto='Test Product',
            descripcion='Test description',
            imagen_url='https://test.com',
            codigo_barras='4303123454678',
            precio=99.99,
            stock_minimo=50,
            stock_actual=5,
            id_categoria=sample_category.id_categoria,
            status=sample_category.status,
        )
        db.session.add(product)
        db.session.commit()

        # Verificar que se guardó correctamente
        assert product.id_producto is not None
        assert product.nombre_producto == 'Test Product'
        assert product.descripcion == 'Test description'
        assert product.imagen_url == 'https://test.com'
        assert product.codigo_barras == '4303123454678'
        assert product.precio == Decimal("99.99")
        assert product.stock_minimo == 50
        assert product.stock_actual == 5
        assert product.id_categoria == sample_category.id_categoria
        assert product.status == sample_category.status

    def test_product_repr(self, sample_product):
        """Test: Representación en string del producto"""
        assert sample_product.nombre_producto == 'Laptop'

    def test_product_relationship_with_category(self, sample_product, sample_category):
        """Test: Relación entre producto y categoría"""
        assert sample_product.id_categoria == sample_category.id_categoria
        assert sample_product.categoria.nombre_categoria == 'Electronics'


class TestCategoryModel:
    """Tests para el modelo Categoria"""

    def test_create_category(self, db):
        """Test: Crear una categoría"""
        category = Categoria(
            nombre_categoria='Furniture',
            descripcion_cat='Home and office furniture'
        )
        db.session.add(category)
        db.session.commit()

        assert category.id_categoria is not None
        assert category.nombre_categoria == 'Furniture'


    def test_category_unique_name(self, client, auth_headers, sample_category):
        """Test: Los nombres de categoría deben ser únicos"""

        duplicate_category = {
            "nombre_categoria":"Electronics",
            "descripcion_cat":"Another electronics category",
            "status":True
        }

        response = client.post("/api/v1/categoria/create",
                               json=duplicate_category,
                               headers=auth_headers)

        assert response.status_code == 409


class TestUserModel:
    """Tests para el modelo Usuario"""

    def test_create_user(self, db):
        """Test: Crear un usuario"""
        user = Usuario(
            nombre='newuser',
            email='new@example.com',
            password_hash=generate_password_hash('testnewuser'),
            rol="Administrador"
        )
        db.session.add(user)
        db.session.commit()

        assert user.id_usuario is not None
        assert user.nombre == 'newuser'
        assert user.email == 'new@example.com'

    def test_password_hashing(self, sample_user):
        """Test: Las contraseñas deben estar hasheadas"""

        assert sample_user.password_hash != 'testpassword'
        assert sample_user.check_password('testpassword') is True
