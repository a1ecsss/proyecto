import mysql.connector

def get_connection():
    #Establece la conexion a la base de datos MySQl
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="proyecto"
    )
