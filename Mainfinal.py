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

class App(Tk):
    def __init__(self):
        super().__init__()
        #instancias
        self.usuario = Usuario()
        self.mesa = Mesa(self.usuario)
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
        if 1:#self.usuario.login(self.Entrys[0].get().strip(),self.Entrys[1].get().strip()):
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
        Label(self, text="Bienvenido al menú de opciones, elige una opción: ", font="Times 12").pack(pady=40)
        Button(self, text="Crear Mesa", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.crear_mesa).pack(pady=10)
        Button(self, text="Unirse a una Mesa", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.unirse_mesa).pack(pady=10)
        Button(self, text="Ver Cuentas", font=("Times", 22), bg="#2e2e2e",fg="white" , relief="flat", width=20, command=self.ver_cuentas).pack(pady=10)
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

    def ver_cuentas(self):
        self.limpiar_ventana() 
        self.home_button()

    def ver_promociones(self):
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


App().mainloop()



