import mysql.connector
from mysql.connector import Error
from config import Config  # Asegúrate de importar la configuración desde config.py
from app.models.usuarios import Usuario  # Asegúrate de importar la clase Usuario desde models.usuario

class InicioSesion:
    @staticmethod
    def autenticar_usuario(nombre_usuario, contrasena):
        try:
            conn = mysql.connector.connect(
                host=Config.DATABASE_HOST,
                user=Config.DATABASE_USERNAME,
                port=Config.DATABASE_PORT,
                password=Config.DATABASE_PASSWORD,
                database=Config.DATABASE_NAME  
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Usuarios WHERE nombre_usuario = %s AND contrasena = %s", (nombre_usuario, contrasena))
            usuario_data = cursor.fetchone()

            if usuario_data:
                # Supongo que la clase Usuario tiene un constructor que toma argumentos como id_usuario, nombre_usuario, etc.
                return Usuario(*usuario_data)

            return None

        except Error as e:
            print(f"Error al autenticar usuario: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()