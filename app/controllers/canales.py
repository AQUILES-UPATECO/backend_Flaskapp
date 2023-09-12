from flask import Blueprint, request, jsonify
from app.models.canal import Canal  # Asegúrate de que la importación sea correcta

canales_bp = Blueprint('canales', __name__)

@canales_bp.route('/crear-canal', methods=['POST'])
def crear_canal():
    # Obtener datos del formulario de creación de canal
    datos_canal = request.get_json()
    nombre_canal = datos_canal['nombre_canal']
    descripcion_canal = datos_canal.get('descripcion_canal', None)
    imagen_canal = datos_canal.get('imagen_canal', None)
    id_servidor = datos_canal['id_servidor']
    id_usuario = datos_canal['id_usuario']

    # Validar datos y crear canal
    if nombre_canal and id_servidor and id_usuario:
        Canal.crear_canal(nombre_canal, descripcion_canal, imagen_canal, id_servidor, id_usuario)
        return jsonify({'mensaje': 'Canal creado exitosamente'}), 201
    else:
        return jsonify({'error': 'Nombre de canal, ID de servidor y ID de usuario son obligatorios'}), 400
    

@canales_bp.route('/obtener-canales/<int:id_servidor>', methods=['GET'])
def obtener_canales_por_servidor(id_servidor):
    canales = Canal.obtener_canales_por_servidor(id_servidor)
    return jsonify({'canales': canales})


@canales_bp.route('/eliminar-canal/<int:id_canal>', methods=['DELETE'])
def eliminar_canal(id_canal):
    if Canal.eliminar_canal(id_canal):
        return jsonify({'mensaje': 'Canal eliminado exitosamente'}), 200
    else:
        return jsonify({'error': 'No se pudo eliminar el canal'}), 400