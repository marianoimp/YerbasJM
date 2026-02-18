from flask import Blueprint, request, jsonify
from db import conectarse_db

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/',methods=['GET'])
def obtener_productos():
    conn = conectarse_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(productos),200
