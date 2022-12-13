import sqlite3
import datetime as fecha
class Modelo:
    
    def __init__(self):
        self.con=sqlite3.connect('supermark.sqlite')
        self.cur=self.con.cursor()

    def agregar_producto(self,descripcion,precio,stock,categoria,vencimiento):
        self.cur.execute(f"INSERT INTO Productos VALUES(NULL,'{descripcion}',{precio},{stock},'{categoria}','{vencimiento}')")
        print(self.cur.fetchall())
        self.con.commit()

    def actualizar_producto(self,id,descripcion,precio,stock,categoria,vencimiento):
        self.cur.execute(f"UPDATE Productos SET descripcion='{descripcion}', precio={precio}, stock={stock}, categoria='{categoria}', fecha_vencimiento='{vencimiento}' WHERE id_producto={id}")
        #print("actualizado: ",self.cur.fetchall())
        self.con.commit()
    def eliminar_producto(self,id):
        self.cur.execute(f"DELTE FROM Productos WHERE id_producto={id}")
        print(self.cur.fetchall())
        self.con.commit()
    def dame_productos(self):
        self.cur.execute(f"SELECT * FROM Productos")
        resultado=self.cur.fetchall()
        print(resultado)
        self.con.commit()
        return resultado
    def buscar_un_producto(self,id):
        self.cur.execute(f"SELECT * FROM Productos WHERE id_producto={id}")
        resultado=self.cur.fetchone()
        print("se encontro: ",resultado)
        self.con.commit()
        return resultado 
    def dame_una_venta(self,id_venta):
        self.cur.execute(f"SELECT id_venta, fecha_venta FROM Ventas WHERE id_venta={id_venta}")
        resultado=self.cur.fetchone()
        self.con.commit()
        return resultado
    def dame_ventas(self):
        self.cur.execute(f"SELECT id_venta, Ventas.id_usuario, username, fecha_venta FROM Ventas INNER JOIN Usuarios ON Ventas.id_usuario=Usuarios.id_usuario")
        resultado=self.cur.fetchall()
        self.con.commit()
        return resultado
    def dame_ventas_usuario(self,id):
        self.cur.execute(f"SELECT id_venta, Ventas.id_usuario, username, fecha_venta FROM Ventas INNER JOIN Usuarios ON Ventas.id_usuario=Usuarios.id_usuario AND Ventas.id_usuario={id}")
        resultado=self.cur.fetchall()
        self.con.commit()
        return resultado
    def dame_detalle_venta(self,id):
        #devuelve registro de nombre,precio,cantidad y subtotal
        query="SELECT Productos.descripcion,Productos.precio,Ventas_productos.cantidad,Productos.precio * Ventas_productos.cantidad " 
        query+="FROM Productos INNER JOIN Ventas_productos ON Productos.id_producto=Ventas_productos.id_producto "
        query+=f"INNER JOIN Ventas ON Ventas.id_venta=Ventas_productos.id_venta WHERE Ventas.id_venta={id}"
        self.cur.execute(query)
        resutlado=self.cur.fetchall()
        self.con.commit()
        return resutlado

    def dame_usuario(self,user,pas):
        self.cur.execute(f"SELECT * FROM Usuarios WHERE username='{user}' AND password='{pas}'")
        resultado=self.cur.fetchone()
        self.con.commit()
        return resultado

    def usuario_email(self,email):
        self.cur.execute(f"SELECT * FROM Usuarios WHERE email='{email}'")
        resultado=self.cur.fetchall()
        self.con.commit()
        return resultado
    def cargar_usuario(self,username,password,fecha_reg,id_rol,email,telefono,direccion):
        self.cur.execute(f"INSERT INTO Usuarios VALUES(NULL,'{username}','{password}','{fecha_reg}',{id_rol},'{email}','{telefono}','{direccion}')")
        self.con.commit()
    
    def crear_venta(self,id_usuario,fecha):
        self.cur.execute(f"INSERT INTO Ventas VALUES(NULL,{id_usuario},'{fecha}')")
        self.con.commit()
    def borrar_venta(self,id):
        self.cur.execute(f"DELETE FROM Ventas WHERE id_venta= {id}")
        self.con.commit()
    #5,6
    def crear_detalle_venta(self,id_producto,id_venta,cantidad):
        self.cur.execute(f"INSERT INTO Ventas_productos VALUES(NULL,{id_producto},{id_venta},{cantidad})")
        self.con.commit()
m=Modelo()
res=m.dame_detalle_venta(5)
for elemento in res:
    print(elemento)


