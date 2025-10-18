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
from ..models import Producto,  Usuario, Categoria
from ..schemas.categoria_schema import PaginateCategoriaSchema, CategoriaSchema
from ..schemas.error_schema import ErrorSchema
from ..schemas.movimientos_schema import PaginateMovimientoSchema, MovimientoSchema


blp_categorias = Blueprint('categorias', __name__, description='Operaciones con Categorias')

#----------- CRUD Categorias -----------#


@blp_categorias.route("/categorias")
class CategoriasResource(MethodView):
    @blp_categorias.response(HTTPStatus.OK, PaginateCategoriaSchema)
    #@jwt_required()  # validacion del token
    def get(self, page =1, per_page=10):
        """ Consultar todas las categorias """
        pagination = Categoria.query.paginate(
            page = page,
            per_page =per_page,
            error_out=False
        )

        return {
            "categorias": pagination.items,
            "total": pagination.total,
            "pages": pagination.pages,
            "current_page": pagination.page,
            "per_page": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
        }



#-----------  Categorias por su Id -----------#

@blp_categorias.route("/categoria/<string:id_categoria>")
class CategoriaIdResource(MethodView):
    @blp_categorias.response(HTTPStatus.OK, CategoriaSchema)
    @jwt_required()
    def get(self, id_categoria):
        """ Consultar las categoria por su ID"""
        categoria = Categoria.query.get_or_404(id_categoria)
        if not categoria :
            abort(HTTPStatus.NOT_FOUND, message="No existe una categoria con el Id proveeido")

        return categoria