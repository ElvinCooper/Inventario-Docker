import os
from flask import jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# 1. Definición del objeto Limiter.
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# 2. Función para configurar e inicializar Limiter en el App Factory
def init_limiter(app):
    """
    Configura el Limiter con la URI de almacenamiento y lo adjunta a la aplicación.
    Debe llamarse después de cargar las variables de entorno.
    """
    # ----------------------------------------------------
    # LECTURA Y VALIDACIÓN DE LA CONFIGURACIÓN DE REDIS
    # ----------------------------------------------------
    
    REDIS_URL = os.environ.get("RATELIMIT_STORAGE_URL")
    env = os.environ.get("FLASK_ENV", "development").lower()
    
    # 3. Validar si estamos en producción y falta la URL
    if env == "production" and not REDIS_URL:
        raise EnvironmentError(
            "FATAL: RATELIMIT_STORAGE_URL no está configurada. "
            "Es obligatoria para el Rate Limiter en producción (Render)."
        )
    
    # 4. Establecer la URI de almacenamiento
    if REDIS_URL:
        # Usar la URL de Upstash Redis
        STORAGE_URI = REDIS_URL
        print(f"[INFO] Limiter usará Redis como almacenamiento.")
    else:
        # Usar el modo en memoria para desarrollo local
        STORAGE_URI = "memory://"
        print("[ADVERTENCIA] Usando Rate Limiting en memoria (solo para desarrollo/testing).")

    # 5. Inicializar Limiter con el storage_uri determinado
    limiter.storage_uri = STORAGE_URI
    limiter.init_app(app)

    # 6. Manejador de errores para la respuesta 429
    @app.errorhandler(429)
    def ratelimit_handler(e):
        return jsonify({
            "error": "Límite de Solicitudes Excedido",
            "message": "Ha enviado demasiadas solicitudes. Intente nuevamente más tarde."
        }), 429

