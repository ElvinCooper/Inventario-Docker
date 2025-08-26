import os
from flask import Flask
from .extensions import init_extensions
from dotenv import load_dotenv
from .models import Producto
from flask import jsonify



def create_app():
    app = Flask(__name__)
    load_dotenv()

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar extensiones
    init_extensions(app)


    @app.get('/')
    def home():
        return '<h1> Hello World ! </h1>'

    @app.get('/productos')
    def productos():
        mis_productos = Producto.query.all()
        return jsonify({
            'productos': [p.to_dict() for p in mis_productos]
        })

    return app




if __name__ == '__main__':
    create_app().run(host="0.0.0.0", port=8000, debug=True)
