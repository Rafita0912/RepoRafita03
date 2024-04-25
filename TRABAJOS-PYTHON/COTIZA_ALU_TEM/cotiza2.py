import materiales
import inicializa

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image
from datetime import datetime

import sqlite3

global mp_ac
mp_ac = inicializa.iniciar()
class login:
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
            global mp_ac
            mp_ac = inicializa.iniciar()
            self.ventana.destroy()
            application=registro()
            mainloop()
        else:
            messagebox.showinfo("NO", "ERROR ......... El USUARIO o la CONTRASEÑA no son correctos, intente nuevamente ........")

class registro:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("390x600")
        self.ventana.title("Registro")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="REGISTRO DE DATOS", font=("Comic Sans", 16,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/foto_frentes_templado.png")
        self.img = self.img.resize((260,130))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=True, fill="both", side="top", pady=0)

        self.label_obra = Label(self.frame2, text="OBRA : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_obra.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_obra = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_obra.grid(row=0, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_cliente = Label(self.frame2, text="Cliente :",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_cliente.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_cliente = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_cliente.grid(row=1, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_telefono = Label(self.frame2, text="Teléfono : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_telefono.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_telefono = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_telefono.grid(row=3, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_direccion = Label(self.frame2, text="Dirección : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_direccion.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_direccion = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_direccion.grid(row=4, column=1, columnspan=3, padx=5, pady=3, sticky="w")
        
        self.label_correo = Label(self.frame2, text="Correo Electrónico : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_correo.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_correo = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_correo.grid(row=5, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.label_observaciones = Label(self.frame2, text="Observaciones : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_observaciones.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_observaciones = Entry(self.frame2, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_observaciones.grid(row=6, column=1, columnspan=3, padx=5, pady=3, sticky="w")

        self.boton_registrar = Button(self.frame2, text="REGISTRAR Y COTIZAR", width=20, font=("Comic Sans", 12,"bold"), command=self.registrar)
        self.boton_registrar.grid(row=7, column=0, columnspan=2, pady=35, padx=10, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=12, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=7, column=1, columnspan=2, pady=35, padx=10, sticky="e")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()
        mainloop()

    def registrar(self):
        if len(self.entry_obra.get()) != 0 and len(self.entry_cliente.get()) != 0 and len(self.entry_telefono.get()) != 0 and len(self.entry_direccion.get()) != 0 and len(self.entry_correo.get()) != 0 and len(self.entry_observaciones.get()) != 0:
            mp_ac[196][3] = self.entry_obra.get()
            mp_ac[197][3] = self.entry_cliente.get()
            mp_ac[198][3] = self.entry_telefono.get()
            mp_ac[199][3] = self.entry_direccion.get()
            mp_ac[200][3] = self.entry_correo.get()
            mp_ac[201][3] = self.entry_observaciones.get()
            self.ventana.destroy()
            application=opcion()
            mainloop()
        else:
            messagebox.showinfo("NO", "ERROR .... algun dato ingresado no es correcto o no ingresaste algún dato, REVISA por favor e ingresa los datos correctamente.... ")

class opcion:
    def __init__(self):
        
        global mp
        mp = inicializa.iniciar()
        
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
        self.frame2.columnconfigure(2, weight=1)

        self.titulo = Label(self.frame1, text="SELECCIONE LA OPCION A COTIZAR", font=("Comic Sans", 16,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=10)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/opciones_a_cotizar.png")
        self.img = self.img.resize((360,500))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=0, fill='x', side='top', pady=3)

        self.label_opcion = Label(self.frame2, width=18, text="OPCION : ",font=("Comic Sans", 14,"bold"), bg="#88ff84", fg="black")
        self.label_opcion.grid(row=0, column=0, padx=10, sticky="e")
        self.entry_opcion = Entry(self.frame2, bd=0, width=10, font=("Comic Sans", 16,"bold"))
        self.entry_opcion.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        self.boton_cotizar = Button(self.frame2, text="COTIZAR", width=18, font=("Comic Sans", 12,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=1, column=0, pady=15, columnspan=1, padx=3, sticky="w")

        self.boton_proforma = Button(self.frame2, text="PROFORMA", width=18, font=("Comic Sans", 12,"bold"), command=self.proforma)
        self.boton_proforma.grid(row=1, column=1, pady=15, columnspan=1, padx=3, sticky="ew")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=1, column=2, pady=15, columnspan=1, padx=3, sticky="e")

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
            messagebox.showinfo("NO", "ERROR ...... algun dato ingresado no es correcto o no ingresaste la opcion ..... intenta nuevamente ....")
    
    def proforma(self):
        self.ventana.destroy()
        application=prof()
        mainloop()
            
    def salir(self):
        self.ventana.destroy()
        application=login()
        mainloop()

class op1:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("390x660")
        self.ventana.title("Usuario")

    def salir(self):
        self.ventana.destroy()
        

class op2:
    def salir(self):
        self.ventana.destroy()


class op3:
    def salir(self):
        self.ventana.destroy()


class op4:
    def salir(self):
        self.ventana.destroy()


class op5:
    def salir(self):
        self.ventana.destroy()


class op6:
    def salir(self):
        self.ventana.destroy()


class op7:
    def salir(self):
        self.ventana.destroy()

class op8:
    def salir(self):
        self.ventana.destroy()


class op9:
    def salir(self):
        self.ventana.destroy()


class op10:
    def salir(self):
        self.ventana.destroy()


class op11:
    def salir(self):
        self.ventana.destroy()


class op12:
    def salir(self):
        self.ventana.destroy()


class op13:
    def salir(self):
        self.ventana.destroy()


class op14:
    def salir(self):
        self.ventana.destroy()


class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La rersta es",resta)

    def multiplicar(self):
        multi=self.valor1*self.valor2
        print("El producto es",multi)

    def dividir(self):
        divi=self.valor1/self.valor2
        print("La division es",divi)

print(mp_ac[168][2])
print(mp_ac[214][2])

mp_ac[5][13] += 5
mp_ac[5][13] += 5

print(mp_ac[5][13])
print(mp_ac[196][2], mp_ac[196][3])

login()

print(mp_ac[196][2], mp_ac[196][3])


