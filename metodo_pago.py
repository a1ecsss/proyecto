import mysql.connector
from db_connection import get_connection

class MetodoPago:
    def __init__(self, tipo):
        self.tipo = tipo

    def agregar_metodo_pago(self):
        #Agrega un nuevo método de pago a la base de datos
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO MetodoPago (tipo) VALUES (%s)"
        cursor.execute(query, (self.tipo,))
        conn.commit()
        metodo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return metodo_id

    def obtener_metodos_pago(self):
        #Devuelve una lista con todos los métodos de pago disponibles
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM MetodoPago"
        cursor.execute(query)
        metodos = cursor.fetchall()
        cursor.close()
        conn.close()
        return metodos
