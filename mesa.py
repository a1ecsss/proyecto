import mysql.connector
from db_connection import get_connection
from random import randint as ran
from tkinter import messagebox as meg

class Mesa:
    def __init__(self, usuario, monto = 0):
        self.codigo = ""
        self.usuario = usuario
        self.monto = monto

    def create_code(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYX"
        numbers = "0123456789"
        for i in range(6):
            desition = [letters,numbers]
            da = ran(0,1)
            self.codigo += desition[da][ran(0,len(desition[da])-1)]

    def registrar_codigo(self):
        conexion = get_connection()  # Usamos la función para obtener la conexión
        cursor = conexion.cursor()
        registrado = False
        try:
            # Intentar insertar el código en la tabla
            sql = "INSERT INTO mesa (codigo, id_usuario, correo_usuario, monto) VALUES (%s, %s, %s, %s)"
            valores = (self.codigo, self.usuario.id, self.usuario.correo, self.monto)
            cursor.execute(sql, valores)
            conexion.commit()
            registrado = not False
        except mysql.connector.IntegrityError as e:
            error_mensaje = str(e)
            if "id_usuario" in error_mensaje:
                cursor.execute("SELECT codigo FROM mesa WHERE id_usuario = %s", (self.usuario.id,))
                resultado = cursor.fetchone()
                self.codigo = resultado[0]  # Asignar el valor de `codigo` encontrado al objeto
                meg.showinfo("","Ya tienes una mesa creada")
            elif "codigo" in error_mensaje:
                self.create_code()  # Generar un nuevo código
                self.registrar_codigo()  # Volver a intentar el registro
        cursor.close()
        conexion.close()

    def code_exist(self):
        conexion = get_connection()
        cursor = conexion.cursor()
        try:
            sql = "SELECT COUNT(*) FROM mesa WHERE codigo = %s"
            valores = (self.codigo,)
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()
            if resultado[0] > 0:
                return True
            else:
                return False
        except mysql.connector.Error as e:
            return False
        finally:
            cursor.close()
            conexion.close()

