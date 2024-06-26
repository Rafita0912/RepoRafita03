import materiales
import inicializa

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image

import sqlite3

mp = materiales.materia_prima() # lista de precios de materia prima
acumula = inicializa.iniciar() #inicializacion a 0 de todas las materias primas


"""
FORMULARIO DE REGISTRO DE OBRA Y CLIENTE
"""
class Registro:

    db_name='database_proyecto.db'
    
    def __init__(self, ventana1):
        self.window=ventana   
        self.window.title("REGISTRO DE DATOS")
        self.window.geometry("393x580")
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
        self.observaciones=Entry(marco,width=25,show="*")
        self.observaciones.grid(row=5, column=1, padx=10, pady=3)
        obs = self.observaciones

        label_password=Label(marco,text="Contraseña : ",font=("Comic Sans", 10,"bold")).grid(row=6,column=0,sticky='s',padx=10,pady=3)
        self.password=Entry(marco,width=25,show="*")
        self.password.grid(row=6, column=1, padx=10, pady=3)
        con = self.password

        "--------------- Frame botones --------------------"

        frame_botones=Frame(ventana)
        frame_botones.pack()

        "------------------ Botones -----------------------"
        
        boton_registrar=Button(frame_botones,text="REGISTRAR Y COTIZAR",command=self.Registrar_usuario ,height=2,width=20,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        #boton_limpiar=Button(frame_botones,text="LIMPIAR",command=self.Limpiar_formulario ,height=2,width=10,bg="gray",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_cancelar=Button(frame_botones,text="CERRAR",command=ventana.quit ,height=2,width=10,bg="red",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
    def Validar_formulario_completo(self):
        if len(self.obra.get()) !=0 and len(self.cliente.get()) !=0 and len(self.telefono.get()) !=0 and len(self.direccion.get()) !=0 and len(self.correo.get()) !=0 and len(self.observaciones.get()) !=0 and len(self.password.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR EN REGISTRO", "Complete todos los campos del formulario")

    def Validar_contraseña(self):
        if(str(self.password.get()) == "rafita"):
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "Contraseña no coincide")
    def Limpiar(self):
        self.obra.delete(0, END)
        self.cliente.delete(0, END)
        self.telefono.delete(0, END)
        self.direccion.delete(0, END)
        self.correo.delete(0, END)
        self.observaciones.delete(0, END)
        self.password.delete(0, END)

    def Registrar_usuario(self):
        if self.Validar_formulario_completo() and self.Validar_contraseña():
            query='INSERT INTO Usuarios VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.obra.get(),self.cliente.get(),self.telefono.get(),self.direccion.get(),self.correo.get(),self.observaciones.get(),self.password.get())
            self.Limpiar()
            self.window.destroy()
            Opciones()


ventana=Tk()
application=Registro(ventana)
ventana.mainloop()
#if __name__ == '__main__':
#    ventana=Tk()
#    application=Registro(ventana)
#    ventana.mainloop()


#for mppv in materiales.materia_prima():
#    print(mppv[2], " = ", mppv[4], " $us x ", mppv[3])

print(mp[4][3])

acumula[5][3] += 5
acumula[5][3] += 5

#for acu in acumulado.acum():
#    print(acu)

print(acumula[5][3])

#for acu in acumula:
#    if acu[3] != 0:
#        print(acu[0], " - ",acu[2], " = ",acu[3], " ", acu[4])

def fijo(base, altura, cantidad, color, espesor, esmerilado, phorizontal):

    return precio_unit, precio_final, mt2, precio_mt2;

def fachada(base, altura, cantidad, color, espesor, tipo, esmerilado, pvertical, phorizontal):

    return precio_unit, precio_final, mt2, precio_mt2;

def corrediza(base, altura, cantidad, color, espesor, tipo, hojas, esmerilado):
    
    return precio_unit, precio_final, mt2, precio_mt2;

def puerta(base, altura, cantidad, color, espesor, tipo, esmerilado, freno):

    return precio_unit, precio_final, mt2, precio_mt2;

