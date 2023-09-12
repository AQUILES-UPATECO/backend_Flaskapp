from flask import Blueprint, request, jsonify
from app.controllers.mensajes import crear_mensaje, obtener_mensajes, eliminar_mensaje

mensajes_routes = Blueprint('mensajes_routes', __name__)

@mensajes_routes.route('/crear-mensaje', methods=['POST'])
def crear_mensaje():
    return crear_mensaje()

@mensajes_routes.route('/mensajes/<int:id_canal>', methods=['GET'])
def obtener_mensajes(id_canal):
    return obtener_mensajes(id_canal)

@mensajes_routes.route('/eliminar-mensaje/<int:id_mensaje>', methods=['DELETE'])
def eliminar_mensaje(id_mensaje):
    return eliminar_mensaje(id_mensaje)