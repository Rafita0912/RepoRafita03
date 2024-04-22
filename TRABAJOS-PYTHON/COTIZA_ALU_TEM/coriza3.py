import materiales
import inicializa

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image
from datetime import datetime

import sqlite3

mp_ac = inicializa.iniciar()

class opcion:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("390x660")
        self.ventana.title("Usuario")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)

        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="SELECCIONE LA OPCION A COTIZAR", font=("Comic Sans", 16,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=10)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/opciones_a_cotizar.png")
        self.img = self.img.resize((360,500))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=0, fill='x', side='top', pady=3)

        self.label_opcion = Label(self.frame2, text="OPCION A COTIZAR : ",font=("Comic Sans", 14,"bold"), bg="#88ff84", fg="black")
        self.label_opcion.grid(row=0, column=0, padx=10, sticky="e")
        self.entry_opcion = Entry(self.frame2, bd=0, width=8, font=("Comic Sans", 16,"bold"))
        self.entry_opcion.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        self.boton_cotizar = Button(self.frame2, text="COTIZAR", width=12, font=("Comic Sans", 12,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=1, column=0, columnspan=2, pady=15)

        self.boton_proforma = Button(self.frame2, text="PROFORMA", width=12, font=("Comic Sans", 12,"bold"), command=self.proforma)
        self.boton_proforma.grid(row=1, column=1, columnspan=2, pady=15)

        self.boton_salir = Button(self.frame2, text="SALIR", width=12, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=1, column=1, columnspan=2, pady=15)

        mainloop()

    def cotizar(self):
        op = self.entry_opcion.get()
        if op == "1":
            self.ventana.destroy()
            application=op1()
            mainloop()
        elif op == "2":
            self.ventana.destroy()
            application=op2()
            mainloop()
        elif op == "3":
            self.ventana.destroy()
            application=op3()
            mainloop()
        elif op == "4":
            self.ventana.destroy()
            application=op4()
            mainloop()
        elif op == "5":
            self.ventana.destroy()
            application=op5()
            mainloop()
        elif op == "6":
            self.ventana.destroy()
            application=op6()
            mainloop()
        elif op == "7":
            self.ventana.destroy()
            application=op7()
            mainloop()
        elif op == "8":
            self.ventana.destroy()
            application=op8()
            mainloop()
        elif op == "9":
            self.ventana.destroy()
            application=op9()
            mainloop()
        elif op == "10":
            self.ventana.destroy()
            application=op10()
            mainloop()
        elif op == "11":
            self.ventana.destroy()
            application=op11()
            mainloop()
        elif op == "12":
            self.ventana.destroy()
            application=op12()
            mainloop()
        elif op == "13":
            self.ventana.destroy()
            application=op13()
            mainloop()
        elif op == "14":
            self.ventana.destroy()
            application=op14()
            mainloop()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto")
    
        def proforma(self):
            if nombre == "TECNICO" and contra == "123":
                self.ventana.destroy()
                application=opciones()
                mainloop()
            else:
                messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto")

    def salir(self):
        self.ventana.destroy()

class op1:


class op2:


class op3:


class op4:


class op5:


class op6:


class op7:


class op8:


class op9:


class op10:


class op11:


class op12:


class op13:


class op14:


class opciones:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("390x560")
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
            self.ventana.destroy()
            ventana=Tk()
            application=Registro(ventana)
            ventana.mainloop()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto")


opcion()