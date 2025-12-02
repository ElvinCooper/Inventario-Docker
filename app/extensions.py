from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask import jsonify
from flask_mail import Mail


db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
migrate = Migrate()
mail = Mail()


def init_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)

    # Log de configuracion de desarrollo
    if app.config['DEBUG']:
       app.logger.info(f"Mail Server: {app.config.get('MAIL_SERVER')}")
       app.logger.info(f"Mail Port: {app.config.get('MAIL_PORT')}")
       app.logger.info(f"Mail Username: {app.config.get('MAIL_USERNAME')}")

    # CRÍTICO: Inicialización de JWTManager
    jwt.init_app(app)

    # CRÍTICO: Definición de los manejadores de errores de JWT
    @jwt.unauthorized_loader
    def missing_token_callback(callback):
        return (
            jsonify(
                {
                    "msg": "Falta el token de acceso en la cabecera Authorization (Bearer).",
                    "error": "unauthorized_error",
                }
            ),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {
                    "msg": "El token proporcionado no es válido, ha expirado o está malformado.",
                    "error": "invalid_token_error",
                }
            ),
            401,
        )



    migrate.init_app(app, db)
