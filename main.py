from tkinter import*
from tkinter import messagebox
from db_connection import get_connection
from usuario import Usuario
from mesa import Mesa
from tkinter import Canvas
from PIL import Image, ImageTk  
from random import randint as ran
from QR import*
from tkinter import filedialog
from menu import Menu
from cuenta import Cuenta
import multiprocessing
from promocion import *

class App(Tk):
    def __init__(self):
        super().__init__()
        #instancias
        self.usuario = Usuario()
        self.mesa = Mesa(self)
        self.menu = Menu(self)
        self.cuenta = Cuenta(self)
        self.promocion = Promocion()
        self.pantalla_login()

    def pantalla_login(self):
        self.title("Iniciar Sesión")
        self.geometry("500x700")
        self.config(padx=20, pady=20)
        text = ["Iniciar sesión","Email:","Contraseña:"]
        placeL = [(250-190,100-30),(80,220),(80,270)]
        placeE = [(220,300-80),(220,300-30)]
        fonts = ["Courier 30 bold","Times 15","Times 15"]
        self.Entrys = []
        for i in range(len(text)):
            Label(self, text=text[i], font=fonts[i]).place(x=placeL[i][0],y=placeL[i][1])
        for i in range(len(placeE)):
            if i: self.Entrys.append(Entry(self, width=25,show="*"))
            else: self.Entrys.append(Entry(self, width=25))
            self.Entrys[i].place(x=placeE[i][0],y=placeE[i][1])
        Button(self, text="Iniciar Sesión",font="Times 14" , command=self.login, width=33, relief="flat", bg="#2e2e2e",fg="white").place(x=60,y=380)

    def login(self):
        if self.usuario.login(self.Entrys[0].get().strip(),self.Entrys[1].get().strip()):
            self.mesa.usuario = self.usuario
            self.pantalla_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def limpiar_ventana(self):
        for widget in self.winfo_children():
            widget.destroy()

    def pantalla_principal(self):
        self.limpiar_ventana()
        self.title("Pantalla Principal")
        Label(self, text="Divise", font="Courier 39 bold").pack(pady=(40,10))
        Label(self, text="Bienvenido al menú de opciones, elige una opción: ", font="Times 12").pack(pady=(30,25))
        Button(self, text="Crear Mesa", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.crear_mesa).pack(pady=10)
        Button(self, text="Unirse a una Mesa", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.unirse_mesa).pack(pady=10)
        Button(self, text="Realizar Pedido", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.hacer_pedido).pack(pady=10)
        Button(self, text="Pagar Cuenta", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.pagar_cuenta).pack(pady=10)
        Button(self, text="Ver Promociones", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.ver_promociones).pack(pady=10)
        Button(self, text="Cerrar Sesión", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.cerrar_sesion).pack(pady=10)

    def crear_mesa(self):
       self.limpiar_ventana()
       self.home_button()
       self.mesa.create_code()
       self.mesa.registrar_codigo()
       Label(self, text="Código de Mesa", font="Courier 39 bold").pack(pady=(100,0))
       Label(self, text="Escanea o escríbe el código para unirte: ", font="Times 12").pack(pady=(5,0))
       Label(self, text=self.mesa.codigo, font="Times 39 bold", fg="#2e2e2e").pack(pady=(10,20))
       self.setImage(createQR(self.mesa.codigo))
       
    def unirse_mesa(self):
       def mostrar():
           if self.mesa.code_exist():
               messagebox.showinfo("","Te haz unido exitosamente!")
               Label(self, text="Código al que te haz unido:", font="Times 22").pack(pady=(20,0))
               Label(self, text=self.mesa.codigo, font="Times 39 bold").pack(pady=(20,0))
           else:
               self.mesa.codigo = ""
               messagebox.showerror("Error","El codigo que ingresaste no existe")

       def ingresar():
           codigo = Ecodigo.get().upper().strip()
           self.mesa.codigo = codigo
           self.mesa.unirse_mesa()
           mostrar()
       def import_image():
           root = filedialog.askopenfilename()
           codigo = scanQR(root)
           self.mesa.codigo = codigo
           mostrar()
       self.limpiar_ventana()
       self.home_button()
       Label(self, text="Unirse", font="Courier 39 bold").pack(pady=(100,0))
       Label(self, text="Escanea o escríbe el código para unirte: ", font="Times 12").pack(pady=(5,0))
       Ecodigo = Entry()
       Ecodigo.pack(pady=(15,20))
       Button(self, text="Ingresar", font=("Times", 15), bg="#2e2e2e",fg="white" , relief="flat", width=10, command=ingresar).pack(pady=(0,20))
       Button(self, text="Escanear Código", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=import_image).pack(pady=10)

    def hacer_pedido(self):
        self.limpiar_ventana() 
        self.home_button()
        def ordenar(nombre):
            self.menu.charge(round(self.mesa.get_monto()+ self.menu.obtener_precio_por_nombre(nombre),2))
            self.cuenta.insertar_pedido(self.usuario.id,nombre, self.menu.obtener_precio_por_nombre(nombre))
            self.hacer_pedido()
        # Mostrar los elementos del menú
        Label(self, text="Menú", font="Courier 39 bold").pack(pady=(40,10))
        for item in self.menu.menu_items:
            item_frame = Frame(self, bg="white")
            item_frame.pack(fill="x",pady=(6,6))
            nombre_label = Label(item_frame, text=item["nombre"], font=("Times", 16), bg="white", anchor="w")
            nombre_label.pack(side="left", fill="x", expand=True)
            precio_label = Label(item_frame, text=f"Q{item['precio']}", font=("Times", 16), bg="white")
            precio_label.pack(side="left")
            # Botón de ordenar
            ordenar_button = Button(item_frame, text="ORDENAR", font=("Times", 12), bg="#2e2e2e",fg="white" , relief="flat", command=lambda item=item: ordenar(item["nombre"]))
            ordenar_button.pack(side="right", padx=5)
        Label(self, text=f"TOTAL: Q{self.cuenta.total}", font="Times 20 bold", bg="white", anchor="w").pack(pady=15)


    def pagar_cuenta(self):
        self.limpiar_ventana()
        self.home_button()
        Label(self, text="Factura", font="Courier 39 bold").pack(pady=(40,10))
        self.cuenta.factura()
        for i in range(len(self.cuenta.mfactura)):
            item_frame = Frame(self, bg="white")
            item_frame.pack(fill="x",pady=(4,4))
            nombre_label = Label(item_frame, text=self.cuenta.mfactura[i][0], font=("Times", 16), bg="white", anchor="w")
            nombre_label.pack(side="left", fill="x", expand=True)
            precio_label = Label(item_frame, text=f"Q{self.cuenta.mfactura[i][1]}", font=("Times", 16), bg="white")
            precio_label.pack(side="right")
        Label(self, text=f"TOTAL MESA: Q{self.mesa.get_monto()}", font="Times 20 bold", bg="white", anchor="w").pack(pady=10)
        Label(self, text=f"TOTAL INDIVIDUAL: Q{self.cuenta.total}", font="Times 20 bold", bg="white", anchor="w").pack(pady=(5,10))
        Button(self, text="Pagar", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.metodo_pago).pack(pady=10)

    def pagar(self):
        self.cuenta.pagar()
        self.mesa = Mesa(self)
        self.menu = Menu(self)
        self.cuenta = Cuenta(self)

    def metodo_pago(self):
        self.limpiar_ventana()
        self.home_button()
        Label().pack()
        def pago_tarjeta():
            self.limpiar_ventana()
            self.home_button()
            Label().pack()
            Label(self, text="Pago Tarjeta", font="Courier 39 bold").pack(pady=(60, 10))
            Label(self, text="Ingresa los datos de tu tarjeta:", font="Times 14").pack(pady=(10, 0))
            Label(self, text="Número de Tarjeta:", font="Times 12").pack(pady=(10, 0))
            tarjeta_entry = Entry(self, width=30)
            tarjeta_entry.pack(pady=(5, 10))
            Label(self, text="Fecha de Expiración (MM/AA):", font="Times 12").pack(pady=(10, 0))
            expiracion_entry = Entry(self, width=15)
            expiracion_entry.pack(pady=(5, 10))
            Label(self, text="CVV:", font="Times 12").pack(pady=(10, 0))
            cvv_entry = Entry(self, width=5, show="*")
            cvv_entry.pack(pady=(5, 20))
            Button(self,text="Pagar",font=("Times", 16),bg="#2e2e2e",fg="white",relief="flat",command=lambda: [messagebox.showinfo("Pago", "Pago realizado con tarjeta"),self.pagar(),self.pantalla_principal()],).pack(pady=20)

        def pago_efectivo():
            self.limpiar_ventana()
            self.home_button()
            Label().pack()
            Label(self, text="Pago Efectivo", font="Courier 39 bold").pack(pady=(60, 10))
            Label(self, text="Dirígete a la caja para completar tu pago.", font="Times 14").pack(pady=(20, 20))
            self.pagar()
            Button(self,text="Volver al Menú Principal",font=("Times", 16),bg="#2e2e2e",fg="white",relief="flat",command=self.pantalla_principal).pack(pady=20)

        # Pantalla de selección de método de pago
        Label(self, text="Método de Pago", font="Courier 39 bold").pack(pady=(40, 10))
        Label(self, text="Selecciona tu método de pago:", font="Times 14").pack(pady=(20, 20))
        Button(self,text="Pago con Tarjeta",font=("Times", 16),bg="#2e2e2e",fg="white",relief="flat",width=20,command=pago_tarjeta,).pack(pady=10)
        Button(self,text="Pago en Efectivo",font=("Times", 16),bg="#2e2e2e",fg="white",relief="flat",width=20,command=pago_efectivo,).pack(pady=10)

    def pago_tarjeta(self):
        self.limpiar_ventana()
        self.home_button()


    def home_button(self):
        Button(self,text="⌂", font=("Times", 22), width=3, bg="#2e2e2e",fg="white" , relief="flat", command=self.pantalla_principal).place(x=10,y=10)

    def cerrar_sesion(self):
        self.limpiar_ventana()
        self.pantalla_login()

    def setImage(self, root):
       imagen_original = Image.open(root)
       imagen_redimensionada = imagen_original.resize((300, 300))
       img = ImageTk.PhotoImage(imagen_redimensionada)
       lbl_img = Label(self, image=img)
       lbl_img.pack()
       lbl_img.image = img


if __name__ == '__main__':
    # Crear dos procesos para ejecutar el programa al mismo tiempo
    proceso1 = multiprocessing.Process(target=App)
    proceso2 = multiprocessing.Process(target=App)

    # Iniciar ambos procesos
    proceso1.start()
    proceso2.start()

    # Esperar a que ambos procesos terminen
    proceso1.join()
    proceso2.join()

App().mainloop()
