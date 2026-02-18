from flask import Blueprint, request, jsonify
from db import conectarse_db

usuarios_bp = Blueprint('usuarios', __name__)
