import mysql.connector
from db_connection import get_connection

class Promocion:
    def __init__(self, descripcion, descuento, fecha_inicio, fecha_fin):
        self.descripcion = descripcion
        self.descuento = descuento
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def crear_promocion(self):
        #Crea una nueva promocion
        conn = get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Promocion (descripcion, descuento, fecha_inicio, fecha_fin)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (self.descripcion, self.descuento, self.fecha_inicio, self.fecha_fin))
        conn.commit()
        promocion_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return promocion_id

    def obtener_promociones(self):
        #Devuelve una lista de todas las promociones
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Promocion"
        cursor.execute(query)
        promociones = cursor.fetchall()
        cursor.close()
        conn.close()
        return promociones
