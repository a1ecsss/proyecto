import mysql.connector
from db_connection import get_connection

class Cuenta:
    def __init__(self, total, usuario_id):
        self.total = total
        self.usuario_id = usuario_id

    def crear_cuenta(self):
        #Crea una nueva cuenta en la base de datos
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Cuenta (total, usuario_id) VALUES (%s, %s)"
        cursor.execute(query, (self.total, self.usuario_id))
        conn.commit()
        cuenta_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return cuenta_id

    def obtener_total(self, cuenta_id):
        #Obtiene el total de una cuenta
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT total FROM Cuenta WHERE id = %s"
        cursor.execute(query, (cuenta_id,))
        total = cursor.fetchone()
        cursor.close()
        conn.close()
        return total if total else 0.0
