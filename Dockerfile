FROM python:3.12-slim

# Evitar .pyc y buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app


WORKDIR /app

COPY requirements.txt .


# Instalar dependencias del sistema necesarias.
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


# Instalar dependencias de Python.
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY . /app

# Puerto de la app
EXPOSE 8000

# Usar Gunicorn para servir Flask en producción
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.run:app"]

