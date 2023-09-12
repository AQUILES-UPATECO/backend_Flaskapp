from flask import Blueprint, request, jsonify
from app.models.servidor import Servidor

servidores_bp = Blueprint('servidores', __name__)

@servidores_bp.route('/crear-servidor', methods=['POST'])
def crear_servidor():
    # Obtener datos del formulario de creación de servidor
    datos_servidor = request.get_json()
    nombre_servidor = datos_servidor['nombre_servidor']
    descripcion_servidor = datos_servidor.get('descripcion_servidor', None)
    id_usuario = datos_servidor['id_usuario']

    # Validar datos y crear servidor
    if nombre_servidor and id_usuario:
        resultado = Servidor.crear_servidor(nombre_servidor, descripcion_servidor, id_usuario)
        if resultado:
            return jsonify({'mensaje': 'Servidor creado exitosamente'}), 201
        else:
            return jsonify({'error': 'No se pudo crear el servidor'}), 400
    else:
        return jsonify({'error': 'Nombre de servidor y ID de usuario son obligatorios'}), 400

@servidores_bp.route('/unirse-a-servidor', methods=['POST'])
def unirse_a_servidor():
    # Obtener datos de la solicitud
    datos_solicitud = request.get_json()
    id_servidor = datos_solicitud['id_servidor']
    id_usuario = datos_solicitud['id_usuario']

    # Validar datos y unirse al servidor
    if id_servidor and id_usuario:
        resultado = Servidor.unirse_a_servidor(id_servidor, id_usuario)
        if resultado:
            return jsonify({'mensaje': 'Te has unido al servidor exitosamente'}), 201
        else:
            return jsonify({'error': 'No se pudo unir al servidor'}), 400
    else:
        return jsonify({'error': 'ID de servidor y ID de usuario son obligatorios'}), 400

@servidores_bp.route('/servidores-por-usuario/<int:id_usuario>', methods=['GET'])
def obtener_servidores_por_usuario(id_usuario):
    # Obtener servidores por ID de usuario
    servidores = Servidor.obtener_servidores_por_usuario(id_usuario)
    if servidores:
        # Convertir resultados en un formato JSON adecuado
        resultados = [{'id_servidor': servidor.id_servidor, 'nombre_servidor': servidor.nombre_servidor} for servidor in servidores]
        return jsonify(resultados), 200
    else:
        return jsonify({'mensaje': 'No se encontraron servidores para este usuario'}), 404