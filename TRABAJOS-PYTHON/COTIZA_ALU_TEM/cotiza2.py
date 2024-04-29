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

        self.boton_ingresar = Button(self.frame2, text="INGRESAR", width=12, font=("Comic Sans", 16,"bold"), command=self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, padx=15, pady=35, sticky="w")

        self.boton_ingresar = Button(self.frame2, text="SALIR", width=12, font=("Comic Sans", 16,"bold"), command=self.salir)
        self.boton_ingresar.grid(row=2, column=1, columnspan=2, padx=15, pady=35, sticky="e")

        mainloop()

    def entrar(self):
        global nombre, contra
        nombre = self.entry_usuario.get()
        contra = self.entry_password.get()
        if (nombre == "TECNICO" and contra == "123") or (nombre == "RAFA" and contra == "555"):
            global mp_ac
            mp_ac = inicializa.iniciar()
            self.ventana.destroy()
            application=registro()
        else:
            messagebox.showinfo("NO", "ERROR ......... El USUARIO ó la CONTRASEÑA no son correctos, intente nuevamente ........")

    def salir(self):
        self.ventana.destroy()


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
        else:
            messagebox.showinfo("NO", "ERROR .... algun dato ingresado no es correcto o no ingresaste algún dato, REVISA por favor e ingresa los datos correctamente.... ")

class opcion:
    def __init__(self):
        
        global mp
        mp = inicializa.iniciar()
        
        self.ventana = Tk()
        self.ventana.geometry("390x700")
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

        self.label_opcion = Label(self.frame2, width=18, text="OPCION : ",font=("Comic Sans", 14,"bold"), bg="#88ff84", fg="black")
        self.label_opcion.grid(row=0, column=0, padx=10, sticky="e")
        self.entry_opcion = Entry(self.frame2, bd=0, width=10, font=("Comic Sans", 16,"bold"))
        self.entry_opcion.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        self.boton_cotizar = Button(self.frame2, text="COTIZAR", width=25, font=("Comic Sans", 12,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=1, column=0, pady=15, columnspan=1, padx=3, sticky="w")

        self.boton_proforma = Button(self.frame2, text="PROFORMA", width=25, font=("Comic Sans", 12,"bold"), command=self.proforma)
        self.boton_proforma.grid(row=1, column=1, pady=15, columnspan=1, padx=3, sticky="e")

        self.boton_proforma = Button(self.frame2, text="MATERIALES", width=25, font=("Comic Sans", 12,"bold"), command=self.material)
        self.boton_proforma.grid(row=2, column=0, pady=5, columnspan=1, padx=3, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=25, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=2, column=1, pady=5, columnspan=1, padx=3, sticky="e")

        mainloop()

    def cotizar(self):
        global base, altura, cantidad, espesor, color, nvertical, mhorizontal, freno, puertaventana

        base = float(0)
        altura = float(0)
        cantidad = int(0)
        espesor = int(0)
        color = int(0)
        nvertical = int(0)
        mhorizontal = int(0)
        freno = int(0)
        puertaventana = int(0)

        op = self.entry_opcion.get()
        if op == "1":
            self.ventana.destroy()
            application=op1()

        elif op == "2":
            self.ventana.destroy()
            application=op2()

        elif op == "3":
            self.ventana.destroy()
            application=op3()

        elif op == "4":
            self.ventana.destroy()
            application=op4()

        elif op == "5":
            self.ventana.destroy()
            application=op5()

        elif op == "6":
            self.ventana.destroy()
            application=op6()

        elif op == "7":
            self.ventana.destroy()
            application=op7()

        elif op == "8":
            self.ventana.destroy()
            application=op8()

        elif op == "9":
            self.ventana.destroy()
            application=op9()

        elif op == "10":
            self.ventana.destroy()
            application=op10()

        elif op == "11":
            self.ventana.destroy()
            application=op11()

        elif op == "12":
            self.ventana.destroy()
            application=op12()

        elif op == "13":
            self.ventana.destroy()
            application=op13()

        elif op == "14":
            self.ventana.destroy()
            application=op14()

        else:
            messagebox.showinfo("NO", "ERROR ...... algun dato ingresado no es correcto o no ingresaste la opcion ..... intenta nuevamente ....")
    
    def proforma(self):
        self.ventana.destroy()
        application=proforma()


    def material(self):
        if nombre == "RAFA" and contra == "555":
            self.ventana.destroy()
            application=material()

        else:
            messagebox.showinfo("NO", "ERROR ......... Este USUARIO solo puede ver e imprimir la PROFORMA, el detalle de materiales solo puede ser visto por el ADMINISTRADOR, seleccione la opción correcta ........")
            
    def salir(self):
        self.ventana.destroy()
        application=login()

class op1:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op1")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="FRENTE TEMPLADO \n TIPO SPYDER", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op1a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=True, fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en metros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en metros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(self.frame2, text="CANTIDAD : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(self.frame2, text="ESPESOR en mm. = 8   ó   10  : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.entry_espesor = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_espesor.grid(row=3, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO = 1 : \n COLOR = 2 : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.entry_color = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_color.grid(row=4, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_nvertical = Label(self.frame2, text="N DIV. VERTICALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_mhorizontal = Label(self.frame2, text="M DIV. HORIZONTALES : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_mhorizontal.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.entry_mhorizontal = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_mhorizontal.grid(row=6, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        

        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=9, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=9, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
        application=login()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.entry_espesor.get()) != 0 and len(self.entry_color.get()) != 0 and len(self.entry_nvertical.get()) != 0 and len(self.entry_mhorizontal.get()) != 0:
            while True:
                try:
                    x = float(self.entry_base.get())
                    y = float(self.entry_altura.get())
                    break
                except ValueError:
                    messagebox.showinfo("NO", "ERROR ....... La medida de la BASE ó ALTURA no son correctas, revise los doatos ingresados e introduzca nuevamente los valores .... RECUERDE LA SEPARACION DECIMAL ES CON PUNTO . ")
                    return(false)
            while True:
                try:
                    x = int(self.entry_cantidad.get())
                    y = int(self.entry_nvertical.get())
                    z = int(self.entry_mhorizontal.get())
                    a = int(self.entry_espesor.get())
                    c = int(self.entry_color.get())

                    break
                except ValueError:
                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD o LAS DIVISIONES no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)

            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = int(self.entry_espesor.get())
            color = int(self.entry_color.get())
            nvertical = int(self.entry_nvertical.get())
            mhorizontal = int(self.entry_mhorizontal.get())

            if espesor == 8:
                if color == 1:
                    

            self.ventana.destroy()
            application=opcion()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")
        
class previo:
    def salir(self):
        self.ventana.destroy()
        application=opcion()

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
print(mp_ac[196][2])
print(mp_ac[196][3])

login()

print(mp_ac[196][2])
print(mp_ac[196][3])

