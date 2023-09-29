import mysql.connector
from config import Config

class Canal:
    def __init__(self, id_canal, nombre_canal, descripcion_canal, imagen_canal, id_servidor, id_usuario):
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.descripcion_canal = descripcion_canal
        self.imagen_canal = imagen_canal
        self.id_servidor = id_servidor
        self.id_usuario = id_usuario

    @classmethod
    def crear_canal(cls, nombre_canal, descripcion_canal, imagen_canal, id_servidor, id_usuario):
        # Conecta a la base de datos
        connection = mysql.connector.connect(
            host=Config.DATABASE_HOST,
            user=Config.DATABASE_USERNAME,
            password=Config.DATABASE_PASSWORD,
            database=Config.DATABASE_NAME,
            port=Config.DATABASE_PORT,
        )

        # Crea un cursor
        cursor = connection.cursor()

        # Inserta un nuevo canal en la base de datos
        query = "INSERT INTO Canales (nombre_canal, descripcion_canal, imagen_canal, id_servidor, id_usuario) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nombre_canal, descripcion_canal, imagen_canal,id_servidor, id_usuario))

        # Realiza el commit y cierra el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def eliminar_canal(cls, id_canal):
        # Conecta a la base de datos
        connection = mysql.connector.connect(
            host=Config.DATABASE_HOST,
            user=Config.DATABASE_USERNAME,
            password=Config.DATABASE_PASSWORD,
            database=Config.DATABASE_NAME,
            port=Config.DATABASE_PORT,
        )

        # Crea un cursor
        cursor = connection.cursor()

        # Elimina un canal de la base de datos
        query = "DELETE FROM Canales WHERE id_canal = %s"
        cursor.execute(query, (id_canal,))

        # Realiza el commit y cierra el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def obtener_canales(cls, id_servidor):
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

        # Consulta los canales de un servidor por su ID
        query = "SELECT * FROM Canales WHERE id_servidor = %s"
        cursor.execute(query, (id_servidor,))
        canales = cursor.fetchall()

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()

        # Crea objetos Canal y devuelve una lista
        lista_canales = []
        for canal in canales:
            canal_obj = cls(
                canal["id_canal"],
                canal["nombre_canal"],
                canal["descripcion_canal"],
                canal["imagen_canal"],
                canal["id_servidor"],
                canal["id_usuario"]
            )
            lista_canales.append(canal_obj)

        return lista_canales