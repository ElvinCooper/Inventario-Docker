from flask_smorest import Blueprint, abort as smorest_abort
from flask.views import MethodView
from flask import current_app
from http import HTTPStatus
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from ..schemas.password_reset_schema import (RequestPasswordResetSchema, ResetPasswordSchema, PasswordResetResponseSchema)
from ..models import Usuario
from ..services.mailer import send_password_reset_email
from ..extensions import db
from ..limiter import limiter

password_reset_bp = Blueprint('password_reset', __name__, description='Recuperación de contraseña')


@password_reset_bp.route('/password/reset')
class PasswordResetResource(MethodView):

    @password_reset_bp.arguments(RequestPasswordResetSchema)
    @password_reset_bp.response(HTTPStatus.OK, PasswordResetResponseSchema)
    #@require_api_key()
    @limiter.limit("3 per hour")
    def post(self, data):
        """Solicitar reset de contraseña - Envía email con token"""
        try:
            email = data['email']
            usuario = Usuario.query.filter_by(email=email).first()

            # Siempre retornar éxito (no revelar si email existe)
            if not usuario:
                return {
                    "success": True,
                    "message": "Recibirás un email con instrucciones"
                }, HTTPStatus.OK

            # Generar token JWT temporal (1 hora)
            token = create_access_token(
                identity=usuario.id_usuario,
                expires_delta=timedelta(hours=1),
                additional_claims={"type": "password_reset"}
            )

            # Enviar email
            try:
                send_password_reset_email(usuario.email, usuario.nombre, token)
                current_app.logger.info(f"Email de reset enviado a: {usuario.email}")
            except Exception as e:
                current_app.logger.error(f"Error enviando email: {str(e)}")

            return {
                "success": True,
                "message": "Si el email existe, recibirás instrucciones"
            }, HTTPStatus.OK

        except Exception as e:
            current_app.logger.error(f"Error: {str(e)}")
            smorest_abort(HTTPStatus.INTERNAL_SERVER_ERROR, message="Error procesando solicitud")


    @password_reset_bp.arguments(ResetPasswordSchema)
    @password_reset_bp.response(HTTPStatus.OK, PasswordResetResponseSchema)
    #@require_api_key()
    @limiter.limit("5 per hour")
    @jwt_required()
    def put(self, data):
        """Confirmar reset - Cambia la contraseña con el token"""
        try:
            # Obtener usuario del token
            user_id = get_jwt_identity()
            usuario = Usuario.query.get(user_id)

            if not usuario:
                smorest_abort(HTTPStatus.NOT_FOUND, message="Usuario no encontrado")

            # Actualizar contraseña
            usuario.password = generate_password_hash(data['new_password'])
            db.session.commit()

            current_app.logger.info(f"Contraseña reseteada: {usuario.email}")

            return {
                "success": True,
                "message": "Contraseña actualizada exitosamente"
            }, HTTPStatus.OK

        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error: {str(e)}")
            smorest_abort(HTTPStatus.INTERNAL_SERVER_ERROR, message="Error al resetear contraseña")