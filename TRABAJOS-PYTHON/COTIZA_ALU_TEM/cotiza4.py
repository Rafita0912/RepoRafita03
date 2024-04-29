import inicializa

from tkinter import *
from tkinter import Tk, StringVar, OptionMenu
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image
from datetime import datetime

import sqlite3

mp_ac = inicializa.iniciar()

class op2:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("380x740")
        self.ventana.title("Op2")

        self.frame1 = Frame(self.ventana)
        self.frame1.configure(bg="#88ff84")
        self.frame1.pack(fill="both", expand="True")

        self.frame2 = Frame(self.ventana)
        self.frame2.configure(bg="#88ff84")
        self.frame2.pack(fill="both", expand=True)

        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame1, text="FRENTE TEMPLADO \n CON HERRAJES Y VIENTOS", font=("Comic Sans", 14,"bold"), bg="#88ff84")
        self.titulo.pack(side="top", pady=15)

        self.img = Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/op2a.png")
        self.img = self.img.resize((260,260))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame1, image = self.render, bg="#88ff84")
        self.fondo.pack(expand=True, fill="both", side="top", pady=0)

        self.label_base = Label(self.frame2, text="BASE en centimetros : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_base.grid(row=0, column=0, padx=5, pady=3, sticky="e")
        self.entry_base = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_base.grid(row=0, column=1, columnspan=3, padx=10, pady=3, sticky="w")
        
        self.label_altura = Label(self.frame2, text="ALTURA en centimetros :",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
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
        
        self.label_color = Label(self.frame2, text="VIDRIO INCOLORO = 1 : \n VIDRIO COLOR = 2 : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
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
        
        self.label_freno = Label(self.frame2, text="CON FRENO = 1 : \n CON PIVOTE = 2 : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_freno.grid(row=7, column=0, padx=5, pady=3, sticky="e")
        self.entry_freno = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_freno.grid(row=7, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.label_puertaventana = Label(self.frame2, text="PUERTA = 1 : \n VENTANA = 2 : ",font=("Comic Sans", 11,"bold"), bg="#88ff84", fg="black", width=50)
        self.label_puertaventana.grid(row=8, column=0, padx=5, pady=3, sticky="e")
        self.entry_puertaventana = Entry(self.frame2, bd=0, width=30, font=("Comic Sans", 11,"bold"))
        self.entry_puertaventana.grid(row=8, column=1, columnspan=3, padx=10, pady=3, sticky="w")

        self.boton_cotizar = Button(self.frame2, text="COTIZAR Y SEGUIR", width=18, font=("Comic Sans", 11,"bold"), command=self.cotizar)
        self.boton_cotizar.grid(row=9, column=0, pady=15, columnspan=1, padx=25, sticky="w")

        self.boton_salir = Button(self.frame2, text="SALIR", width=18, font=("Comic Sans", 12,"bold"), command=self.salir)
        self.boton_salir.grid(row=9, column=1, pady=15, columnspan=1, padx=10, sticky="ew")

        mainloop()
    
    def salir(self):
        self.ventana.destroy()
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
                    a = int(self.entry_espesor.get())
                    c = int(self.entry_color.get())
                    b = int(self.entry_freno.get())
                    d = int(self.entry_puertaventana.get())
                    break
                except ValueError:
                    messagebox.showinfo("NO", "ERROR ....... La CANTIDAD o LAS DIVISIONES no son correctas, revise los datos ingresados e introduzca nuevamente los valores correctos.... RECUERDE QUE DEBEN SER NUMEROS SIN DECIMALES")
                    return(False)
            global base, altura, cantidad, espesor, color, nvertical, mhorizontal, freno, puertaventana

            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            cantidad = int(self.entry_cantidad.get())
            espesor = int(self.entry_espesor.get())
            color = int(self.entry_color.get())
            nvertical = int(self.entry_nvertical.get())
            mhorizontal = int(self.entry_mhorizontal.get())
            freno = int(self.entry_freno.get())
            puertaventana = int(self.entry_puertaventana.get())

            self.ventana.destroy()
            application=previo()
            mainloop()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto o no ingresaste algún dato")
    

mp_ac[5][13] += 5
mp_ac[5][13] += 5

print(mp_ac[5][13])
print(mp_ac[196][2], mp_ac[196][3])

op2()

print(mp_ac[196][2], mp_ac[196][3])
