import mysql.connector
from db_connection import get_connection

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def login(self, email, password):
        if not email or not password:
            return 0
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM Usuario WHERE correo = %s AND contraseña = %s"
            cursor.execute(query, (email, password))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            if result:
                self.id = result[0]
                self.nombre = result[1]
                self.correo = result[3]
                return 1
            else:
                return 0
        except Exception as e:
            return 0

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
