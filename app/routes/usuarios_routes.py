from flask import Blueprint, request, jsonify
from app.controllers.usuarios import obtener_perfil_usuario, editar_perfil_usuario, buscar_usuarios

usuarios_routes = Blueprint('usuarios_routes', __name__)

@usuarios_routes.route('/perfil/<int:id_usuario>', methods=['GET'])
def obtener_perfil(id_usuario):
    return obtener_perfil_usuario(id_usuario)

@usuarios_routes.route('/perfil/editar/<int:id_usuario>', methods=['PUT'])
def editar_perfil(id_usuario):
    return editar_perfil_usuario(id_usuario)

@usuarios_routes.route('/buscar', methods=['GET'])
def buscar():
    nombre_usuario = request.args.get('nombre_usuario')
    return buscar_usuarios(nombre_usuario)