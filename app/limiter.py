from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import current_app


# # 1. Define la función que verifica la configuración.
# def get_dynamic_limits():
#     """Retorna límites normales o 0 si estamos en modo TESTING."""
#     # current_app solo se llama cuando esta función se ejecuta en contexto.
#     if current_app.config.get("testing", False):
#         return ["0 per day"] # Deshabilita límites
#     else:
#         return ["200 per day", "50 per hour"]
#
#
# # 2. Inicializa Limiter pasando la función como referencia.
# limiter = Limiter(
#     key_func=get_remote_address,
#     # Pasar la función sin parentesis (el callable)
#     default_limits=get_dynamic_limits
# )


# configurar rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    # default_limits=["200 per day", "50 per hour"]
    # if not current_app.config.get("testing")
    # else ["0 per day"]  # Deshabilitar límites en modo testing
    )

