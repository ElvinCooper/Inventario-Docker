from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import current_app


# configurar rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
    )

