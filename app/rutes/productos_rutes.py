from flask_smorest import Blueprint, abort
from ..extensions import db
from http import HTTPStatus
#####from schemas.Error_schemas import ErrorSchema
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from ..models import Producto, Categoria, Movimientos, ProductoProveedor
from ..schemas.producto_schema import ProductoSchema


productos_bp = Blueprint('productos', __name__, description='Operaciones con productos')


# ------ CRUD PRODUCTOS ------#
@productos_bp.route("/productos")
class ProductoResource(MethodView):

    @productos_bp.response(HTTPStatus.OK, ProductoSchema(many=True))
    #@jwt_required()
    def get(self):
        """ Consultar todos los productos en el sistema"""
        pais = Producto.query.all()
        return pais












