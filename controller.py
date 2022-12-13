from views import v_menu_admin
from views import v_inicioSesion
from views import v_cargar_producto
from views import v_modificar_producto
from views import v_ventas
from views import v_detalle_venta
from views import v_Registro
from model import Modelo
from tkinter import messagebox
from tkinter import Tk
from tkinter import messagebox
import datetime as dtt

class Ctrl_menu_admin:
    def __init__(self,model:Modelo,view:v_menu_admin,datos):
        self.admin=datos
        self.model=model
        self.view=view
        self.view.botonCargarProducto["command"]=self.mostrarVentanaCarga
        self.view.botonModificarProducto["command"]=self.mostrarVentanaUpdate
        self.view.botonVentas["command"]=self.mostrarVentanaVentas

    def mostrarVentanaCarga(self):
        root=Tk()
        v=v_cargar_producto(root)
        c=Ctrl_producto(self.model,v)
    def mostrarVentanaUpdate(self):
        root=Tk()
        v=v_modificar_producto(root)
        c=Ctrl_u_producto(self.model,v)
    def mostrarVentanaVentas(self):
        root=Tk()
        v=v_ventas(root)
        c=Ctrl_ventas(self.model,v)


class Ctrl_producto:
    def __init__(self,model:Modelo,view:v_cargar_producto):
        self.model=model
        self.view=view
        self.view.botoncrear["command"]=self.cargar_datos_producto

    def cargar_datos_producto(self):
        nombre=self.view.getNombreText()
        precio=self.view.getPrecioText()
        stock=self.view.getStockText()
        categoria=self.view.getCategoriaText()
        vencimiento=self.view.getVencimientoText()
        self.model.agregar_producto(nombre,precio,stock,categoria,vencimiento)
        print("se inserto: ",nombre,precio,stock,categoria,vencimiento)

class Ctrl_u_producto:
    def __init__(self,model:Modelo,view:v_modificar_producto):
        self.model=model
        self.view=view
        self.view.botonbuscar["command"]=self.buscar_producto
        self.view.botonmodificar["command"]=self.enviar_datos
        self.view.botonatras["command"]=self.saludar
        
    def buscar_producto(self):
        try:
            id=int(self.view.getIdText())
            resultado=self.model.buscar_un_producto(id)
            self.view.cargarCuadros(resultado[1],resultado[2],resultado[3],resultado[4],resultado[5]) 
        except:
            print("problema con la base de datos")
    def enviar_datos(self):
        try:
            self.model.actualizar_producto(self.view.getIdText(),self.view.getNombreText(),self.view.getPrecioText(),self.view.getStockText(),self.view.getCategoriaText(),self.view.getVencimientoText())
            self.view.limpiarCuadros()
            messagebox.showinfo(message="CAMBIOS GUARDADOS",title="Exito!")
        except:
            print("error al enviar los datos")
        
    def saludar(self):
        print("hola")
        
class Ctrl_ventas:
    def __init__(self,model:Modelo,view:v_ventas):
        self.model=model
        self.view=view
        self.cargar_ventas()
        self.view.botonbuscar["command"]=self.mostrarDetalle
        self.view.botonbuscarusuario["command"]=self.buscar_ventas_usuario

    def cargar_ventas(self):
        #self.view.limpiar_tabla()
        self.view.cargar_tabla_datos(self.model.dame_ventas())
    
    def buscar_ventas_usuario(self):
        self.id=self.view.getIdText()
        self.view.limpiar_tabla()
        self.view.cargar_tabla_datos(self.model.dame_ventas_usuario(int(self.id)))
    def mostrarDetalle(self):
        root=Tk()
        v=v_detalle_venta(root)
        c=Ctrl_detalle_venta(self.model,v,int(self.id))
        self.view.root.destroy()

