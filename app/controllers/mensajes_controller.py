from flask import jsonify
from app.models.mensajes import Mensaje

class MensajesController:

    @staticmethod
    def crear_mensaje(data):
        # Lógica para crear un mensaje, utilizando los datos en 'data'
        contenido_mensaje = data.get("contenido_mensaje")
        id_usuario = data.get("id_usuario")
        id_canal = data.get("id_canal")

        # Llama a la función en el modelo para crear un mensaje
        Mensaje.crear_mensaje(contenido_mensaje, id_usuario, id_canal)

        return jsonify({"message": "Mensaje creado con éxito"}), 201

    @staticmethod
    def eliminar_mensaje(id_mensaje):
        # Lógica para eliminar un mensaje
        Mensaje.eliminar_mensaje(id_mensaje)

        return jsonify({"message": "Mensaje eliminado con éxito"}), 200

    @staticmethod
    def obtener_mensajes_por_canal(id_canal):
        # Lógica para obtener mensajes por canal
        mensajes = Mensaje.obtener_mensajes_por_canal(id_canal)

        # Formatear la respuesta en formato JSON
        mensajes_json = [{"id_mensaje": mensaje.id_mensaje,
                          "contenido_mensaje": mensaje.contenido_mensaje,
                          "fecha_creacion": mensaje.fecha_creacion,
                          "id_usuario": mensaje.id_usuario,
                          "id_canal": mensaje.id_canal} for mensaje in mensajes]

        return jsonify(mensajes_json)
    