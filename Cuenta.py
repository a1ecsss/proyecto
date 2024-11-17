import mysql.connector
from db_connection import get_connection

class Cuenta:
    def __init__(self, main):
        self.main = main
        self.mfactura = [[]]
        self.total = 0

    def obtener_pedidos_usuario(self,usuario_id):
        conexion = get_connection()
        cursor = conexion.cursor()
        try:
            sql = "SELECT * FROM cuenta WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            resultados = cursor.fetchall()
            return resultados 
        except Exception as e:
            return None
        finally:
            cursor.close()
            conexion.close()

    def insertar_pedido(self,usuario_id, pedido, precio):
        conexion = get_connection()
        cursor = conexion.cursor()
        try:
            sql = "INSERT INTO cuenta (usuario_id, pedido, precio) VALUES (%s, %s, %s)"
            cursor.execute(sql, (usuario_id, pedido, precio))
            conexion.commit()
            self.factura()
            print("Pedido insertado correctamente.")
        except Exception as e:
            conexion.rollback()
            print("Error al insertar el pedido:", e)
        
        finally:
            cursor.close()
            conexion.close()

    def factura(self):
        self.mfactura = []
        pedidos = self.obtener_pedidos_usuario(self.main.usuario.id)
        total = 0
        for i in range(len(pedidos)):
            total+=float(pedidos[i][2])
            self.mfactura.append([pedidos[i][1],float(pedidos[i][2])])
        self.total = round(total,2)
        
    def pagar(self):
        conexion = get_connection()
        cursor = conexion.cursor()
        try:
            sql_cuenta = "DELETE FROM cuenta WHERE usuario_id = %s"
            cursor.execute(sql_cuenta, (self.main.usuario.id,))
            sql_mesa = "DELETE FROM mesa WHERE id_usuario = %s"
            cursor.execute(sql_mesa, (self.main.usuario.id,))
            conexion.commit()
            print(f"Se ha pagado la cuenta del usuario: {self.main.usuario.id}")
        
        except Exception as e:
            conexion.rollback()
            print("Error al eliminar las filas del usuario:", e)
        
        finally:
            cursor.close()
            conexion.close()
