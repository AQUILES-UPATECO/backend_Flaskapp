from flask import Blueprint, request, jsonify
from app.controllers.servidores import crear_servidor, unirse_a_servidor, obtener_servidores_por_usuario

servidores_routes = Blueprint('servidores_routes', __name__)

@servidores_routes.route('/crear-servidor', methods=['POST'])
def crear_servidor():
    return crear_servidor()

@servidores_routes.route('/unirse-a-servidor', methods=['POST'])
def unirse_a_servidor():
    return unirse_a_servidor()

@servidores_routes.route('/servidores/<int:id_usuario>', methods=['GET'])
def obtener_servidores_por_usuario(id_usuario):
    return obtener_servidores_por_usuario(id_usuario)


