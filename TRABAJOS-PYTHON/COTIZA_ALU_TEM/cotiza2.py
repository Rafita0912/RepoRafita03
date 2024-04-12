import materiales
import inicializa

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image

import sqlite3

mp = materiales.materia_prima()
acumula = inicializa.iniciar() 

class login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("390x680")
        self.ventana.title("Usuario")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand=True)

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="Introduzca usuario y contraseña", font=("Comic Sans", 13,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=5)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/logo_masercon.png")
        self.img = self.img.resize((340,80))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=True, fill="both", side="top", pady=5)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/foto_frentes_templado.png")
        self.img = self.img.resize((340,80))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=True, fill="both", side="top", pady=5)

        mainloop()

login()