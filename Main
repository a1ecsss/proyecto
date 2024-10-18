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
    def _init_(self):
        super()._init_()
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
