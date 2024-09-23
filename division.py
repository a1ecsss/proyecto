import mysql.connector
from db_connection import get_connection

class Division:
    def __init__(self, cuenta_id, usuario_id, item, monto):
        self.cuenta_id = cuenta_id
        self.usuario_id = usuario_id
        self.item = item
        self.monto = monto

    def crear_division(self):
        #Crea una division de cuenta
        conn = get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Division (cuenta_id, usuario_id, item, monto)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (self.cuenta_id, self.usuario_id, self.item, self.monto))
        conn.commit()
        division_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return division_id

    def obtener_divisiones(self, cuenta_id):
        #Obtiene todas las divisiones de una cuenta
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Division WHERE cuenta_id = %s"
        cursor.execute(query, (cuenta_id,))
        divisiones = cursor.fetchall()
        cursor.close()
        conn.close()
        return divisiones
