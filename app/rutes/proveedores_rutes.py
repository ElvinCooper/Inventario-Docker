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
from ..models import Proveedor, Producto, Usuario
from ..schemas.error_schema import ErrorSchema
from ..schemas.movimientos_schema import PaginateMovimientoSchema, MovimientoSchema
from ..schemas.proveedor_schema import PaginateProveedorSchema

blp_proveedores = Blueprint('proveedores', __name__, description='Operaciones con Proveedores')



@blp_proveedores.route('/proveedores')
class ProveedoresResource(MethodView):
    @blp_proveedores.response(HTTPStatus.OK, PaginateProveedorSchema)
    @jwt_required()
    def get(self):
        """ Consultar todos los proveedores """

        # Obtener parámetros de paginación desde query string
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        pagination = Proveedor.query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        return {
            "proveedores": pagination.items,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
        }