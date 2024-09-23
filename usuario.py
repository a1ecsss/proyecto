import mysql.connector
from db_connection import get_connection

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def crear_usuario(self):
        #Crea un nuevo usuario en la base de datos
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Usuario (nombre) VALUES (%s)"
        cursor.execute(query, (self.nombre,))
        conn.commit()
        user_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return user_id

    def obtener_historial(self, usuario_id):
        #Retorna el historial de pagos de un usuario dado su ID
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT historialPagos FROM Usuario WHERE id = %s"
        cursor.execute(query, (usuario_id,))
        historial = cursor.fetchone()
        cursor.close()
        conn.close()
        return historial if historial else []
