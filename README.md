# <span style="color:green"> Inventario-Dockerizado </span>
### <span style="color:green"> Python Version 3.11 </span>
#### <span style="color:green"> Descripción: </span>

Inventario-Docker es una API RESTful completa para la gestión de inventarios, diseñada con un enfoque en la escalabilidad y la facilidad de despliegue. Esta aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre productos, categorías y existencias en un sistema de inventario.
Utilizando un stack moderno y ligero, la API está construida con Python y Flask como framework web, SQLAlchemy para el manejo de ORM y base de datos relacional con PostgreSQL. Incluye documentación interactiva mediante OpenAPI (Swagger) para facilitar el testing y el uso, y pruebas unitarias con Pytest para garantizar la calidad del código. Todo el proyecto está dockerizado, lo que permite un despliegue rápido y consistente en cualquier entorno.

### <span style="color:green"> Características Principales: </span>

**Gestión de Productos:** Agregar, editar, eliminar y buscar productos con detalles como nombre, descripción, precio y stock.

**Categorías:** Organización de productos en categorías para una mejor clasificación.

**Autenticación y Autorización:** Soporte básico para JWT (puedes extenderlo según necesidades).

**Documentación Automática:** Swagger UI integrado para explorar y probar endpoints en tiempo real.

**Pruebas Automatizadas:** Cobertura de tests con Pytest para endpoints y lógica de negocio.

**Despliegue Fácil:** Configuración con Docker y Docker Compose para desarrollo y producción.

**Base de Datos Robusta:** PostgreSQL con migraciones gestionadas por Alembic (opcional, integrable).

Ideal para startups, e-commerce o cualquier sistema que requiera control de stock eficiente.
Tecnologías Utilizadas

 - Backend: Python 3.9+, Flask, SQLAlchemy 
 - Base de Datos: PostgreSQL
 - Documentación API: Flask-RESTX / OpenAPI (Swagger)
 - Testing: Pytest, Pytest-Cov
 - Contenerización: Docker, Docker Compose
 - Otras: Alembic (para migraciones), Gunicorn (para producción)

### <span style="color:green"> Requisitos Previos: </span>

- Docker y Docker Compose instalados.
- Python 3.9+ (para desarrollo local sin Docker).
- it para clonar el repositorio.

**Instalación:**

**Opción 1:** Despliegue con Docker (Recomendado)

- Clona el repositorio:textgit clone https://github.com/ElvinCooper/Inventario-Docker.git
- cd Inventario-Docker
- Inicia los servicios (API + PostgreSQL):textdocker-compose up -d --build 
- Esto levantará: La API en http://localhost:5000
- La base de datos PostgreSQL en localhost:5432 (con variables de entorno por defecto).

**Verifica el despliegue:**

- Accede a Swagger en http://localhost:5000/swagger para probar endpoints.
- Revisa los logs con docker-compose logs -f.


**Opción 2:** Desarrollo Local (Sin Docker)

- Clona el repositorio como arriba.
- Crea un entorno virtual:textpython -m venv venv
- source venv/bin/activate  # En Windows: venv\Scripts\activate
- Instala dependencias:textpip install -r requirements.txt
- Configura la base de datos:
- Instala y levanta PostgreSQL localmente.
- Crea una base de datos llamada inventario_db.
- Actualiza las variables en .env (o config.py).

**Ejecuta migraciones (si usas Alembic):** textalembic upgrade head
**Inicia la aplicación:textflask run --debugO con Gunicorn para producción:** gunicorn -w 4 -b 0.0.0.0:5000 app:app.

Uso
### <span style="color:green"> Endpoints Principales: </span>

La documentación interactiva está disponible en http://localhost:8000/apidocs. Aquí una tabla con los endpoints principales:

| Método | Endpoint                           | Descripción                          | Autenticación |
|--------|------------------------------------|--------------------------------------|---------------|
| POST   | `/api/v1/productos/create`         | Crear un nuevo producto             | Opcional     |
| GET    | `/api/v1/productos`                | Listar todos los productos          | No           |
| GET    | `/api/v1/productos/<id_producto>`  | Obtener detalles de un producto     | No           |
| PUT    | `/api/v1/productos/<id_producto>`  | Actualizar un producto              | Requerida    |
| DELETE | `/api/v1/productos/<id_producto>`  | Eliminar un producto                | Requerida    |
| POST   | `/api/v1/categoria/create`         | Crear una nueva categoría           | Opcional     |
| GET    | `/api/v1/categorias`               | Listar todas las categorías         | No           |
| GET    | `/api/v1/categoria/<id_categoria>` | Obtener una categoría por ID        | No           |
| PUT    | `/api/v1/categoria/<id_categoria>` | Actualizar una categoría            | Requerida    |
| DELETE | `/api/v1/categoria/<id_categoria>` | Eliminar una categoría              | Requerida    |




**Ejemplo de request (POST /api/products):**

```python 
json{
  "name": "Laptop Dell",
  "description": "Laptop de 16GB RAM",
  "price": 1200.00,
  "stock": 10,
  "category_id": 1
}
```

### Variables de Entorno
**Crea un archivo .env en la raíz:**
```text
 DATABASE_URL=postgresql://user:password@localhost:5432/inventario_db

SECRET_KEY=tu_clave_secreta_aqui
FLASK_ENV=development
```

### Pruebas
**Ejecuta las pruebas unitarias:**
```text 
pytest --cov=app --cov-report=html
```
Esto genera un reporte de cobertura en htmlcov/. Las pruebas cubren endpoints, modelos de DB y lógica de validación.

Inventario \
├── .github \
├── app  
│   ├── routes  \        # Definición de endpoints 
│   ├── schemas \        # Esquemas Marshmallow / Pydantic (opcional) 
│   ├── __init__.py  \   # Inicialización de Flask 
│   ├── extensions.py \  # Inicialización de Flask 
│   ├── models.py      \ # Modelos SQLAlchemy (Product, Category, etc.) 
│   ├── run.py         \ # Inicialización de Flask 
│   ├── wsgi.py        \ # Inicialización de Flask  
│   ├── config.py      \ # Configuraciones de la app 
│   └── run.py \
├── htmlcov \
│    ├── index.html \
│    ├── ect... \

├── tests \
│   ├── __init__.py \
│   ├── test_products.py  # Pruebas para productos \
│   ├── test_categories.py # Pruebas para categorías \
│   └── conftest.py       # Fixtures compartidas (pytest) \
├── migrations/           # Migraciones con Alembic \
├── Dockerfile            # Imagen Docker de la API \
├── docker-compose.yml    # Servicios: app + db \
├── requirements.txt      # Dependencias Python \
├── .env.example          # Plantilla de variables de entorno \
├── .gitignore \
└── README.md             # Este archivo \



### <span style="color:green"> Contribución </span>
**Las contribuciones son bienvenidas! Sigue estos pasos:**

- Forkea el repositorio.
- Crea una branch para tu feature: git checkout -b feature/nueva-funcionalidad.
- Commitea tus cambios: git commit -m 'Agrega nueva funcionalidad'.
- Pushea a la branch: git push origin feature/nueva-funcionalidad.
- Abre un Pull Request.

Asegúrate de correr pruebas antes de subir cambios: pytest.
Licencia

**Contacto** \
Desarrollado por Elvin Cooper

GitHub: @ElvinCooper
Email: ing.elvin01cooper@gmail.com

¡Gracias por el interés! Si encuentras issues o tienes sugerencias, abre un ticket en el repo.

