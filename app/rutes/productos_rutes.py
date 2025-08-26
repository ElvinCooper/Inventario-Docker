from flask_smorest import Blueprint, abort
from ..extensions import db
from http import HTTPStatus
#####from schemas.Error_schemas import ErrorSchema
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from ..models import Producto, Categoria, Movimientos, ProductoProveedor
from ..schemas.producto_schema import ProductoSchema, PaginationSchema, PaginateProductoSchema


productos_bp = Blueprint('productos', __name__, description='Operaciones con productos')


# ------ CRUD PRODUCTOS ------#
@productos_bp.route("/productos")
class ProductoResource(MethodView):

    @productos_bp.arguments(PaginationSchema, location="query", as_kwargs=True)
    @productos_bp.response(HTTPStatus.OK, PaginateProductoSchema)
    #@jwt_required()  # validacion del token
    def get(self, page =1, per_page=10):
        """ Consultar todos los productos en el sistema"""
        pagination = Producto.query.paginate(
            page = page,
            per_page =per_page,
            error_out=False
        )

        return {
            "productos": pagination.items,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
        }












