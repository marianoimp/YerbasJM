from flask import Flask
from flask_cors import CORS
from routes.productos import productos_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(productos_bp, url_prefix="/productos")

if __name__=="__main__":
    app.run(port=5053,debug=True)