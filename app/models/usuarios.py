import mysql.connector
from mysql.connector import Error
from config import Config
import bcrypt
from flask_login import UserMixin
from flask_login import login_user


class Usuario:
    def __init__(
        self, id_usuario, nombre_usuario, contrasena, correo_electronico, imagen_perfil
    ):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.correo_electronico = correo_electronico
        self.imagen_perfil = imagen_perfil

    
    @staticmethod
    def registrar_usuario(nombre_usuario, contrasena, correo_electronico, imagen_perfil):
        try:
            # Genera un salt aleatorio para el hash
            salt = bcrypt.gensalt()
        
            # Genera el hash de la contraseña utilizando el salt
            hashed_password = bcrypt.hashpw(contrasena.encode("utf-8"), salt)
        
            conn = mysql.connector.connect(
                host=Config.DATABASE_HOST,
                user=Config.DATABASE_USERNAME,
                password=Config.DATABASE_PASSWORD,
                database=Config.DATABASE_NAME,
                port=Config.DATABASE_PORT,
            )
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Usuarios (nombre_usuario, contrasena, correo_electronico, imagen_perfil) VALUES (%s, %s, %s, %s)",
                (nombre_usuario, hashed_password, correo_electronico, imagen_perfil),
            )
            conn.commit()

        except Error as e:
            print(f"Error al registrar usuario: {e}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()  



    @staticmethod
    def iniciar_sesion(nombre_usuario, contrasena):
        try:
            conn = mysql.connector.connect(
                host=Config.DATABASE_HOST,
                user=Config.DATABASE_USERNAME,
                password=Config.DATABASE_PASSWORD,
                database=Config.DATABASE_NAME,
                port=Config.DATABASE_PORT,
            )
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM Usuarios WHERE nombre_usuario = %s", (nombre_usuario,)
            )
            usuario_data = cursor.fetchone()

            if usuario_data:
                (
                    id_usuario,
                    nombre_usuario,
                    hashed_password,
                    correo_electronico,
                    imagen_perfil,
                ) = usuario_data

                if bcrypt.checkpw(contrasena.encode("utf-8"), hashed_password.encode("utf-8")):
                    usuario = Usuario(
                        id_usuario,
                        nombre_usuario,
                        hashed_password,
                        correo_electronico,
                        imagen_perfil,
                    )
                    return usuario

            return None

        except Error as e:
            print(f"Error al autenticar usuario: {e}")
            return None

        finally:
            cursor.close()
            conn.close()

    
    @staticmethod
    def obtener_datos_de_usuario(nombre_usuario):
        try:
            # Establecer la conexión a la base de datos
            conn = mysql.connector.connect(
                host=Config.DATABASE_HOST,
                user=Config.DATABASE_USERNAME,
                password=Config.DATABASE_PASSWORD,
                database=Config.DATABASE_NAME,
                port=Config.DATABASE_PORT,
            )

            # Crear un cursor
            cursor = conn.cursor()

            # Consulta SQL para obtener los datos del usuario
            query = "SELECT id_usuario, nombre_usuario, imagen_perfil FROM usuarios WHERE nombre_usuario = %s"
            cursor.execute(query, (nombre_usuario,))

            # Obtener los resultados
            usuario = cursor.fetchone()

            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

            # Devolver los datos del usuario
            return usuario  # Esto devolverá una tupla (id_usuario, nombre_usuario, imagen_perfil)

        except Exception as e:
            print("Error al obtener datos del usuario:", e)
            return None
        
    @classmethod
    def obtener_usuario_por_id(cls, id_usuario):
        # Conecta a la base de datos
        connection = mysql.connector.connect(
            host=Config.DATABASE_HOST,
            user=Config.DATABASE_USERNAME,
            password=Config.DATABASE_PASSWORD,
            database=Config.DATABASE_NAME,
            port=Config.DATABASE_PORT,
        )

        # Crea un cursor
        cursor = connection.cursor(dictionary=True)

        # Consulta un usuario por su ID
        query = "SELECT * FROM Usuarios WHERE id_usuario = %s"
        cursor.execute(query, (id_usuario,))
        usuario = cursor.fetchone()

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()

        if usuario:
            # Devuelve una instancia de Usuario solo con el id_usuario
            return cls(id_usuario=usuario["id_usuario"])
        else:
            return None