from marshmallow import fields, validate, post_load, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models import Proveedor
from ..extensions import db



class ProveedorSchema(Schema):
    id_proveedor = fields.Str(dump_only=True)
    nombre_proveedor = fields.Str(required=True)
    contact = fields.Str(required=True)
    telefono = fields.Str(required=True)
    email = fields.Str(required=True)
    direccion = fields.Str(required=True)
    fecha_registro = fields.DateTime(dump_only=True)
    status = fields.Boolean(required=True)


#---- Schema para respuestas paginada ----#
class PaginateProveedorSchema(SQLAlchemyAutoSchema):
    proveedores = fields.Nested(ProveedorSchema, many=True)
    total = fields.Int()
    pages = fields.Int()

    current_page = fields.Int()
    per_page = fields.Int()
    has_next = fields.Bool()
    has_prev = fields.Bool()




class ProveedorUpdateSchema(Schema):
    class Meta:
        model = Proveedor
        load_instance = True
        sqla_session = db.session
        partial = True
        schema_name= "ProveedorUpdateSchema"

    nombre_proveedor    = fields.Str(required=False)
    contact = fields.Str(required=False)
    telefono = fields.Str(required=False)
    email = fields.Str(required=False)
    direccion = fields.Str(required=False)
    status = fields.Bool(required=False)
