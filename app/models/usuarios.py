import mysql.connector
from mysql.connector import Error


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
    def registrar_usuario(
        nombre_usuario, contrasena, correo_electronico, imagen_perfil
    ):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                database="chatapp",
                user="tu_usuario",
                password="tu_contraseña",
            )
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Usuarios (nombre_usuario, contrasena, correo_electronico, imagen_perfil) VALUES (%s, %s, %s, %s)",
                (nombre_usuario, contrasena, correo_electronico, imagen_perfil),
            )
            conn.commit()

        except Error as e:
            print(f"Error al registrar usuario: {e}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    # Agregar métodos para actualizar el perfil del usuario, cambiar la imagen, etc.
