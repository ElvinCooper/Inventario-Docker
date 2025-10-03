from marshmallow import fields, validate, post_load, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models import Producto, Movimientos, Usuario
from ..extensions import db



class MovimientoSchema(Schema):
    id_movimiento = fields.Str(dump_only=True)
    id_productos  = fields.Str(required=True)
    id_usuario    = fields.Str(required=True)
    tipo_movimiento = fields.Str(required=True)
    cantidad = fields.Int(as_string=True, required=True)
    precio_unitario = fields.Decimal(as_string=True, required=True)
    motivo = fields.Str(required=True)
    referencia = fields.Url(allow_none=True)
    fecha_movimiento = fields.DateTime(dump_only=True)
    observaciones = fields.Str(allow_none=True)


#---- Schema para respuestas paginada ----#
class PaginateMovimientoSchema(SQLAlchemyAutoSchema):
    movimientos = fields.Nested(MovimientoSchema, many=True)
    total = fields.Int()
    pages = fields.Int()

    current_page = fields.Int()
    per_page = fields.Int()
    has_next = fields.Bool()
    has_prev = fields.Bool()