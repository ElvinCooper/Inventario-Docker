import os
from base64 import urlsafe_b64decode

from flask import Flask
from .extensions import init_extensions, db
from dotenv import load_dotenv
from .models import Producto, Categoria
from flask import jsonify
from .rutes.productos_rutes import productos_bp
from .rutes.user_rutes import usuario_bp
from .rutes.movimientos_rutes import blp_movimientos
from .rutes.categorias_rutes import blp_categorias
from .rutes.proveedores_rutes import blp_proveedores
from werkzeug.exceptions import HTTPException
from .config import DevelopmentConfig, ProductionConfig
from flask_smorest import Api
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Configuracion del entorno
    env = os.getenv("FLASK_ENV", "development")

    app.config.from_object(DevelopmentConfig)

    api = Api(app)

    if not app.config.get('SQLALCHEMY_DATABASE_URI'):
        raise ValueError(f"SQLALCHEMY_DATABASE_URI no está configurado para el entorno: {env}")


    # Inicializar extensiones
    init_extensions(app)


    # Registrar blueprints de las rutas
    api.register_blueprint(usuario_bp, url_prefix="/api/v1")
    api.register_blueprint(productos_bp, url_prefix="/api/v1")
    api.register_blueprint(blp_categorias, url_prefix="/api/v1")
    api.register_blueprint(blp_proveedores, url_prefix="/api/v1")
    api.register_blueprint(blp_movimientos, url_prefix="/api/v1")


    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)