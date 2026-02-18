from flask import Flask
from flask_cors import CORS
from routes.productos import productos_bp
from routes.categorias import categorias_bp
from routes.carrito import carrito_bp
from routes.usuarios import usuarios_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(productos_bp, url_prefix="/productos")
app.register_blueprint(categorias_bp, url_prefix="/categorias")
app.register_blueprint(carrito_bp, url_prefix="/carrito")
app.register_blueprint(usuarios_bp, url_prefix="/usuarios")


if __name__=="__main__":
    app.run(port=5053,debug=True)