import os
from base64 import urlsafe_b64decode

from flask import Flask
from .extensions import init_extensions
from dotenv import load_dotenv
from .models import Producto, Categoria
from flask import jsonify
from .rutes.productos_rutes import productos_bp
from .rutes.user_rutes import usuario_bp
from .rutes.movimientos_rutes import blp_movimientos
from werkzeug.exceptions import HTTPException


load_dotenv()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar extensiones
    init_extensions(app)

    # Registrar blueprints de las rutas
    app.register_blueprint(productos_bp, url_prefix="/api/v1")
    app.register_blueprint(usuario_bp, url_prefix="/api/v1")
    app.register_blueprint(blp_movimientos, url_prefix="/api/v1")

    return app

app = create_app()

if __name__ == '__main__':
    create_app().run(host="0.0.0.0", port=8000, debug=True)
