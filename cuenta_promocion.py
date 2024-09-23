import mysql.connector
from db_connection import get_connection

class CuentaPromocion:
    def __init__(self, cuenta_id, promocion_id):
        self.cuenta_id = cuenta_id
        self.promocion_id = promocion_id

    def aplicar_promocion(self):
        #se asocia una promocion a una cuenta
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO CuentaPromocion (cuenta_id, promocion_id) VALUES (%s, %s)"
        cursor.execute(query, (self.cuenta_id, self.promocion_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def obtener_promociones_cuenta(self, cuenta_id):
        #Devuelve una lista de promociones aplicadas a una cuenta
        conn = get_connection()
        cursor = conn.cursor()
        query = """SELECT p.descripcion, p.descuento FROM Promocion p
                   JOIN CuentaPromocion cp ON p.id = cp.promocion_id
                   WHERE cp.cuenta_id = %s"""
        cursor.execute(query, (cuenta_id,))
        promociones = cursor.fetchall()
        cursor.close()
        conn.close()
        return promociones
