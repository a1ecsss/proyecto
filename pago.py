import mysql.connector
from db_connection import get_connection

class Pago:
    def __init__(self, monto, fecha, usuario_id, metodoPago_id):
        self.monto = monto
        self.fecha = fecha
        self.usuario_id = usuario_id
        self.metodoPago_id = metodoPago_id

    def realizar_pago(self):
        #Registra un nuevo pago en la base de datos
        conn = get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Pago (monto, fecha, usuario_id, metodoPago_id)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (self.monto, self.fecha, self.usuario_id, self.metodoPago_id))
        conn.commit()
        pago_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return pago_id

    def obtener_pagos_usuario(self, usuario_id):
        #Obtiene el historial de pagos de un usuario
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Pago WHERE usuario_id = %s"
        cursor.execute(query, (usuario_id,))
        pagos = cursor.fetchall()
        cursor.close()
        conn.close()
        return pagos
