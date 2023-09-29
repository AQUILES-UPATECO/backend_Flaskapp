import mysql.connector
from config import Config

class Mensaje:
    def __init__(self, id_mensaje, contenido_mensaje, fecha_creacion, id_usuario, id_canal):
        self.id_mensaje = id_mensaje
        self.contenido_mensaje = contenido_mensaje
        self.fecha_creacion = fecha_creacion
        self.id_usuario = id_usuario
        self.id_canal = id_canal

    @classmethod
    def crear_mensaje(cls, contenido_mensaje, id_usuario, id_canal):
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

        # Inserta un nuevo mensaje en la base de datos
        query = "INSERT INTO Mensajes (contenido_mensaje, id_usuario, id_canal) VALUES (%s, %s, %s)"
        cursor.execute(query, (contenido_mensaje, id_usuario, id_canal))

        # Realiza el commit y cierra el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def eliminar_mensaje(cls, id_mensaje):
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

        # Elimina un mensaje de la base de datos
        query = "DELETE FROM Mensajes WHERE id_mensaje = %s"
        cursor.execute(query, (id_mensaje,))

        # Realiza el commit y cierra el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def obtener_mensajes_por_canal(cls, id_canal):
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

        # Consulta los mensajes por canal
        query = "SELECT * FROM Mensajes WHERE id_canal = %s"
        cursor.execute(query, (id_canal,))
        mensajes = cursor.fetchall()

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()

        # Crea objetos Mensaje y devuelve una lista
        lista_mensajes = []
        for mensaje in mensajes:
            mensaje_obj = cls(
                mensaje["id_mensaje"],
                mensaje["contenido_mensaje"],
                mensaje["fecha_creacion"],
                mensaje["id_usuario"],
                mensaje["id_canal"]
            )
            lista_mensajes.append(mensaje_obj)

        return lista_mensajes