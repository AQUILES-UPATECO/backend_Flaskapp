import mysql.connector
from config import Config

class Servidor:
    def __init__(self, id_servidor, nombre_servidor, descripcion_servidor, id_usuario):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.descripcion_servidor = descripcion_servidor
        self.id_usuario = id_usuario


    
    @classmethod
    def crear_servidor(cls, nombre_servidor, descripcion_servidor, id_usuario, id_usuario_creador):
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

        # Inserta un nuevo servidor en la base de datos, incluyendo id_usuario_creador
        query = "INSERT INTO Servidores (nombre_servidor, descripcion_servidor, id_usuario, id_usuario_creador) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nombre_servidor, descripcion_servidor, id_usuario, id_usuario_creador))

        # Realiza el commit y cierra el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def eliminar_servidor(cls, id_servidor):
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

        # Elimina un servidor de la base de datos
        query = "DELETE FROM Servidores WHERE id_servidor = %s"
        cursor.execute(query, (id_servidor,))

        # Realiza el commit y cierra el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def obtener_servidores(cls, id_usuario):
        """Obtiene los servidores que un usuario creo y a los que se suscribió"""
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

        # Consulta los servidores que el usuario ha creado
        query_creados = "SELECT * FROM Servidores WHERE id_usuario = %s"
        cursor.execute(query_creados, (id_usuario,))
        servidores_creados = cursor.fetchall()

        # Consulta los servidores a los que el usuario se ha suscrito
        query_suscritos = """
            SELECT s.*
            FROM Servidores s
            JOIN Usuario_Servidor us ON s.id_servidor = us.Id_servidor
            WHERE us.Id_usuario = %s
        """
        cursor.execute(query_suscritos, (id_usuario,))
        servidores_suscritos = cursor.fetchall()

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()

        # Combina y crea objetos Servidor, luego devuelve una lista
        lista_servidores = []

        for servidor in servidores_creados:
            servidor_obj = cls(
                servidor["id_servidor"],
                servidor["nombre_servidor"],
                servidor["descripcion_servidor"],
                servidor["id_usuario"]
            )
            lista_servidores.append(servidor_obj)

        for servidor in servidores_suscritos:
            servidor_obj = cls(
                servidor["id_servidor"],
                servidor["nombre_servidor"],
                servidor["descripcion_servidor"],
                servidor["id_usuario"]
            )
            lista_servidores.append(servidor_obj)

        return lista_servidores
    
    @classmethod
    def obtener_todos_los_servidores(cls):
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

        # Consulta todos los servidores desde la base de datos
        query = "SELECT * FROM Servidores"
        cursor.execute(query)
        servidores = cursor.fetchall()

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()

        # Crea objetos Servidor y devuelve una lista
        lista_servidores = []
        for servidor in servidores:
            servidor_obj = cls(
                servidor["id_servidor"],
                servidor["nombre_servidor"],
                servidor["descripcion_servidor"],
                servidor["id_usuario"]
            )
            lista_servidores.append(servidor_obj)

        return lista_servidores
    
    @classmethod
    def suscribir_usuario(cls, id_servidor, id_usuario):
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

        # Inserta una nueva suscripción en la tabla Usuario_Servidor
        query = "INSERT INTO usuario_servidor (Id_servidor,Id_usuario) VALUES (%s, %s)"
        cursor.execute(query, (id_usuario, id_servidor))

        # Realiza el commit y cierra el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()


    @classmethod
    def obtener_servidor_por_id(cls, id_servidor):
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

        # Consulta un servidor por su ID
        query = "SELECT * FROM Servidores WHERE id_servidor = %s"
        cursor.execute(query, (id_servidor,))
        servidor = cursor.fetchone()

        # Cierra el cursor y la conexión
        cursor.close()
        connection.close()

        if servidor:
            return cls(
                servidor["id_servidor"],
            )
        else:
            return None