class Ctrl_detalle_venta:
    def __init__(self,model:Modelo,view:v_detalle_venta,id_venta):
        print(id_venta)
        self.id_venta=id_venta
        self.model=model
        self.view=view
        self.view.botonaceptar["command"]=self.accionAceptar
        self.cargarVentana()

    def cargarVentana(self):
        venta=self.model.dame_una_venta(self.id_venta)
        self.view.setLabelVenta(2)
        self.view.setLabelFecha("2025-12-10")
        lista_registros=self.model.dame_detalle_venta(self.id_venta)
        total=0
        for registro in lista_registros:
            total+=float(registro[3])
        self.view.setLabelTotal(total)
        self.view.CargarDatosTabla(lista_registros)

    def accionAceptar(self):
        self.view.root.destroy()
###################
###################
class Controlador_Sesion:
    def __init__(self,model:Modelo,view:v_inicioSesion):
        self.model=model
        self.view=view
        self.view.botonInicio['command'] = self.iniciar
        self.view.botonSalir['command'] = self.eventoSalir
        self.view.botonRegistro['command'] = self.eventoRegistro ###
        #self.root=Tk()
        #self.root.mainloop()
    
    def iniciar(self):
        user=self.view.getUsernameText()
        contra=self.view.getContraText()
        #print(correo)
        #print(contra)
        #Extrae los datos a una lista de tuplas
        datos=list()
        datos=self.model.dame_usuario(user,contra)
        print(type(datos))
        
        try:
            if len(datos)!=0:
            
                rol=datos[4]
                print(rol)
                contraseña=datos[2]
                if contra==contraseña:
                    if rol==1:
                        #INGRESA A LA VENTANA DEL CLIENTE}
                        print("CLIENTE")
                    else:
                        #INGRESA A LA VENTANA DEL ADMIN
                        print("ADMIN")
                        root=Tk()
                        v=v_menu_admin(root)
                        Ctrl_menu_admin(self.model,v,datos)
                        self.view.root.destroy()
                else:
                    self.view.cuadroContraTextVar.set("")
                    self.view.lblMensaje.config(text="CONTRASEÑA INCORRECTA")
        except:
            self.view.cuadroUsernameTextVar.set("")
            self.view.cuadroContraTextVar.set("")
            self.view.lblMensaje.config(text="CORREO NO VALIDO")
            
    def eventoSalir(self):
        self.view.root.destroy()

    def eventoRegistro(self):
        #   VENTANAS
        root=Tk()
        v=v_Registro(root)
        c=Controlador_registro(self.model,v)
        #self.registro=self.view.v_Registro()
        self.view.root.destroy()
        #v.botonRegistro['command'] = self.eventoRegistrarse
        #v.botonRegresar['command'] = self.volverVentanaInicioSesion

class Controlador_registro:
    def __init__(self,model:Modelo ,view:v_Registro):
        self.model=model
        self.view=view
        self.view.botonRegistro['command']=self.eventoRegistrarse
        #self.view.botonRegresar['command']=self.volverVentanaInicioSesion

    def eventoRegistrarse(self):

        nombre=self.view.getUsername()
        contra=self.view.getContra()
        correo=self.view.getCorreo()
        telefono=self.view.getTelefono()
        direccion=self.view.getDireccion()

        # REALIZA LA CONSULTA PARA LA BASE DE DATOS

        #consulta="SELECT * FROM Usuario where correo = '%s';"%(correo)
        #datos=self.baseDatos.datos(consulta)
        print(nombre)
        print(contra)
        print(correo)
        print(telefono)
        print(direccion)

        datos=self.model.usuario_email(correo)
        print(datos)
        if len(datos)==0:
            self.view.setMensajeCorreo("CORREO VALIDO")
            fecha=dtt.date.today()
            #self.model.cargar_usuario(nombre,contra,fecha,1,correo,telefono,direccion)
            
            self.view.root.after(2000,self.textoRegistroExitoso)
            self.view.root.after(4000,self.destruirVentana)
            #messagebox.showinfo(message="Registro exitoso",title="Exito")
        else:
            self.textoRegistroNoExitoso()
       
    def textoRegistroExitoso(self):
        self.view.setMensajeCorreo("Registro exitoso")
    def textoRegistroNoExitoso(self):
        self.view.setMensajeCorreo2("Registro fallido")
    #   Metodo necesario para el retorno a la ventan de inicio sesion y cerrando a la vez la ventana de registro
    def destruirVentana(self):
        self.view.root.destroy()
   

