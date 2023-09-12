import mysql.connector
from mysql.connector import Error

class Servidor:
    def __init__(self, id_servidor, nombre_servidor, descripcion_servidor, id_usuario):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.descripcion_servidor = descripcion_servidor
        self.id_usuario = id_usuario

    @staticmethod
    def crear_servidor(nombre_servidor, descripcion_servidor, id_usuario):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='chatapp',
                user='tu_usuario',
                password='tu_contraseña'
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Servidores (nombre_servidor, descripcion_servidor, id_usuario) VALUES (%s, %s, %s)",
                           (nombre_servidor, descripcion_servidor, id_usuario))
            conn.commit()

        except Error as e:
            print(f"Error al crear servidor: {e}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

   