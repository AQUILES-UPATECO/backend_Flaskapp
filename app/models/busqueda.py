import mysql.connector
from mysql.connector import Error

class Busqueda:
    @staticmethod
    def buscar_servidores_por_nombre(nombre_servidor):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='chatapp',
                user='tu_usuario',
                password='tu_contraseña'
            )
            cursor = conn.cursor()
            cursor.execute("SELECT nombre_servidor, descripcion_servidor, COUNT(id_usuario) as cantidad_usuarios FROM Servidores WHERE nombre_servidor LIKE %s GROUP BY nombre_servidor, descripcion_servidor",
                           ('%' + nombre_servidor + '%',))
            resultados = cursor.fetchall()

            servidores_encontrados = []
            for resultado in resultados:
                servidores_encontrados.append({
                    'nombre_servidor': resultado[0],
                    'descripcion_servidor': resultado[1],
                    'cantidad_usuarios': resultado[2]
                })

            return servidores_encontrados

        except Error as e:
            print(f"Error al buscar servidores: {e}")
            return []

        finally:
            cursor.close()
            conn.close()