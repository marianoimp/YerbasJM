from flask import Blueprint, request, jsonify
from db import conectarse_db

carrito_bp = Blueprint('carrito', __name__)


