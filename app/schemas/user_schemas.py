from marshmallow import fields, validate, post_load, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models import Usuario
from ..extensions import db


"""class UserSchema(SQLAlchemyAutoSchema):
    id_usuario = fields.Str(dump_only=True)
    nombre = fields.Str(required=True)
    email = fields.Str(required=True)
    password_hash = auto_field(required=True, validate=validate.Length(min=8, max=25), load_only=True)
    rol = fields.Str(required=True)
    fecha_registro = fields.DateTime(dump_only=True)
    ultimo_acceso = fields.DateTime(dump_only=True)
    status = fields.Bool(required=True)
    movimientos = fields.Str(required=True) 
"""


class UserSimpleSchema(Schema):
    class Meta:
        model = Usuario
        load_instance = True
        sqla_session = db.session
        schema_name = "UserSimpleSchema"

    id_usuario = fields.Str(dump_only=True)
    nombre = fields.Str()
    email = fields.Email()
    status = fields.Bool()
    rol = fields.Str()
    fecha_registro = fields.DateTime()
    ultimo_acceso = fields.DateTime()
    movimientos = fields.Str()

