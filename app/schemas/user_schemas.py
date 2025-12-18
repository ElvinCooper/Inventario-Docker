from marshmallow import fields, validate, post_load, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models import Usuario
from ..extensions import db


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        sqla_session = db.session
        include_fk = True
        include_relationships = True

    id_usuario = fields.Str(dump_only=True)
    nombre = fields.Str(required=True)
    email = fields.Str(required=True)
    password_hash = auto_field(required=True, validate=validate.Length(min=8, max=25), load_only=True)
    rol = fields.Str(required=True)
    fecha_registro = fields.DateTime(dump_only=True)
    ultimo_acceso = fields.DateTime(dump_only=True)
    status = fields.Bool(required=True)
    movimientos = fields.List(fields.Str(), dump_only=True)

# ------------------------  Schema para registrar un usuario ---------------------------------#
class UserRegisterSchema(Schema):

    nombre = fields.String(required=True, validate=validate.Length(min=1, max=60))
    email = fields.Email(required=True)
    password_hash = fields.String(required=True, validate=validate.Length(min=8, max=25), load_only=True)
    telefono = fields.String(validate=validate.Length(max=15), allow_none=True)
    rol = fields.Str(required=True)
    status = fields.Bool(required=True)

#------------------------- Schema para respuesta al registrar usuario --------------------------#
class UserResponseSchema(Schema):
    id_usuario = fields.String()
    nombre = fields.String()
    email = fields.Email()
    telefono = fields.String(allow_none=True)
    rol = fields.String()
    ultimo_acceso = fields.DateTime()
    fecha_registro = fields.DateTime(allow_none=True)
    status = fields.Bool()




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




class LoginSchema(Schema):
    email = fields.Email(required=True)
    password_hash = fields.String(required=True, validate=validate.Length(min=1))
    schema_name = "UserLoginSchema"



class LoginResponseSchema(Schema):
    class Meta:
        model = Usuario
        load_instance = True
        include_relationships = False  # No incluir relaciones en actualización
        sqla_session = db.session
        partial = True  # Para actualizaciones parciales
        schema_name = "LoginSchema"

    access_token = fields.String()
    refresh_token = fields.String(required=False)
    usuario = fields.Nested(UserSchema, only=('id_usuario', 'nombre', 'email', 'rol'))
    message = fields.String()




# --------------------- Schema para la respuesta del Logout ---------------------------------------#
class LogoutResponseSchema(Schema):
    class Meta:
        model = Usuario
        load_instance = True
        include_relationships = False  # No incluir relaciones en actualización
        sqla_session = db.session
        partial = True  # Para actualizaciones parciales
        schema_name = "UserLogoutSchema"

    mensaje = fields.String()


# --------------------- Schema para la respuesta del refresh token ---------------------------------------#
class TokenRefreshResponseSchema(Schema):
    class Meta:
            model = Usuario
            load_instance = True
            include_relationships = False  # No incluir relaciones en actualización
            sqla_session = db.session
            partial = True  # Para actualizaciones parciales
            schema_name = "TokenRefreshSchema"

    acces_token = fields.String(required=True)
    refresh_token = fields.String(required=True)


# ---- schema para errores ----#
class UserErrorSchema(Schema):
    success = fields.Boolean(load_default=False)
    message = fields.Str(required=True)