import inicializa

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image
from datetime import datetime

import sqlite3

mp_ac = inicializa.iniciar()

class op1:
    def __init__(self):
        ventana = Tk()
        ventana.geometry("400x760")
        ventana.title("Op1")
        ventana.config(bg="#88ff84")

        self.titulo = Label(ventana, text="FRENTE TEMPLADO TIPO SPYDER", font=("Comic Sans", 16,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op1a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(ventana, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=True, fill="both", side="top", pady=0)

        self.es = StringVar()
        self.co = StringVar()
        self.fr = StringVar()
        self.pu = StringVar()

        self.lista1 = ["8 mm", "10 mm"]
        self.lista2 = ["Incoloro", "Color"]
        self.lista3 = ["Con Freno Hidráulico", "Sin Freno, con pivote"]       
        self.lista4 = ["Puerta", "Ventana"]

        self.opcion1 = OptionMenu(ventana, self.es, *self.lista1)
        self.opcion2 = OptionMenu(ventana, self.co, *self.lista2)
        self.opcion3 = OptionMenu(ventana, self.fr, *self.lista3)
        self.opcion4 = OptionMenu(ventana, self.pu, *self.lista4)

        self.opcion1.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.opcion2.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.opcion3.configure(width=30, activebackground="gray", bd=0, cursor="hand2")
        self.opcion4.configure(width=30, activebackground="gray", bd=0, cursor="hand2")

        self.es.set("Selecione el espesor del vidrio")
        self.co.set("Seleccione el color del vidrio")
        self.fr.set("Seleccione si lleva Freno o No")
        self.pu.set("Seleccione si es Puerta o Ventana")

        self.label_base = Label(ventana, text="BASE en centimetros : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(ventana, text="ALTURA en centimetros :",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_altura.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_altura = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_altura.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_cantidad = Label(ventana, text="CANTIDAD : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_cantidad.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_cantidad = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_cantidad.grid(row=2, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_espesor = Label(ventana, text="ESPESOR : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_espesor.grid(row=3, column=0, padx=5, pady=3, sticky="e")
        self.opcion1 = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.opcion1.grid(row=3, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_color = Label(ventana, text="COLOR : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_color.grid(row=4, column=0, padx=5, pady=3, sticky="e")
        self.opcion2 = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.opcion2.grid(row=4, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_nvertical = Label(ventana, text="N-DIV.VERTICALES : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_nvertical.grid(row=5, column=0, padx=5, pady=3, sticky="e")
        self.entry_nvertical = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_nvertical.grid(row=5, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_mhorizontal = Label(ventana, text="M-DIV.HORIZONTALES : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_mhorizontal.grid(row=6, column=0, padx=5, pady=3, sticky="e")
        self.entry_mhorizontal = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.entry_mhorizontal.grid(row=6, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_freno = Label(ventana, text="FRENO HIDRAULICO : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_freno.grid(row=7, column=0, padx=5, pady=3, sticky="e")
        self.opcion3 = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.opcion3.grid(row=7, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_puertaventana = Label(ventana, text="PUERTA / VENTANA : ",font=("Comic Sans", 12,"bold"), bg="#88ff84", fg="black")
        self.label_puertaventana.grid(row=8, column=0, padx=5, pady=3, sticky="e")
        self.opcion4 = Entry(ventana, bd=0, width=20, font=("Comic Sans", 12,"bold"))
        self.opcion4.grid(row=8, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.boton_cotizar = Button(ventana, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 12,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=9, column=0, pady=15, columnspan=1, padx=3, sticky="w")

        self.boton_salir = Button(ventana, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=9, column=1, pady=15, columnspan=1, padx=3, sticky="e")

        mainloop()
    
    def salir(self):
        ventana.destroy()
        application=login()
        mainloop()

    def cotizar(self):
        if len(self.entry_base.get()) != 0 and len(self.entry_altura.get()) != 0 and len(self.entry_cantidad.get()) != 0 and len(self.entry_espesor.get()) != 0 and len(self.entry_color.get()) != 0 and len(self.entry_nvertical.get()) != 0 and len(self.entry_mhorizontal.get()) != 0 and len(self.entry_freno.get()) != 0 and len(self.entry_puertaventana.get()) != 0:
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
                    break
                except ValueError:
                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD o LAS DIVISIONES no son correctas, revise los datos ingresados e introduzca nuevamente los valores .... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES ")
                    return(False)
            global base, altura, cantidad, espesor, color, nvertical, mhorizontal, freno, puertaventana

            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = self.entry_espesor.get()
            color = self.entry_color.get()
            nvertical = int(self.entry_nvertical.get())
            mhorizontal = int(self.entry_mhorizontal.get())
            freno = self.entry_freno.get()
            puertaventana = self.entry_puertaventana.get()

            ventana.destroy()
            ventana=Tk()
            application=opcion()
            mainloop()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")
    
    def proforma(self):
        self.ventana.destroy()
        #application=login()
        #mainloop()


ventana=Tk()
op1()
mainloop()
