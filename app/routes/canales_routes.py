from flask import Blueprint, request, jsonify
from app.controllers.canales import crear_canal, obtener_canales_por_servidor, eliminar_canal

canales_routes = Blueprint('canales_routes', __name__)

@canales_routes.route('/crear-canal', methods=['POST'])
def crear_canal():
    return crear_canal()

@canales_routes.route('/canales/<int:id_servidor>', methods=['GET'])
def obtener_canales_por_servidor(id_servidor):
    return obtener_canales_por_servidor(id_servidor)

@canales_routes.route('/eliminar-canal/<int:id_canal>', methods=['DELETE'])
def eliminar_canal(id_canal):
    return eliminar_canal(id_canal)