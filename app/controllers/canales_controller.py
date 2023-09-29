from flask import jsonify, request
from app.models.canales import Canal

class CanalesController:

    @staticmethod
    def obtener_canales(id_servidor):
        """Funcion del controlador que obtiene los canales de la base de datos
        con el id del servidor"""
        canales = Canal.obtener_canales(id_servidor)

        # Formatear la respuesta en formato JSON
        canales_json = [{"id_canal": canal.id_canal,
                         "nombre_canal": canal.nombre_canal,
                         "descripcion_canal": canal.descripcion_canal,
                         "id_servidor": canal.id_servidor,
                         "id_usuario": canal.id_usuario} for canal in canales]

        return jsonify(canales_json)

    @staticmethod
    def crear_canal(data):
        """Funcion del controlador que crea un canal tomando los datos extraidos
         del form que se encuentra en main.html"""
        try:
            # Lógica para crear un canal, utilizando los datos en 'data'
            nombre_canal = data.get("nombre_canal")
            descripcion_canal = data.get("descripcion_canal")
            imagen_canal=None
            id_servidor = data.get("id_servidor")
            id_usuario = data.get("id_usuario")
            
            # Llama a la función en el modelo para crear un canal con los valores proporcionados
            Canal.crear_canal(nombre_canal, descripcion_canal,imagen_canal, id_servidor, id_usuario)

            return jsonify({"message": "Canal creado con éxito"}), 201
        except Exception as e:
            # Manejar cualquier excepción que ocurra, por ejemplo, si el servidor no existe
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def eliminar_canal(id_canal):
        """Funcion del controlador que elimina un canal con el id de canal"""
        try:
            # Lógica para eliminar un canal
            Canal.eliminar_canal(id_canal)

            return jsonify({"message": "Canal eliminado con éxito"}), 200
        except Exception as e:
            # Manejar cualquier excepción que ocurra, por ejemplo, si el canal no existe
            return jsonify({"error": str(e)}), 500

   