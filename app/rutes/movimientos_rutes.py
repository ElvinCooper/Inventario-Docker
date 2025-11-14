import datetime
import uuid
from datetime import timezone, datetime
from flask_smorest import Blueprint, abort
from flask import request
from ..extensions import db
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from ..models import Producto, Movimientos, Usuario
from ..schemas.error_schema import ErrorSchema
from ..schemas.movimientos_schema import PaginateMovimientoSchema, MovimientoSchema


blp_movimientos = Blueprint('Movimientos', __name__, description='Operaciones con movimientos')

#----------- CRUD Movimientos -----------#

@blp_movimientos.route("/movimiento/create")
class CreateMovimientoResource(MethodView):
    @blp_movimientos.arguments(MovimientoSchema)
    @blp_movimientos.response(HTTPStatus.CREATED, MovimientoSchema)
    @blp_movimientos.alt_response(HTTPStatus.INTERNAL_SERVER_ERROR, schema=ErrorSchema, description="Error interno del servidor", example={"succes": False, "message": "Error interno del servidor"})
    @jwt_required()
    def post(self, data_movimiento):
        """Registrar un nuevo movimiento en el sistema"""

        # Obtener usuario del token
        current_user_id = get_jwt_identity()

        # Verificar que el producto existe
        producto = Producto.query.get(data_movimiento["id_producto"])
        if not producto:
            abort(HTTPStatus.NOT_FOUND, message="Producto no encontrado")

        nuevo_movimiento = Movimientos(
            id_movimiento=str(uuid.uuid4()),
            id_producto=data_movimiento["id_producto"],
            id_usuario=current_user_id,
            tipo_movimiento=data_movimiento["tipo_movimiento"],
            cantidad=data_movimiento["cantidad"],
            precio_unitario=data_movimiento["precio_unitario"],
            motivo=data_movimiento["motivo"],
            referencia=data_movimiento["referencia"],
            fecha_movimiento=datetime.now(timezone.utc),
            observaciones=data_movimiento.get("observaciones")
        )

        # Actualizar stock según tipo de movimiento
        if nuevo_movimiento.tipo_movimiento.lower() == 'entrada':
            producto.stock_actual += nuevo_movimiento.cantidad
        elif nuevo_movimiento.tipo_movimiento.lower() == 'salida':
            if producto.stock_actual < nuevo_movimiento.cantidad:
                abort(HTTPStatus.BAD_REQUEST, message="Stock insuficiente")
            producto.stock_actual -= nuevo_movimiento.cantidad

        db.session.add(nuevo_movimiento)
        db.session.commit()

        return nuevo_movimiento, HTTPStatus.CREATED




#--------------------------- Listar todos los movimientos del sistema --------------------------------#
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
        movimiento = Movimientos.query.get_or_404(id_movimiento, description="Movimiento no existe")

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