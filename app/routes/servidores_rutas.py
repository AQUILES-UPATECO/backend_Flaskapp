from flask import Blueprint, request, jsonify
from app.controllers.servidores_controller import ServidoresController

servidores_bp = Blueprint("servidores", __name__)


@servidores_bp.route("/servidores/<int:id_usuario>", methods=["GET"])
def obtener_servidores(id_usuario):
    return ServidoresController.obtener_servidores(id_usuario)

@servidores_bp.route("/servidores/todos", methods=["GET"])
def obtener_todos_los_servidores():
    return ServidoresController.obtener_todos_los_servidores()



@servidores_bp.route("/servidores/crear", methods=["POST"])
def crear_servidor():
    data = request.json
    return ServidoresController.crear_servidor(data)

@servidores_bp.route("/servidores/suscribir/<int:id_usuario>/<int:id_servidor>", methods=["POST"])
def suscribir_usuario_a_servidor(id_usuario, id_servidor):
    data = request.json
    data["id_usuario"] = id_usuario
    data["id_servidor"] = id_servidor
    print(data)
    return ServidoresController.suscribir_usuario_a_servidor(data)

@servidores_bp.route("/servidores/eliminar/<int:id_servidor>", methods=["DELETE"])
def eliminar_servidor(id_servidor):
    return ServidoresController.eliminar_servidor(id_servidor)