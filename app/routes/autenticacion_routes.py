from flask import Blueprint, request, jsonify
from app .controllers.autenticacion import registrar_usuario, iniciar_sesion

autenticacion_routes = Blueprint('autenticacion_routes', __name__)

@autenticacion_routes.route('/registro', methods=['POST'])
def registro():
    return registrar_usuario()

@autenticacion_routes.route('/inicio-sesion', methods=['POST'])
def inicio_sesion():
    return iniciar_sesion()