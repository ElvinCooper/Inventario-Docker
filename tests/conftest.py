"""
Configuración de fixtures para pytest.
"""
import os

import pytest
import subprocess
import time
from app.run import create_app
from app.extensions import db as _db
from app.models import Usuario, Producto, Categoria, Proveedor, Movimientos

# ============================================
# FIXTURES DE INFRAESTRUCTURA
# ============================================

@pytest.fixture(scope='session', autouse=True)
def docker_db():
    """
    Inicia el contenedor de PostgreSQL antes de todos los tests
    y lo detiene después de todos los tests.

    scope='session': Se ejecuta UNA vez para toda la sesión de tests
    autouse=True: Se ejecuta automáticamente sin necesidad de declararlo
    """
    print("\n Iniciando contenedor de PostgreSQL...")
    subprocess.run(
        ['docker-compose', '-f', 'docker-compose.test.yaml', 'up', '-d'],
        check=True
    )

    # Esperar a que PostgreSQL esté listo
    print(" Esperando a que PostgreSQL esté listo...")
    time.sleep(5)

    yield  # Aquí se ejecutan todos los tests

    print("\n Deteniendo contenedor de PostgreSQL...")
    subprocess.run(
        ['docker-compose', '-f', 'docker-compose.test.yaml', 'down', '-v'],
        check=True
    )


@pytest.fixture(scope='session')
def app():
    """
    Crea la aplicación Flask configurada para testing.

    scope='session': Se crea UNA vez y se comparte entre todos los tests
    """
    os.environ["FLASK_ENV"] = "testing"
    app = create_app("testing")

    # Configuración específica para testing
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'postgresql://test_user:test_password@localhost:5434/test_inventory',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'JWT_SECRET_KEY': 'test-secret-key-do-not-use-in-production',
        'WTF_CSRF_ENABLED': False,
    })

    # Crear todas las tablas
    with app.app_context():
        _db.create_all()

    yield app

    # Limpiar después de todos los tests
    with app.app_context():
        _db.drop_all()


@pytest.fixture(scope='function')
def db(app):
    """
    Proporciona una sesión de base de datos limpia para cada test.

    scope='function': Se ejecuta antes de CADA test individual
    Esto asegura que cada test comience con una BD vacía
    """
    with app.app_context():
        # Limpiar todas las tablas antes del test
        _db.session.remove()
        _db.drop_all()
        _db.create_all()

        yield _db

        # Rollback después del test
        _db.session.remove()


@pytest.fixture
def client(app):
    """
    Cliente de prueba para hacer peticiones HTTP a la API.

    Uso:
        response = client.get('/api/v1/productos')
        response = client.post('/api/v1/productos', json={...})
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """
    Runner para comandos CLI de Flask.

    Uso:
        result = runner.invoke(args=['db', 'init'])
    """
    return app.test_cli_runner()


# ============================================
# FIXTURES DE DATOS DE PRUEBA
# ============================================

@pytest.fixture
def sample_user(db):
    """
    Crea un usuario de ejemplo en la BD.

    """
    user = Usuario(
        nombre='testuser',
        email='test@example.com',
        # Asume que tienes un método para hashear contraseñas
        # password_hash=generate_password_hash('testpassword')
    )
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def sample_category(db):
    """
    Crea una categoría de ejemplo.
    """
    category = Categoria(
        nombre_categoria='Electronics',
        descripcion_cat='Electronic devices and accessories'
    )
    db.session.add(category)
    db.session.commit()
    return category


@pytest.fixture
def sample_product(db, sample_category):
    """
    Crea un producto de ejemplo.

    Nota que depende de sample_category (se ejecuta automáticamente).
    """
    product = Producto(
        nombre_producto='Laptop',
        descripcion='High-performance laptop',
        status=True
    )
    db.session.add(product)
    db.session.commit()
    return product


@pytest.fixture
def auth_token(client, sample_user):
    """
    Obtiene un token JWT válido para autenticación.
    """
    response = client.post('/api/v1/auth/login', json={
        'email': 'testuser',
        'password_hash': 'testpassword'
    })

    if response.status_code == 200:
        data = response.get_json()
        return data.get('access_token')
    return None


@pytest.fixture
def auth_headers(auth_token):
    """
    Headers con autenticación para peticiones protegidas.

    Uso:
        response = client.get('/api/protected', headers=auth_headers)
    """
    if auth_token:
        return {
            'Authorization': f'Bearer {auth_token}',
            'Content-Type': 'application/json'
        }
    return {'Content-Type': 'application/json'}
