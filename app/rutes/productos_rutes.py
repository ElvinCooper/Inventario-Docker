import datetime
import uuid
from datetime import timezone, datetime
from flask_smorest import Blueprint, abort
from ..extensions import db
from http import HTTPStatus
#####from schemas.Error_schemas import ErrorSchema
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from ..models import Producto, Categoria, Movimientos, ProductoProveedor
from ..schemas.error_schema import ErrorSchema
from ..schemas.producto_schema import ProductoSchema, PaginationSchema, PaginateProductoSchema, ProductoUpdateSchema


productos_bp = Blueprint('productos', __name__, description='Operaciones con productos')


# ------ CRUD PRODUCTOS ------#


@productos_bp.route("/productos")
class ProductoResource(MethodView):
    @productos_bp.response(HTTPStatus.OK, PaginateProductoSchema)
    @jwt_required()
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



# ------ PRODUCTOS POR SU ID------#

@productos_bp.route("/productos/<string:id_producto>")
class ProductoResource(MethodView):
    @productos_bp.response(HTTPStatus.OK, ProductoSchema)
    @jwt_required()
    def get(self, id_producto):
        """ Consultar los productos por su ID"""
        producto = Producto.query.get_or_404(id_producto)
        if not producto :
            abort(HTTPStatus.NOT_FOUND, message="No existe un producto con el Id proveeido")

        return producto





# ------  CREACION DE PRODUCTOS  ------#

@productos_bp.route("/productos/create")
class CreateProductoResource(MethodView):
    @productos_bp.arguments(ProductoSchema)
    @productos_bp.response(HTTPStatus.CREATED, ProductoSchema)
    @productos_bp.alt_response(HTTPStatus.BAD_REQUEST, schema=ErrorSchema, description="Solicitud inválida", example={"success": False, "message": "Ya existe un producto con ese código de barras"})
    @productos_bp.alt_response(HTTPStatus.NOT_FOUND, schema=ErrorSchema, description="Categoría no encontrada", example={"success": False, "message": "No existe esta categoria"})
    @productos_bp.alt_response(HTTPStatus.INTERNAL_SERVER_ERROR, schema=ErrorSchema, description="Error interno del servidor", example={"succes": False, "message": "Error interno del servidor"})
    @jwt_required()

    def post(self, data_producto):
        """ Ingresar un nuevo producto en el sistema"""
        try:
            producto_existente = Producto.query.filter_by(codigo_barras=data_producto["codigo_barras"]).first()

            if producto_existente:
                abort(HTTPStatus.BAD_REQUEST, errors={"message": "Ya existe un producto con ese código de barras"})

            categoria = Categoria.query.filter_by(id_categoria=data_producto["id_categoria"]).first()
            if not categoria:
                abort(HTTPStatus.NOT_FOUND, errors={"message": "No existe esta categoria"})


            nuevo_producto = Producto(
                id_producto=str(uuid.uuid4()),
                nombre_producto=data_producto["nombre_producto"],
                descripcion=data_producto["descripcion"],
                imagen_url=data_producto["imagen_url"],
                codigo_barras=data_producto["codigo_barras"],
                precio=data_producto["precio"],
                stock_minimo=data_producto["stock_minimo"],
                stock_actual=data_producto["stock_actual"],
                id_categoria=data_producto["id_categoria"],
                fecha_creacion=datetime.now(timezone.utc),
                fecha_actualizacion=datetime.now(timezone.utc),
                status=data_producto["status"]
            )

            db.session.add(nuevo_producto)
            db.session.commit()

            return nuevo_producto, HTTPStatus.CREATED

        except ValidationError as e:
            abort(HTTPStatus.BAD_REQUEST, message=e.messages)

        except Exception as e:
            db.session.rollback()
            print(f"ERROR: {e}")
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=str(e))



   # ---- Eliminar un producto existente  ----#

@productos_bp.route("/productos/delete/<string:id_producto>")
class ProductoResource(MethodView):
    @productos_bp.response(HTTPStatus.OK, ProductoSchema)
    @jwt_required()
    def delete(self, id_producto):
        """ Eliminar un producto por su ID """
        producto = Producto.query.get_or_404(id_producto)
        if not producto:
            abort(HTTPStatus.NOT_FOUND, message="No existe un producto con el Id proveeido")

        try:
            db.session.delete(producto)
            db.session.commit()
            return {"success": True, "message": "Producto eliminado exitosamente"}, HTTPStatus.OK

        except Exception as err:
            db.session.rollback()
            abort(HTTPStatus.BAD_REQUEST, message=f"Error al eliminar el producto: {str(err)}")



# ------ Actualizar un producto existente ------#

@productos_bp.route("/productos/update/<string:id_producto>")
class ProductoResource(MethodView):
    @productos_bp.arguments(ProductoUpdateSchema)
    @productos_bp.response(HTTPStatus.OK, ProductoSchema)
    @productos_bp.alt_response(HTTPStatus.NOT_FOUND, schema=ErrorSchema, description="Producto no encontrado", example={"success": False, "message": "No existe un producto con este Id"})
    @jwt_required()
    def put(self, update_data, id_producto ):
        """ Actualizar un producto por su ID """
        #id_producto = Producto.query.get_or_404(id_producto)
        producto = db.session.get(Producto, id_producto)

        if not producto:
            abort(HTTPStatus.NOT_FOUND, message="No existe un producto con el Id proveeido")

        try:
            if update_data.get("nombre_producto"):
                producto.nombre_producto = update_data["nombre_producto"]
            if update_data.get("descripcion"):
                producto.descripcion = update_data["descripcion"]
            if update_data.get("precio"):
                producto.precio = update_data["precio"]
            if update_data.get("stock_minimo"):
                producto.stock_minimo = update_data["stock_minimo"]
            if update_data.get("stock_actual"):
                producto.stock_actual = update_data["stock_actual"]
            if update_data.get("imagen_url"):
                producto.imagen_url = update_data["imagen_url"]


            db.session.commit()
            return producto

        except Exception as err:
            db.session.rollback()
            abort(HTTPStatus.BAD_REQUEST, message=f"Error al actualizar el producto: {str(err)}")
