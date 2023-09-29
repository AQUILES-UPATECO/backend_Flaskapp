from flask import Blueprint
from app.controllers.usuarios_controller import (
    registrar_usuario,
    iniciar_sesion, )

# Se crea un Blueprint para las rutas de usuarios
usuarios_bp = Blueprint("usuarios", __name__)


# Se Definen las rutas asociadas a las funciones del controlador utilizando el decorador
@usuarios_bp.route("/usuarios/registrar", methods=["POST"])
def registrar():
    return registrar_usuario()


@usuarios_bp.route("/usuarios/iniciar_sesion", methods=["POST"])
def iniciar_sesion_route():
    return iniciar_sesion()
