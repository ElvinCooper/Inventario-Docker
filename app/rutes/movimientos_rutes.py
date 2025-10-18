import datetime
import uuid
from datetime import timezone, datetime
from flask_smorest import Blueprint, abort
from flask import request
from ..extensions import db
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from ..models import Producto, Movimientos, Usuario
from ..schemas.error_schema import ErrorSchema
from ..schemas.movimientos_schema import PaginateMovimientoSchema, MovimientoSchema


blp_movimientos = Blueprint('movimientos', __name__, description='Operaciones con movimientos')

#----------- CRUD Movimientos -----------#


@blp_movimientos.route("/movimientos")
class MovimientoResource(MethodView):
    @blp_movimientos.response(HTTPStatus.OK, PaginateMovimientoSchema)
    @jwt_required()  # validacion del token
    def get(self, page =1, per_page=10):
        """ Consultar todos los movimientos en el sistema"""
        pagination = Movimientos.query.paginate(
            page = page,
            per_page =per_page,
            error_out=False
        )

        return {
            "movimientos": pagination.items,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
        }



#-----------  Movimientos por su Id -----------#

@blp_movimientos.route("/movimiento/<string:id_movimiento>")
class MovimientoIdResource(MethodView):
    @blp_movimientos.response(HTTPStatus.OK, MovimientoSchema)
    @jwt_required()
    def get(self, id_movimiento):
        """ Consultar los movimientos por su ID"""
        movimiento = Movimientos.query.get_or_404(id_movimiento)
        if not movimiento :
            abort(HTTPStatus.NOT_FOUND, message="No existe un movimiento con el Id proveeido")

        return movimiento


# -----------  Movimientos por su usuarios -----------#
@blp_movimientos.route("/movimientos/<string:id_usuario>")
class MovimientoUserResource(MethodView):
    @blp_movimientos.response(HTTPStatus.OK, PaginateMovimientoSchema)
    @jwt_required()
    def get(self, id_usuario):
        """ Consultar todos los movimientos de un usuario"""

        # Obtener parámetros de paginación desde query string
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        # Verificar que el usuario existe
        usuario = Usuario.query.get_or_404(id_usuario, description="Usuario no encontrado")

        # Paginar movimientos del usuario ordenados por id
        pagination = Movimientos.query.filter_by(id_usuario=id_usuario).order_by(Movimientos.id_movimiento.asc())\
        .paginate(
            page=page,
            per_page=per_page,
            error_out=False )

        return {
            "movimientos": pagination.items,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
        }




# -----------  Movimientos por tipos  -----------#
@blp_movimientos.route("/tipos-movimientos/<string:tipo_movimiento>")
class MovimientoUserResource(MethodView):
    @blp_movimientos.response(HTTPStatus.OK, PaginateMovimientoSchema, )
    @jwt_required()
    def get(self, tipo_movimiento):
        """ Consultar los movimientos por su tipo"""

        # Obtener parámetros de paginación desde query string
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        # Paginar movimientos del usuario ordenados por su tipo.
        pagination = (Movimientos.query.filter_by(tipo_movimiento=tipo_movimiento).paginate
        (
        page=page,
        per_page=per_page,
        error_out=False ))

        return {
            "movimientos": pagination.items,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.per_page,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
        }