import datetime
import uuid
from datetime import timezone, datetime
from urllib import request

from flask_smorest import Blueprint, abort
from ..extensions import db
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from ..models import Usuario
from ..schemas.error_schema import ErrorSchema
from ..schemas.user_schemas import UserSimpleSchema

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




