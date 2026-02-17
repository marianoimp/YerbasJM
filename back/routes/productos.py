from flask import Blueprint, request, jsonify
from db import conectarse_db

productos_bp = Blueprint("productos", __name__)

@productos_bp.route("/",methods=["GET"])
def obtener_productos():