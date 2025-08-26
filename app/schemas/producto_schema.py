from marshmallow import fields, validate, post_load, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models import Producto
from ..extensions import db



class ProductoSchema(Schema):
    id_producto = fields.Str(dump_only=True)
    nombre_producto = fields.Str(required=True)
    descripcion = fields.Str(required=True)
    codigo_barras = fields.Str(required=True)
    precio = fields.Decimal(as_string=True)
    stock_minimo = fields.Int(required=True)
    stock_actual = fields.Int(required=True)
    id_categoria = fields.Str(required=True)
    imagen_url = fields.Url(allow_none=True)
    fecha_creacion = fields.DateTime(dump_only=True)
    fecha_actualizacion = fields.DateTime(dump_only=True)
    status = fields.Bool()




