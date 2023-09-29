from flask import Blueprint, request, jsonify
from app.controllers.mensajes_controller import MensajesController

mensajes_bp = Blueprint("mensajes", __name__)

@mensajes_bp.route("/mensajes/crear", methods=["POST"])
def crear_mensaje():
    data = request.json
    return MensajesController.crear_mensaje(data)

@mensajes_bp.route("/mensajes/eliminar/<int:id_mensaje>", methods=["DELETE"])
def eliminar_mensaje(id_mensaje):
    return MensajesController.eliminar_mensaje(id_mensaje)

@mensajes_bp.route("/mensajes/canal/<int:id_canal>", methods=["GET"])
def obtener_mensajes_por_canal(id_canal):
    return MensajesController.obtener_mensajes_por_canal(id_canal)