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
from ..schemas.proveedor_schema import PaginateProveedorSchema, ProveedorSchema, ProveedorUpdateSchema

blp_proveedores = Blueprint('proveedores', __name__, description='Operaciones con Proveedores')



#--------- Listar todos los proveedores ----------#
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



#-------------- Consultar proveedores por su Id ---------------#
@blp_proveedores.route('/proveedores/<id_proveedor>')
class ProveedoresIdResource(MethodView):
    @blp_proveedores.response(HTTPStatus.OK, ProveedorSchema)
    @jwt_required()
    def get(self, id_proveedor):
        """ Consultar los proveedores por su id """

        proveedor = Proveedor.query.get_or_404(id_proveedor, description="Proveedor no existe")

        return proveedor


#------------- Crear un nuevo proveedor ------------------#

@blp_proveedores.route("/proveedor/create")
class CreateProveedorResource(MethodView):
    @blp_proveedores.arguments(ProveedorSchema)
    @blp_proveedores.response(HTTPStatus.CREATED, ProveedorSchema)
    @blp_proveedores.alt_response(HTTPStatus.INTERNAL_SERVER_ERROR, schema=ErrorSchema, description="Error interno del servidor", example={"succes": False, "message": "Error interno del servidor"})
    @jwt_required()

    def post(self, data_proveedor):
        """ Ingresar un nuevo proveedor en el sistema"""
        try:

            nuevo_proveedor = Proveedor(
                id_proveedor=str(uuid.uuid4()),
                nombre_proveedor=data_proveedor["nombre_proveedor"],
                contact =data_proveedor["contact"],
                telefono=data_proveedor["telefono"],
                email=data_proveedor["email"],
                direccion=data_proveedor["direccion"],
                fecha_registro=datetime.now(timezone.utc),
                status=data_proveedor["status"]

            )

            db.session.add(nuevo_proveedor)
            db.session.commit()

            return nuevo_proveedor, HTTPStatus.CREATED

        except ValidationError as e:
            abort(HTTPStatus.BAD_REQUEST, message=e.messages)

        except Exception as e:
            db.session.rollback()
            print(f"ERROR: {e}")
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=str(e))



# ------ Actualizar un proveedor existente ------#

@blp_proveedores.route("/proveedor/update/<string:id_proveedor>")
class ProveedorUpdateResource(MethodView):
    @blp_proveedores.arguments(ProveedorUpdateSchema)
    @blp_proveedores.response(HTTPStatus.OK, ProveedorSchema)
    @blp_proveedores.alt_response(HTTPStatus.NOT_FOUND, schema=ErrorSchema, description="Proveedor no encontrado", example={"success": False, "message": "No existe un proveedor con este Id"})
    @jwt_required()
    def put(self, update_data, id_proveedor ):
        """ Actualizar un proveedor por su ID """

        proveedor = db.session.get(Proveedor, id_proveedor)

        if not proveedor:
            abort(HTTPStatus.NOT_FOUND, message="No existe un proveedor con el Id proveeido")

        try:
            if update_data.get("nombre_proveedor"):
                proveedor.nombre_proveedor = update_data["nombre_proveedor"]
            if update_data.get("contact"):
                proveedor.contact = update_data["contact"]
            if update_data.get("telefono"):
                proveedor.telefono = update_data["telefono"]
            if update_data.get("email"):
                proveedor.email = update_data["email"]
            if update_data.get("direccion"):
                proveedor.direccion = update_data["direccion"]
            if "status" in update_data:
                proveedor.status = update_data["status"]


            db.session.commit()
            return proveedor

        except Exception as err:
            db.session.rollback()
            abort(HTTPStatus.BAD_REQUEST, message=f"Error al actualizar el proveedor: {str(err)}")



   # ---- Eliminar un proveedor existente  ----#

@blp_proveedores.route("/proveedor/delete/<string:id_proveedor>")
class ProveedorDeleteResource(MethodView):
    @blp_proveedores.response(HTTPStatus.NO_CONTENT)
    @jwt_required()
    def delete(self, id_proveedor):
        """ Eliminar un proveedor por su ID """
        proveedor = Proveedor.query.get_or_404(id_proveedor, description="Proveedor no encontrado")

        db.session.delete(proveedor)
        db.session.commit()
        return