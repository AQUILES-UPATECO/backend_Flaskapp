from flask import  jsonify
from app.models.servidores import Servidor
from app.models.usuarios import Usuario


class ServidoresController:
  
    
    @staticmethod
    def obtener_servidores(id_usuario):
        """Funcion del controlador que obtiene los servidores por el id usuario"""
        
        servidores = Servidor.obtener_servidores(id_usuario)

        # Formatear la respuesta en formato JSON
        servidores_json = [{"id_servidor": servidor.id_servidor,
                            "nombre_servidor": servidor.nombre_servidor,
                            "descripcion_servidor": servidor.descripcion_servidor,
                            "id_usuario": servidor.id_usuario} for servidor in servidores]

        return jsonify(servidores_json)
    
    def obtener_todos_los_servidores():
        """Funcion del controlador que obtiene todos los servidores y los manda para
        ser visualizados en el main.html"""
        # Lógica para obtener todos los servidores de la base de datos
        todos_los_servidores = Servidor.obtener_todos_los_servidores()
        
        # Formatear la respuesta en formato JSON
        servidores_json = [{"id_servidor": servidor.id_servidor,
                            "nombre_servidor": servidor.nombre_servidor,
                            "descripcion_servidor": servidor.descripcion_servidor,
                            "id_usuario": servidor.id_usuario} for servidor in todos_los_servidores]

        return jsonify(servidores_json)
        
    @staticmethod
    def crear_servidor(data):
        """Funcion del controlador que crea un servidor con los datos recogidos
        del form en main.html"""
        # Utilizando los datos en 'data'
        nombre_servidor = data.get("nombre_servidor")
        descripcion_servidor = data.get("descripcion_servidor")
        id_usuario = data.get("id_usuario")
    
        # Establece el id_usuario_creador igual al id_usuario que inició sesión
        id_usuario_creador = id_usuario
    
        # Llama a la función en el modelo para crear un servidor con ambos valores
        Servidor.crear_servidor(nombre_servidor, descripcion_servidor, id_usuario, id_usuario_creador)
    
        return jsonify({"message": "Servidor creado con éxito"}), 201
    
    @staticmethod
    def suscribir_usuario_a_servidor(data):
        """Funcion del controlador para suuscribir a un usuario a un servidor"""
        try:
            # Extraer los datos del servidor y el usuario de 'data'
            id_usuario = data.get("id_usuario")
            id_servidor = data.get("id_servidor")          
            
            # Llamar al método suscribir_usuario de la clase Usuario
            Servidor.suscribir_usuario(id_usuario, id_servidor)

            # Si la suscripción se realiza con éxito, puedes devolver una respuesta JSON
            return jsonify({"message": "Usuario suscrito al servidor con éxito"}), 200
        except Exception as e:
            # Manejar cualquier excepción que ocurra, por ejemplo, si el usuario o servidor no existen
            return jsonify({"error": str(e)}), 500
        

    @staticmethod
    def eliminar_servidor(id_servidor):
        """Funcion del controlador que elimina un servidor
        con el id servidor"""
        # Lógica para eliminar un servidor
        Servidor.eliminar_servidor(id_servidor)
        
        return jsonify({"message": "Servidor eliminado con éxito"}), 200