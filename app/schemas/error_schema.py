from marshmallow import Schema, fields

# ---- schema para errores ----#
class ErrorSchema(Schema):
    success = fields.Boolean(load_default=False)
    message = fields.Str(required=True)

