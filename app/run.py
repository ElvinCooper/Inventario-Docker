import os
from flask import Flask
from .extensions import init_extensions, db
from dotenv import load_dotenv
from flask import jsonify
from flask_migrate import Migrate, upgrade as migrate_upgrade
from werkzeug.exceptions import HTTPException
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from flask_smorest import Api
from .limiter import init_limiter



def create_app(env=None):
    load_dotenv()

    # Detectar el entorno
    env = os.getenv("FLASK_ENV", "development").lower()
    print(f"[INFO] Entorno detectado: {env}")  # debug temporal

    app = Flask(__name__)

    #app.config.from_object(DevelopmentConfig)
    # Configuracion del entorno
    if env == "development":
        app.config.from_object(DevelopmentConfig)
    elif env == "production":
        app.config.from_object(ProductionConfig)
    else :
        app.config.from_object(TestingConfig)

    # Inicializar extensiones
    init_extensions(app)
    init_limiter(app)

    from .rutes.productos_rutes import productos_bp
    from .rutes.user_rutes import usuario_bp
    from .rutes.movimientos_rutes import blp_movimientos
    from .rutes.categorias_rutes import blp_categorias
    from .rutes.proveedores_rutes import blp_proveedores
    from .rutes.password_reset_rutes import password_reset_bp

    api = Api(app)

    # EJECUTAR MIGRACIONES AL INICIAR (solo en producción)
    if env == "production":
        with app.app_context():
            try:
                print("Ejecutando migraciones automáticas...")
                migrate_upgrade()
                print("Migraciones completadas!")
            except Exception as e:
                print(f"Error en las migraciones: {e}")

    if not app.config.get('SQLALCHEMY_DATABASE_URI'):
        raise ValueError(f"SQLALCHEMY_DATABASE_URI no está configurado para el entorno: {env}")

    # Registrar blueprints de las rutas
    api.register_blueprint(usuario_bp, url_prefix="/api/v1")
    api.register_blueprint(productos_bp, url_prefix="/api/v1")
    api.register_blueprint(blp_categorias, url_prefix="/api/v1")
    api.register_blueprint(blp_proveedores, url_prefix="/api/v1")
    api.register_blueprint(blp_movimientos, url_prefix="/api/v1")
    api.register_blueprint(password_reset_bp, url_prefix="/api/v1")

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
