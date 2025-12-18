from marshmallow import fields, validate, post_load, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema



class MovimientoSchema(Schema):
    id_movimiento = fields.Str(dump_only=True)
    id_producto  = fields.Str(required=True)
    tipo_movimiento = fields.Str(required=True)
    cantidad = fields.Int(as_string=True, required=True)
    precio_unitario = fields.Decimal(as_string=True, required=True)
    motivo = fields.Str(required=True)
    referencia = fields.Str(allow_none=True)
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



# ---- schema para errores ----#
class MovimientoErrorSchema(Schema):
    success = fields.Boolean(load_default=False)
    message = fields.Str(required=True)