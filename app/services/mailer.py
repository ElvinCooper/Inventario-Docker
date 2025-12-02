"""
Servicio simple para envío de emails
"""
from flask import current_app
from flask_mail import Message
from ..extensions import mail


def send_email(subject, recipient, body):
    """
    Enviar email simple

    Args:
        subject: Asunto
        recipient: Email destino
        body: Contenido del mensaje
    """
    try:
        msg = Message(
            subject=subject,
            recipients=[recipient],
            body=body,
            sender=current_app.config['MAIL_DEFAULT_SENDER']
        )

        mail.send(msg)
        current_app.logger.info(f"Email enviado a: {recipient}")
        return True

    except Exception as e:
        current_app.logger.error(f"Error enviando email: {str(e)}")
        return False


def send_welcome_email(email, nombre):
    """Email de bienvenida al registrarse"""
    subject = "Bienvenido a Inventory API"
    body = f"""
Hola {nombre},

¡Gracias por registrarte en Inventory API!

Tu cuenta ha sido creada exitosamente.

Saludos,
El equipo de Inventory API
    """
    return send_email(subject, email, body)


def send_password_reset_email(email, nombre, token):
    """Email para resetear contraseña"""
    reset_url = f"{current_app.config['FRONTEND_URL']}/reset-password?token={token}"

    subject = "Recuperación de contraseña"
    body = f"""
Hola {nombre},

Para restablecer tu contraseña, haz clic en el siguiente enlace:

{reset_url}

Este enlace es válido por 1 hora.

Si no solicitaste esto, ignora este mensaje.

Saludos,
El equipo de Inventory API
    """
    return send_email(subject, email, body)