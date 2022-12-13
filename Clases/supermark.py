import sqlite3 as sql
from Clases.Clases_supermark import *
class Conexion_BD:
    def __init__(self,db):
        self.conexion=sql.connect(db)
        self.cursor=self.conexion.cursor()
    def ejecutar_consulta(self,consulta):
        #ejecuta una consulta a partir del parametro consulta(que es una cadena)
        self.conexion.execute(consulta)
    def commit(self):
        self.conexion.commit()
    def cerrar_conexion(self):
        self.conexion.close()
    def devuelve_datos(self,consulta):
        self.cursor.execute(consulta)
        datos=self.cursor.fetchall()
        return datos
    def devuelve_uno(self,consulta):
        self.cursor.execute(consulta)
        dato=self.cursor.fetchone()
        return dato
    
class DBManager:
    def __init__(self,url: str):
        self.url=url
    def _conectar(self):
        return sql.connect(self.url)
    def ejecutar_query(self,query: str):
        conn=self._conectar()
        cursor=conn.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
        conn.commit()
        conn.close()
        #print(type(result))
        return result
class Datos:
    def __init__(self,ruta):
        self.__db=DBManager(ruta)
    
    def DameUsuario(self,id):
        resultado=list()
        if type(id)==int and id>0:
            query=f"SELECT * FROM Usuarios WHERE id_usuario={id}"
            resultado=self.__db.ejecutar_query(query)
            print(resultado)
            #print(type(resultado))
        else:
            print("no se ingreso un id entero")
    def DameRoles(self):
        query=f"SELECT * FROM Rol"
        resultado=self.__db.ejecutar_query(query)
        print(resultado)
   
    #ABM ventas
    def crear_venta(self,id_usuario,fecha_venta):
        query=f"INSERT INTO Ventas VALUES(NULL,{id_usuario},{fecha_venta})"
        self.__db.ejecutar_query(query)
    def modificar_venta(self,id_usuario,fecha_venta):
        query=f"UPDATE Ventas SET id_usuario={id_usuario},fecha_venta='{fecha_venta}'"
        self.__db.ejecutar_query(query)
    def eliminar_venta(self,id_venta):
        query=f"DELETE FROM Ventas WHERE id_venta={id_venta}"
        self.__db.ejecutar_query(query)
    #ABM producto
    def crear_producto(self,descripcion,precio,stock,categoria,fecha_vencimiento):
        query=f"INSERT INTO Productos VALUES(NULL,'{descripcion}',{precio},{stock},'{categoria}','{fecha_vencimiento}')"
        self.__db.ejecutar_query(query)
    def modificar_producto(self,descripcion,precio,stock,cateogria,fecha_venc):
        query=f"UPDATE Productos(descripcion,precio,stock,categoria,fecha_vencimiento) VALUES({descripcion},{precio},{stock},{cateogria},{fecha_venc}))"
        self.__db.ejecutar_query(query)
    def eliminar_producto(self,id_producto):
        query=f"DELETE FROM Productos WHERE id_producto={id_producto}"
        self.__db.ejecutar_query(query)
    #ABM usuario
    def crear_usuario(self,id_usuario,username,password,fecha,id_rol,email,telefono,direccion):
        query=f"INSERT INTO Usuarios VALUES(NULL,{username},'{password}','{fecha}',{id_rol},'{email}','{telefono}','{direccion}')"
        self.__db.ejecutar_query(query)
    def modificar_usuario(self,id_usuario,username,password,fecha,id_rol,email,telefono,direccion):
        query=f"UPDATE Usuarios SET username='{username}', password='{password}', fecha_registro='{fecha}',id_rol={id_rol},email='{email}',telefono='{telefono}',direccion='{direccion}' WHERE id_usuario={id_usuario})"
        self.__db.ejecutar_query(query)
    def eliminar_usuario(self,id_usuario):
        query=f"DELETE FROM Usuario WHERE id_usuario={id_usuario}"
        self.__db.ejecutar_query(query)
    #ABM rol
    def crear_rol(self,nombre_rol):
        query=f"INSERT INTO Rol VALUES(NULL,{nombre_rol})"
        self.__db.ejecutar_query(query)
    def modificar_rol(self,id_rol,nombre_rol):
        query=f"UPDATE Rol SET nombre='{nombre_rol}' WHERE id_rol={id_rol}"
        self.__db.ejecutar_query(query)
    def eliminar_rol(self,id_rol):
        query=f"DELETE FROM Rol WHERE id_rol={id_rol}"
        self.__db.ejecutar_query(query)
    #ABM detalle_compra
    def crear_venta_producto(self,id_producto,id_venta,cantidad,precio):
        query=F"INSERT INTO Ventas_productos VALUES(NULL,'{id_producto}','{id_venta}','{cantidad}','{precio}')"
        self.__db.ejecutar_query(query)
    def eliminar_venta_producto(self,id):
        query=f"DELETE FROM Ventas_productos WHERE id_venta_producto={id}"
        self.__db.ejecutar_query(query)
    #BUSCAR USUARIO
    def traer_usuario(self,username,password):
        query=f"SELECT * FROM Usuarios WHERE username='{username}' AND password='{password}'"
        resultado=self.__db.ejecutar_query(query)
        if len(resultado)!=0:
            t=resultado[0]
            usuario=Usuario(int(t[0]),t[1],t[2],t[3],int(t[4]),t[5],t[6],t[7])
            return usuario
        else:
            print("no existe")



#ruta="C:/Users/INTEL/Documents/pythonProject/1000 programadores python/Proyecto Supermark/SQL/supermark.sqlite"
#d=Datos(ruta)

#db=Conexion_BD(ruta)

#t1="CREATE TABLE IF NOT EXISTS Productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT,descripcion TEXT,precio FLOAT,stock INTEGER,categoria TEXT,fecha_vencimiento TEXT)"
#t2="CREATE TABLE IF NOT EXISTS Rol(id_rol INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT)"
#t3="CREATE TABLE IF NOT EXISTS Usuarios(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT,fecha_registro TEXT,id_rol INTEGER,email TEXT,telefono TEXT,direccion TEXT, FOREIGN KEY (id_rol) REFERENCES Rol(id_rol))"
#t4="CREATE TABLE IF NOT EXISTS Ventas(id_venta INTEGER PRIMARY KEY AUTOINCREMENT, id_usuario INTEGER, fecha_venta TEXT, FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario))"
#t5="CREATE TABLE IF NOT EXISTS Ventas_productos(id_venta_producto INTEGER PRIMARY KEY AUTOINCREMENT, id_producto INTEGER,id_venta INTEGER,cantidad INTEGER,precio FLOAT, FOREIGN KEY (id_producto) REFERENCES Productos(id_producto),FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta))"

#d.DameRoles()

#i6="INSERT INTO Rol VALUES(NULL,'DIRECCION')"
#i7="INSERT INTO Rol VALUES(NULL,'ADMINISTRADOR')"
#i8="INSERT INTO Usuarios VALUES(NULL,'cristian9','0800','29-11-22',2,'cristian@gmail.com',4445,'mitren 700')"
#i9="INSERT INTO Usuarios VALUES(NULL,'danielc','0800','29-11-22',2,'daniel@supermark.com',911,'alvarado 555')"
#db.mostrar(x)

#db.commit()
#db.cerrar_conexion()

    
