# Inventario-Dockerizado

**Python 3.12+**

## Descripción

Inventario-Docker es una API RESTful para la gestión de inventarios, construida con Python y Flask. Permite gestionar productos y categorías, cuenta con autenticación básica (JWT), documentación OpenAPI (Swagger) y está preparada para desplegarse con Docker y Docker Compose.

## Características principales

- Gestión de productos: crear, editar, eliminar y listar productos (nombre, descripción, precio, stock, categoría).
- Gestión de categorías.
- Autenticación con JWT (mecanismo básico).
- Documentación automática (OpenAPI / Swagger).
- Pruebas automatizadas con pytest.
- Despliegue con Docker y Docker Compose.
- Base de datos PostgreSQL con migraciones (Alembic/Flask-Migrate).

## Tecnologías

- Python 3.12+
- Flask
- SQLAlchemy
- PostgreSQL
- OpenAPI / Swagger
- Alembic (migraciones)
- Gunicorn (servidor en producción)
- Docker, Docker Compose
- Pytest

---

## Requisitos previos

- Docker y Docker Compose instalados.
- (Opcional) Python 3.12+ para desarrollo local sin Docker.

---

## Quickstart — Despliegue con Docker (recomendado)

1. Clona el repositorio:
```bash
git clone https://github.com/ElvinCooper/Inventario-Docker.git
cd Inventario-Docker
```

2. Crea un archivo .env en la raíz (puedes basarte en .env.example):

3. Levanta los servicios (app + db):
```bash
docker-compose up -d --build
```

4. Comprobar:
- API: http://localhost:8000
- Swagger / documentación interactiva: http://localhost:8000/apidocs 
- Base de datos (mappeada al host): localhost:5433 → contenedor:5432

Ver logs:
```bash
docker-compose logs -f
```

---

## Desarrollo local (sin Docker)

1. Clona el repositorio:
```bash
git clone https://github.com/ElvinCooper/Inventario-Docker.git
cd Inventario-Docker
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

4. Configura la base de datos local (PostgreSQL) y crea la base `inventario_db`. Ajusta variables en `.env` o `config.py`.

5. Ejecuta migraciones (local):
```bash
alembic upgrade head
# o si usas Flask-Migrate
flask db upgrade
```

6. Ejecuta la aplicación en desarrollo:
```bash
export FLASK_APP=app.run
export FLASK_ENV=development
flask run --port 8000
# o para producción local con Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app.run:app
```

---

## Variables de entorno

Crea un archivo `.env` en la raíz (no subir a repositorios públicos con credenciales reales). Un ejemplo básico está en `.env.example`. Variables relevantes (ejemplos):

- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB
- POSTGRES_PORT
- DATABASE_URL (ejemplos abajo)
- SECRET_KEY
- FLASK_ENV

Ejemplos de DATABASE_URL:
- Para ejecución en Docker Compose (desde el contenedor `web`):  
  postgresql://postgres:postgres@db:5432/inventario_db
- Para conexión desde tu host (cuando docker-compose mapea el puerto):  
  postgresql://postgres:postgres@localhost:5433/inventario_db

---

## Migraciones y comandos en contenedor

Si prefieres ejecutar migraciones desde el contenedor (con Docker Compose):
```bash
# Ejecutar alembic dentro del servicio 'web'
docker-compose exec web alembic upgrade head
# o con Flask-Migrate
docker-compose exec web flask db upgrade
```

Para ejecutar tests dentro del contenedor:
```bash
docker-compose exec web pytest --cov=app --cov-report=html
```

Si existe un archivo `docker-compose.test.yaml`, puedes usarlo con:
```bash
docker-compose -f docker-compose.test.yaml up --build
```

---

## Pruebas

Ejecutar pruebas localmente:
```bash
pytest --cov=app --cov-report=html
```
El reporte de cobertura se genera en `htmlcov/`.

---

## Endpoints (resumen)

La documentación interactiva (Swagger) es la fuente canónica. A modo de resumen, algunos endpoints principales:

- POST /api/v1/productos/create — Crear producto (requiere auth según configuración)
- GET /api/v1/productos — Listar productos
- GET /api/v1/productos/{id_producto} — Detalles de producto
- PUT /api/v1/productos/{id_producto} — Actualizar producto
- DELETE /api/v1/productos/{id_producto} — Eliminar producto
- POST /api/v1/categoria/create — Crear categoría
- GET /api/v1/categorias — Listar categorías
- etc.

Ejemplo de payload (JSON) para crear producto:
```json
{
  "name": "Laptop Dell",
  "description": "Laptop con 16GB RAM",
  "price": 1200.00,
  "stock": 10,
  "category_id": 1
}
```

Sugerencia: para ejemplos de uso, usa curl o Postman con el endpoint `/api/v1/productos/create` y el header `Content-Type: application/json`.

---

## Estructura del proyecto (resumen)
```
Inventario-Docker/
├── app/                # Código fuente: routes, models, config, extensions
├── migrations/         # Migraciones Alembic / Flask-Migrate
├── tests/              # Pruebas con pytest
├── Dockerfile
├── docker-compose.yaml
├── docker-compose.test.yaml
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── openapi.json
└── README.md
```

---

## Contribución

Contribuciones bienvenidas. Flujo recomendado:
1. Fork y crea una branch: `git checkout -b feature/mi-feature`
2. Asegúrate de pasar tests: `pytest`
3. Haz push y abre PR describiendo el cambio.

Para contribuciones significativas, considera abrir un issue antes para discutir el diseño.

---

## Licencia

(Indica aquí la licencia que desees; por ejemplo MIT). Añade un archivo LICENSE en la raíz con la licencia seleccionada.

---

## Contacto

Desarrollado por Elvin Cooper  
GitHub: @ElvinCooper  
Email: ing.elvin01cooper@gmail.com

Gracias por tu interés. Si encuentras errores en la documentación o en el código, abre un issue en el repositorio.