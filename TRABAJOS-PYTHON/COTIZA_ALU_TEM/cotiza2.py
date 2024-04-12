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
        self.ventana.geometry("390x600")
        self.ventana.title("Usuario")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="Introduzca usuario y contraseña", font=("Comic Sans", 16,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/logo_masercon.png")
        self.img = self.img.resize((340,100))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=True, fill="both", side="top", pady=0)

        self.label_usuario = Label(self.frame2, text="USUARIO",font=("Comic Sans", 16,"bold"), bg="#88ff84", fg="black")
        self.label_usuario.grid(row=0, column=0, padx=10, sticky="e")
        self.entry_usuario = Entry(self.frame2, bd=0, width=14, font=("Comic Sans", 16,"bold"))
        self.entry_usuario.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        self.label_password = Label(self.frame2, text="CONTRASEÑA",font=("Comic Sans", 16,"bold"), bg="#88ff84", fg="black")
        self.label_password.grid(row=1, column=0, padx=10, sticky="e")
        self.entry_password = Entry(self.frame2, bd=0, width=14, font=("Comic Sans", 16,"bold"), show="*")
        self.entry_password.grid(row=1, column=1, columnspan=3, padx=5, sticky="w")

        self.boton_ingresar = Button(self.frame2, text="INGRESAR", width=16, font=("Comic Sans", 16,"bold"), command=self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=35)


    mainloop()

    def entrar(self):
        nombre = self.entry_usuario.get()
        contra = self.entry_password.get()
        if nombre == "TECNICO" and contra == "123":
            messagebox.showinfo("Acceso correcto")
        else:
            messagebox.showinfo("ERROR algun dato ingresado no es correcto")


login()