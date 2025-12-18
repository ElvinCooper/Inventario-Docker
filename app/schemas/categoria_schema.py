from marshmallow import fields, validate, post_load, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models import Producto, Movimientos, Usuario, Categoria
from ..extensions import db



class CategoriaSchema(Schema):
    id_categoria = fields.Str(dump_only=True)
    nombre_categoria = fields.Str(required=True)
    descripcion_cat = fields.Str(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)
    status = fields.Bool(required=True)


#---- Schema para respuestas paginada ----#
class PaginateCategoriaSchema(SQLAlchemyAutoSchema):
    categorias = fields.Nested(CategoriaSchema, many=True)
    total = fields.Int()
    pages = fields.Int()

    current_page = fields.Int()
    per_page = fields.Int()
    has_next = fields.Bool()
    has_prev = fields.Bool()


class CategoriaUpdateSchema(Schema):
    class Meta:
        model = Categoria
        load_instance = True
        sqla_session = db.session
        partial = True
        schema_name= "CategoriaUpdateSchema"

    nombre_categoria    = fields.Str(required=False)
    descripcion_cat = fields.Str(required=False)


class SuccessResponseSchema(Schema):
    success = fields.Bool()
    message = fields.Str()


# ---- schema para errores ----#
class CategoriaErrorSchema(Schema):
    success = fields.Boolean(load_default=False)
    message = fields.Str(required=True)