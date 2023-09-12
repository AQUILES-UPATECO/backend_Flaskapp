import mysql.connector
from mysql.connector import Error

class Mensaje:
    def __init__(self, id_mensaje, contenido_mensaje, fecha_creacion, id_usuario, id_canal):
        self.id_mensaje = id_mensaje
        self.contenido_mensaje = contenido_mensaje
        self.fecha_creacion = fecha_creacion
        self.id_usuario = id_usuario
        self.id_canal = id_canal

    @staticmethod
    def crear_mensaje(contenido_mensaje, fecha_creacion, id_usuario, id_canal):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='chatapp',
                user='tu_usuario',
                password='tu_contraseña'
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Mensajes (contenido_mensaje, fecha_creacion, id_usuario, id_canal) VALUES (%s, %s, %s, %s)",
                           (contenido_mensaje, fecha_creacion, id_usuario, id_canal))
            conn.commit()

        except Error as e:
            print(f"Error al crear mensaje: {e}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    # Agregar métodos para modificar y eliminar mensajes, obtener mensajes por canal, etc.