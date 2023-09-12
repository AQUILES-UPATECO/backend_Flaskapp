from flask import Blueprint, request, jsonify
from app.models.inicio_sesion import InicioSesion, Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['POST'])
def registrar_usuario():
    # Obtener datos del formulario de registro
    datos_registro = request.get_json()
    nombre_usuario = datos_registro['nombre_usuario']
    contrasena = datos_registro['contrasena']
    correo_electronico = datos_registro['correo_electronico']
    imagen_perfil = datos_registro.get('imagen_perfil', None)

    # Validar datos y registrar usuario
    if nombre_usuario and contrasena:
        Usuario.registrar_usuario(nombre_usuario, contrasena, correo_electronico, imagen_perfil)
        return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 201
    else:
        return jsonify({'error': 'Nombre de usuario y contraseña son obligatorios'}), 400

@auth_bp.route('/inicio-sesion', methods=['POST'])
def iniciar_sesion():
    # Obtener datos del formulario de inicio de sesión
    datos_inicio_sesion = request.get_json()
    nombre_usuario = datos_inicio_sesion['nombre_usuario']
    contrasena = datos_inicio_sesion['contrasena']

    # Autenticar usuario
    usuario = InicioSesion.autenticar_usuario(nombre_usuario, contrasena)

    if usuario:
        # Crear sesión de usuario (por ejemplo, usar Flask-Login)
        # Devolver detalles del usuario autenticado
        return jsonify({'mensaje': 'Inicio de sesión exitoso', 'usuario': {
            'nombre_usuario': usuario.nombre_usuario,
            'correo_electronico': usuario.correo_electronico,
            'imagen_perfil': usuario.imagen_perfil
        }}), 200
    else:
        return jsonify({'error': 'Nombre de usuario o contraseña incorrectos'}), 401