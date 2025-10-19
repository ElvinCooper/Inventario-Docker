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
from ..schemas.categoria_schema import PaginateCategoriaSchema, CategoriaSchema, CategoriaUpdateSchema, SuccessResponseSchema
from ..schemas.error_schema import ErrorSchema

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


#------------- Crear una nueva categoria ------------------#

@blp_categorias.route("/categoria/create")
class CreateCategoriaResource(MethodView):
    @blp_categorias.arguments(CategoriaSchema)
    @blp_categorias.response(HTTPStatus.CREATED, CategoriaSchema)
    @blp_categorias.alt_response(HTTPStatus.INTERNAL_SERVER_ERROR, schema=ErrorSchema, description="Error interno del servidor", example={"succes": False, "message": "Error interno del servidor"})
    @jwt_required()

    def post(self, data_categoria):
        """ Ingresar una nueva categoria en el sistema"""
        try:

            nueva_categoria = Categoria(
                id_categoria=str(uuid.uuid4()),
                nombre_categoria=data_categoria["nombre_categoria"],
                descripcion_cat=data_categoria["descripcion_cat"],
                fecha_creacion=datetime.now(timezone.utc),
                status=data_categoria["status"]

            )

            db.session.add(nueva_categoria)
            db.session.commit()

            return nueva_categoria, HTTPStatus.CREATED

        except ValidationError as e:
            abort(HTTPStatus.BAD_REQUEST, message=e.messages)

        except Exception as e:
            db.session.rollback()
            print(f"ERROR: {e}  {data_categoria}")
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=str(e))




# ------ Actualizar una categoria existente ------#

@blp_categorias.route("/categoria/update/<string:id_categoria>")
class CategoriaUpdateResource(MethodView):
    @blp_categorias.arguments(CategoriaUpdateSchema)
    @blp_categorias.response(HTTPStatus.OK, CategoriaSchema)
    @blp_categorias.alt_response(HTTPStatus.NOT_FOUND, schema=ErrorSchema, description="Categoria no encontrada", example={"success": False, "message": "No existe una categoria con este Id"})
    def put(self, update_data, id_categoria ):
        """ Actualizar una categoria por su ID """
        #id_producto = Producto.query.get_or_404(id_producto)
        categoria = db.session.get(Categoria, id_categoria)

        if not categoria:
            abort(HTTPStatus.NOT_FOUND, message="No existe una categoria con el Id proveeido")

        try:
            if update_data.get("nombre_categoria"):
                categoria.nombre_categoria = update_data["nombre_categoria"]
            if update_data.get("descripcion_cat"):
                categoria.descripcion_cat = update_data["descripcion_cat"]


            db.session.commit()
            return categoria

        except Exception as err:
            db.session.rollback()
            abort(HTTPStatus.BAD_REQUEST, message=f"Error al actualizar la categoria: {str(err)}")



   # ---- Eliminar una categoria existente  ----#

@blp_categorias.route("/categoria/delete/<string:id_categoria>")
class CategoriaDeleteResource(MethodView):
    @blp_categorias.response(HTTPStatus.NO_CONTENT)
    def delete(self, id_categoria):
        """ Eliminar una categoria por su ID """
        categoria = Categoria.query.get_or_404(id_categoria)
        db.session.delete(categoria)
        db.session.commit()
        return

# @blp_categorias.route("/categoria/delete/<string:id_categoria>")
# class CategoriaDeleteResource(MethodView):
#     @blp_categorias.response(HTTPStatus.OK, SuccessResponseSchema)
#     def delete(self, id_categoria):
#         """ Eliminar una categoria por su ID """
#         categoria = Categoria.query.get_or_404(id_categoria)
#
#         # if not categoria:
#         #     abort(HTTPStatus.NOT_FOUND, message="No existe una categoria con el Id proveeido")
#
#         try:
#             db.session.delete(categoria)
#             db.session.commit()
#             return {
#                 "success": True,
#                 "message": f"Categoría '{categoria.nombre_categoria}' eliminada exitosamente"
#             }, HTTPStatus.OK
#
#         except Exception as err:
#             db.session.rollback()
#             abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=f"Error al eliminar la categoría: {str(err)}")