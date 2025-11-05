
from . import models
from flask import Flask
import os

def create_app(config_name=None):
    app = Flask(__name__)

    if not config_name:
        config_name = os.getenv('CONFIG_CLASS', 'DevelopmentConfig')

    app.config.from_object(f"app.config.{config_name}")
