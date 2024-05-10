import sqlite3

con = sqlite3.connect("baseprueba.db")
cur = con.cursor()

# CREAR UNA BASE DE DATOS DESDE PYTHON
#cur.execute("CREATE TABLE Usuarios (ID INT PRIMARY KEY NOT NULL, LOGIN CHAR(50) NOT NULL, NOMBRE CHAR(50) NOT NULL)")

#INSERTAR DATOS A UNA TABLA YA CREADA DESDE PYTHON
#cur.execute("INSERT INTO Usuarios (ID, LOGIN, NOMBRE) VALUES (10, 'DAVID', 'mAC cHICKEN')")

#BORRAR DATOS DE UNA TABLA YA CREADA Y CARGADA
#cur.execute("DELETE FROM Usuarios WHERE ID = 2")

#PEDIR UN CODIGO PARA RECUPERAR LA INFORMACION DE LA BASE DE DATOS
#id=float(input("Ingrese un ID:"))
#cursor=cur.execute("SELECT LOGIN, NOMBRE FROM Usuarios WHERE ID=?", (id, ))
#filas=cursor.fetchall()
#if len(filas)>0:
#    for fila in filas:
#        print(fila)
#else:
#    print("No existen artículos con un precio menor al ingresado.")


#RECUPERAR DATOS DE UNA TABLA YA CREADA T CARGADA
#cur.execute("SELECT ID, LOGIN, NOMBRE FROM Usuarios WHERE ID=3")

#cursor=conexion.execute("select codigo,descripcion,precio from articulos")
#for fila in cursor:
#    print(fila)


#3print(login)

con.commit()
con.close()