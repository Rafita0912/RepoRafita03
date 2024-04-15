import materiales
import inicializa

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image

import sqlite3

mp = materiales.materia_prima()
acumulado_cantidad = inicializa.iniciar() 
cotiza1c = inicializa.iniciar()
cotiza1s = inicializa.iniciar()
cotiza2c = inicializa.iniciar()
cotiza2s = inicializa.iniciar()

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
            self.ventana.destroy()
            ventana=Tk()
            application=Registro(ventana)
            ventana.mainloop()
        else:
            messagebox.showinfo("NO", "ERROR algun dato ingresado no es correcto")
class Registro:

    db_name='database_proyecto.db'
    
    def __init__(self, ventana):
        self.window=ventana   
        self.window.title("REGISTRO DE DATOS")
        self.window.geometry("393x600")
        self.window.resizable(0,0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"

        titulo= Label(ventana, text="REGISTRO DE DATOS",fg="black",font=("Comic Sans", 13,"bold"),pady=5).pack()

        "--------------- Logo e imagenes ------------"

        imagen_registro=Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/logo_masercon.png")
        nueva_imagen=imagen_registro.resize((240,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=3)

        imagen_registro=Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/foto_frentes_templado.png")
        nueva_imagen=imagen_registro.resize((260,130))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=3)

        "--------- Marco para toma de datos ------------"

        marco = LabelFrame(ventana, text="Registro de datos",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2,pady=3)
        marco.pack()

        "--------- Formulario de toma de datos ----------"

        label_obra=Label(marco,text="OBRA : ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=3)
        self.obra=Entry(marco,width=25)
        self.obra.focus()
        self.obra.grid(row=0, column=1, padx=5, pady=3)
        ob = self.obra

        label_cliente=Label(marco,text="Cliente : ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=3)
        self.cliente=Entry(marco,width=25)
        self.cliente.grid(row=1, column=1, padx=10, pady=3)
        cl = self.cliente

        label_telefono=Label(marco,text="Teléfono: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=10,pady=3)
        self.telefono=Entry(marco,width=25)
        self.telefono.grid(row=2, column=1, padx=10, pady=3)
        te = self.telefono

        label_direccion=Label(marco,text="Dirección : ",font=("Comic Sans", 10,"bold")).grid(row=3,column=0,sticky='s',padx=10,pady=3)
        self.direccion=Entry(marco,width=25)
        self.direccion.grid(row=3, column=1, padx=10, pady=3)
        di = self.direccion

        label_correo=Label(marco,text="Correo electronico: ",font=("Comic Sans", 10,"bold")).grid(row=4,column=0,sticky='s',padx=10,pady=8)
        self.correo=Entry(marco,width=25)
        self.correo.grid(row=4, column=1, padx=10, pady=8)
        co = self.correo

        label_observaciones=Label(marco,text="Observaciones : ",font=("Comic Sans", 10,"bold")).grid(row=5,column=0,sticky='s',padx=10,pady=3)
        self.observaciones=Entry(marco,width=25)
        self.observaciones.grid(row=5, column=1, padx=10, pady=3)
        obs = self.observaciones

        "--------------- Frame botones --------------------"

        frame_botones=Frame(ventana)
        frame_botones.pack()

        "------------------ Botones -----------------------"
        
        boton_registrar=Button(frame_botones,text="REGISTRAR Y COTIZAR",command=self.Registrar_usuario ,height=2,width=20,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)

        boton_cancelar=Button(frame_botones,text="CERRAR",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
    def Validar_formulario_completo(self):
        if len(self.obra.get()) !=0 and len(self.cliente.get()) !=0 and len(self.telefono.get()) !=0 and len(self.direccion.get()) !=0 and len(self.correo.get()) !=0 and len(self.observaciones.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR EN REGISTRO", "Complete todos los campos del formulario")

    def Registrar_usuario(self):
        if self.Validar_formulario_completo():
            query='INSERT INTO Usuarios VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.obra.get(),self.cliente.get(),self.telefono.get(),self.direccion.get(),self.correo.get(),self.observaciones.get())
            ventana=Tk()
            application=Opciones(ventana)
            ventana.mainloop()

class Opciones:
    
    def __init__(self, ventana):
        self.raiz=ventana   
        self.raiz.title("OPCIONES")
        self.raiz.geometry("393x600")
        self.raiz.resizable(0,0)
        self.raiz.config(bd=10)
        
        "--------------- Titulo --------------------"

        titulo= Label(ventana, text="SELECCIONE EL CERRAMIENTO A COTIZAR",fg="black",font=("Comic Sans", 13,"bold"),pady=5).pack()

        "--------------- Logo e imagenes ------------"

        imagen_registro=Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/logo_masercon.png")
        nueva_imagen=imagen_registro.resize((240,60))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=3)

        imagen_registro=Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/frentes_fijos.png")
        nueva_imagen=imagen_registro.resize((250,100))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=3)

        imagen_registro=Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/puerta_ventana_corrediza.png")
        nueva_imagen=imagen_registro.resize((250,100))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=3)

        imagen_registro=Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/puerta_batiente_1.png")
        nueva_imagen=imagen_registro.resize((250,100))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=3)

        imagen_registro=Image.open("C:/Users/PcAsusZenbookRafita/Desktop/REPO_RAFAEL_ANTEQUERA/TRABAJOS-PYTHON/COTIZA_ALU_TEM/imagenes/puerta_batiente_2.png")
        nueva_imagen=imagen_registro.resize((250,100))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(ventana, image= render)
        label_imagen.image=render
        label_imagen.pack(pady=3)

        "--------- Marco para toma de datos ------------"

        marco = LabelFrame(ventana, text="Opción seleccionada",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2,pady=3)
        marco.pack()

        "--------- Formulario de toma de datos ----------"

        label_opcion=Label(marco,text="SELECCIONE LA OPCION : ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=3)
        self.opcion=Entry(marco,width=25)
        self.opcion.focus()
        self.opcion.grid(row=0, column=1, padx=5, pady=3)
        opcion = self.opcion

        "--------------- Frame botones --------------------"

        frame_botones=Frame(ventana)
        frame_botones.pack()

        "------------------ Botones -----------------------"
        
        boton_opcion=Button(frame_botones,text="COTIZAR y CONTINUAR",command=self.opcion,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)

        boton_proforma=Button(frame_botones, text="PROFORMA", command=self.proforma,height=2,width=10,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)

        boton_cancelar=Button(frame_botones, text="CERRAR", command=(ventana.quit, ventana.destroy()) ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
    def Validar_formulario_completo(self):
        if len(self.opcion.get()) !=0:
            self.raiz.destroy()
            ventana=Tk()
            application=Operacion()
            ventana.mainloop()
            return True
        else:
             messagebox.showerror("ERROR EN REGISTRO", "Complete todos los campos del formulario")

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


login()

print(mp[4][2])
print(acumulado_cantidad[5][3])

acumulado_cantidad[5][3] += 5
acumulado_cantidad[5][3] += 5

print(acumulado_cantidad[5][3])
