from flask import Blueprint, request, jsonify
from db import conectarse_db

categorias_bp = Blueprint('categorias',__name__)

@categorias_bp.route('/', methods=['GET'])
def obtener_categorias():
    conn = conectarse_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM categorias')
    categorias = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(categorias),200

@categorias_bp.route('/<int:id_usuario/categorias',methods=['POST'])
def agregar_categorias(id_usuario):
    conn = conectarse_db()
    cursor = conn.cursor(dictionary=True)

    data = request.json()
    id_producto = data.get("id_producto")
    