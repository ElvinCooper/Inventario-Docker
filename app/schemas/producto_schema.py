from marshmallow import fields, validate, post_load, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models import Producto
from ..extensions import db



class ProductoSchema(Schema):
    id_producto = fields.Str(dump_only=True)
    nombre_producto = fields.Str(required=True)
    descripcion = fields.Str(required=True)
    codigo_barras = fields.Str(required=True)
    precio = fields.Decimal(as_string=True, required=True)
    stock_minimo = fields.Int(required=True)
    stock_actual = fields.Int(required=True)
    id_categoria = fields.Str(required=True)
    imagen_url = fields.Url(allow_none=True)
    fecha_creacion = fields.DateTime(dump_only=True)
    fecha_actualizacion = fields.DateTime(dump_only=True)
    status = fields.Bool(required=True)


# ---- Schema para validation ----#
class  PaginationSchema(Schema):
    page = fields.Int(load_default=1, validate=validate.Range(min=1))
    per_page = fields.Int(load_default=20, validate=validate.Range(min=1))



#---- Schema para respuestas paginada ----#
class PaginateProductoSchema(SQLAlchemyAutoSchema):
    productos = fields.Nested(ProductoSchema, many=True)
    total = fields.Int()
    pages = fields.Int()

    current_page = fields.Int()
    per_page = fields.Int()
    has_next = fields.Bool()
    has_prev = fields.Bool()



class ProductoUpdateSchema(Schema):
    class Meta:
        model = Producto
        load_instance = True
        sqla_session = db.session
        partial = True
        schema_name= "ProductoUpdateSchema"

    nombre_producto    = fields.Str(required=False)
    descripcion = fields.Str(required=False)
    precio   = fields.Str(required=False)
    stock_minimo = fields.Int(required=False)
    stock_actual = fields.Int(required=False)
    imagen_url = fields.Url(allow_none=True)




