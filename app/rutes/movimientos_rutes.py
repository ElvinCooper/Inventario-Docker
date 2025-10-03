import datetime
import uuid
from datetime import timezone, datetime
from flask_smorest import Blueprint, abort
from ..extensions import db
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from ..models import Producto, Movimientos, Usuario
from ..schemas.error_schema import ErrorSchema
from ..schemas.movimientos_schema import PaginateMovimientoSchema


blp_movimientos = Blueprint('movimientos', __name__, description='Operaciones con movimientos')

#----------- CRUD Movimientos -----------#


@blp_movimientos.route("/movimientos")
class MovimientoResource(MethodView):
    @blp_movimientos.response(HTTPStatus.OK, PaginateMovimientoSchema)
    #@jwt_required()  # validacion del token
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

