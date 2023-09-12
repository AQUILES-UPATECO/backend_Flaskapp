from flask import Blueprint, request, jsonify
from app.models.mensaje import Mensaje

mensajes_bp = Blueprint('mensajes', __name__)

@mensajes_bp.route('/crear-mensaje', methods=['POST'])
def crear_mensaje():
    datos_mensaje = request.get_json()
    contenido_mensaje = datos_mensaje['contenido_mensaje']
    fecha_creacion = datos_mensaje['fecha_creacion']
    id_usuario = datos_mensaje['id_usuario']
    id_canal = datos_mensaje['id_canal']

    if contenido_mensaje and fecha_creacion and id_usuario and id_canal:
        Mensaje.crear_mensaje(contenido_mensaje, fecha_creacion, id_usuario, id_canal)
        return jsonify({'mensaje': 'Mensaje creado exitosamente'}), 201
    else:
        return jsonify({'error': 'Contenido de mensaje, fecha de creación, ID de usuario y ID de canal son obligatorios'}), 400

@mensajes_bp.route('/obtener-mensajes/<int:id_canal>', methods=['GET'])
def obtener_mensajes(id_canal):
    mensajes = Mensaje.obtener_mensajes_por_canal(id_canal)
    if mensajes:
        mensajes_json = [{'id_mensaje': mensaje.id_mensaje, 'contenido_mensaje': mensaje.contenido_mensaje,
                          'fecha_creacion': mensaje.fecha_creacion} for mensaje in mensajes]
        return jsonify({'mensajes': mensajes_json}), 200
    else:
        return jsonify({'error': 'No se encontraron mensajes para este canal'}), 404

@mensajes_bp.route('/eliminar-mensaje/<int:id_mensaje>', methods=['DELETE'])
def eliminar_mensaje(id_mensaje):
    mensaje = Mensaje.obtener_mensaje_por_id(id_mensaje)
    if mensaje:
        # Verificar si el usuario tiene permisos para eliminar el mensaje (agregar lógica de autenticación aquí)
        # Si el usuario tiene permisos, eliminar el mensaje
        Mensaje.eliminar_mensaje(id_mensaje)
        return jsonify({'mensaje': 'Mensaje eliminado exitosamente'}), 200
    else:
        return jsonify({'error': 'Mensaje no encontrado'}), 404