import datetime
import uuid
from datetime import timezone, datetime
from urllib import request
from flask_smorest import Blueprint, abort
from ..extensions import db
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt, get_jwt_identity
from flask.views import MethodView
from ..models import Usuario, TokenBlocklist
from ..schemas.error_schema import ErrorSchema
from ..schemas.user_schemas import UserSimpleSchema, LoginSchema, LoginResponseSchema, LogoutResponseSchema, TokenRefreshResponseSchema
from flask import jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import HTTPException
usuario_bp = Blueprint('user', __name__, description='Operaciones con usuarios')


#------------ Endpoint para consultar todos los usuarios del sistema ------------#
@usuario_bp.route('/usuarios')
class UserResource(MethodView):
    @usuario_bp.response(HTTPStatus.OK, UserSimpleSchema(many=True))
    @usuario_bp.alt_response(HTTPStatus.UNAUTHORIZED, schema=ErrorSchema, description="No autorizado", example={"succes": False, "message": "No autorizado"})
    @usuario_bp.alt_response(HTTPStatus.INTERNAL_SERVER_ERROR, schema=ErrorSchema, description="Error interno del servidor", example={"succes": False, "message": "Error interno del servidor"})
    # @jwt_required()
    def get(self):
        """ Consultar todos los usuarios del sistema """
        usuarios = Usuario.query.all()

        return usuarios

# ------- Endpoint para consultar un usuario por su Id ----------#
@usuario_bp.route('/usuario/<string:id_usuario>')
class UserIdResource(MethodView):
    @usuario_bp.response(HTTPStatus.OK, UserSimpleSchema)
    @usuario_bp.alt_response(HTTPStatus.NOT_FOUND, schema=ErrorSchema, description="Usuario no encontrado", example={"succes": False, "message": "Usuario no encontrado"})
    @usuario_bp.alt_response(HTTPStatus.INTERNAL_SERVER_ERROR, schema=ErrorSchema, description="Error interno del servidor", example={"succes": False, "message": "Error interno del servidor"})

    #@jwt_required()
    def get(self, id_usuario):
        """ Consultar un usuario por su Id"""
        usuario = Usuario.query.filter_by(id_usuario=id_usuario).first()
        if not usuario:
            #abort(HTTPStatus.NOT_FOUND, errors={"message": "Usuario no encontrado"})
            return jsonify({"succes": False,
                            "message": "No existe ningun usuario con este Id"}), HTTPStatus.NOT_FOUND

        return usuario


#--------- Endpoint para hacer login de un usuario del sistema ---------#
@usuario_bp.route('/auth/login', methods=['POST'])
@usuario_bp.arguments(LoginSchema)
@usuario_bp.response(HTTPStatus.OK, LoginResponseSchema)
@usuario_bp.alt_response(HTTPStatus.UNAUTHORIZED, schema=ErrorSchema, description="No esta autorizado", example={"success": False, "message": "No esta autorizado"})
@usuario_bp.alt_response(HTTPStatus.INTERNAL_SERVER_ERROR, schema=ErrorSchema, description="Error al generar token", example={"success": False, "message": "Error interno del servidor"})
def login_user(data_login):
    """ Login de usuarios """
    try:
        # Buscar usuario por email proveeido
        usuario = Usuario.query.filter_by(email=data_login['email']).first()
        if not usuario:
            current_app.logger.warning(f"Intento de login con email inexistente: {data_login['email']}")
            return({"message":f"Credenciales Invalidas"}), HTTPStatus.UNAUTHORIZED

        #if not check_password_hash(usuario.password_hash, data_login.get("password_hash")):
        if usuario.password_hash != data_login['password_hash']:
            return ({"message":"Credenciales Invalidas password"}), HTTPStatus.UNAUTHORIZED

        # Generar token de authentication
        additional_claims = {"rol": usuario.rol}
        access_token = create_access_token(identity=usuario.id_usuario, additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=usuario.id_usuario)

        response = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "usuario": {
                "id_usuario": usuario.id_usuario,
                "nombre": usuario.nombre,
                "email": usuario.email,
                "rol": {"descripcion": usuario.rol}
            },
            "message": "Login exitoso"
        }

        return response, HTTPStatus.OK

    except HTTPException as http_exc:
        raise http_exc  # esto permite que pasen errores como 401, 400 etc...
    except Exception as e:
        current_app.logger.error(f"Error en login: {str(e)}")
        return {"success": False,
                "message": f"Error interno: {str(e)}"}, HTTPStatus.INTERNAL_SERVER_ERROR





# ------------------ Endpoint para Logout -----------------------#

@usuario_bp.route('/auth/logout')
class LogoutResource(MethodView):
    @jwt_required()
    @usuario_bp.response(HTTPStatus.OK, LogoutResponseSchema)
    def post(self):
        """ Logout usuarios  """
        jti =get_jwt()['jti']
        db.session.add(TokenBlocklist(jti=jti))
        db.session.commit()
        return {"mensaje": "Sesion cerrada con exito"}


# ------------------ Endpoint para renovar los tokens -------------------#

@usuario_bp.route('/auth/refresh')
class RefreshToken(MethodView):
    @jwt_required()
    @usuario_bp.response(HTTPStatus.OK, TokenRefreshResponseSchema)
    def post(self):
        """ Renovar los tokens """
        jwt_payload = get_jwt()
        jti = jwt_payload['jti']
        identity = get_jwt_identity()

        # verificar si el token está revocado
        if TokenBlocklist.query.filter_by(jti=jti).first():
            abort(HTTPStatus.UNAUTHORIZED, message="Refresh token revocado")

        # Revocar el token actual
        db.session.add(TokenBlocklist(jti=jti))
        db.session.commit()

        # Generar nuevos tokens
        new_access_token = create_access_token(identity=identity)
        new_refresh_token = create_refresh_token(identity=identity)

        return {
            "acces_token": new_access_token,
            "refresh_token": new_refresh_token
        }