import mysql.connector
from mysql.connector import Error

class Canal:
    def __init__(self, id_canal, nombre_canal, descripcion_canal, imagen_canal, id_servidor, id_usuario):
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.descripcion_canal = descripcion_canal
        self.imagen_canal = imagen_canal
        self.id_servidor = id_servidor
        self.id_usuario = id_usuario

    @staticmethod
    def crear_canal(nombre_canal, descripcion_canal, imagen_canal, id_servidor, id_usuario):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='chatapp',
                user='tu_usuario',
                password='tu_contraseña'
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Canales (nombre_canal, descripcion_canal, imagen_canal, id_servidor, id_usuario) VALUES (%s, %s, %s, %s, %s)",
                           (nombre_canal, descripcion_canal, imagen_canal, id_servidor, id_usuario))
            conn.commit()

        except Error as e:
            print(f"Error al crear canal: {e}")
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    # Agregar métodos para obtener canales por servidor, administrar mensajes, etc.