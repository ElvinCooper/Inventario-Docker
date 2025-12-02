from marshmallow import Schema, fields, validate


class RequestPasswordResetSchema(Schema):
    """Solicitar reset"""
    email = fields.Email(required=True)


class ResetPasswordSchema(Schema):
    """Confirmar reset"""
    new_password = fields.String(
        required=True,
        validate=validate.Length(min=8, max=25),
        load_only=True
    )


class PasswordResetResponseSchema(Schema):
    """Respuesta"""
    success = fields.Boolean()
    message = fields.String()