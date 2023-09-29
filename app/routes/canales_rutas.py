from flask import Blueprint, request, jsonify
from app.controllers.canales_controller import CanalesController

canales_bp = Blueprint("canales", __name__)

@canales_bp.route("/canales/<int:id_servidor>", methods=["GET"])
def obtener_canales(id_servidor):
    print(id_servidor)
    return CanalesController.obtener_canales(id_servidor)

@canales_bp.route("/canales/crear", methods=["POST"])
def crear_canal():
    data = request.json
    print(data)
    return CanalesController.crear_canal(data)

@canales_bp.route("/canales/eliminar/<int:id_canal>", methods=["DELETE"])
def eliminar_canal(id_canal):
    return CanalesController.eliminar_canal(id_canal)