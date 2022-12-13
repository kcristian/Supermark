from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#MENU PRINCIPAL
class v_menu_admin():
    def __init__(self,root:Tk):
        self.root=root
        self.root.title("Menu Administrador")
        self.root.geometry("300x200")
        self.root.resizable(0,0)
        #self.root.eval("tk::PlaceWindow .  center")
        self.createwidgets()
    def createwidgets(self):
        miframe=Frame(self.root)
        miframe.pack()
        self.botonCargarProducto=Button(miframe,text="cargar producto",width=15,height=2)
        self.botonCargarProducto.grid(row=0,column=1,padx=5,pady=5)

        self.botonModificarProducto=Button(miframe,text="modificar producto",width=15,height=2)
        self.botonModificarProducto.grid(row=1,column=1,padx=5,pady=5)

        self.botonVentas=Button(miframe,text="ventas de usuario",width=15,height=2)
        self.botonVentas.grid(row=2,column=1,padx=5,pady=5)

        # self.botonDetalles=Button(miframe,text="detalles de compra",width=15,height=2)
        # self.botonDetalles.grid(row=3,column=1,padx=5,pady=5)

#CREAR PRODUCTO
class v_cargar_producto:
    def __init__(self,root:Tk):
        self.root=root
        self.root.title("Alta de producto")
        self.root.geometry("350x400")
        self.root.resizable(0,0)
        self.createWidgets()
    def createWidgets(self):
        miframe=Frame(self.root)
        miframe.pack()

        self.lblvacio=Label(miframe,text="INGRESO DEL NUEVO PRODUCTO",width=25,height=2)
        self.lblvacio.grid(row=0,column=2)
        self.lblvacio.anchor("e")

        #producto
        self.lblnombre=Label(miframe,text="nombre:",width=7,height=3)
        self.lblnombre.grid(row=1,column=1)

        self.cuadro1textvar=StringVar()
        self.cuadro1=Entry(miframe,textvariable=self.cuadro1textvar)
        self.cuadro1.grid(row=1,column=2)

        self.lblprecio=Label(miframe,text="precio:",width=7,height=3)
        self.lblprecio.grid(row=2,column=1)

        self.cuadro2textvar=StringVar()
        self.cuadro2=Entry(miframe,textvariable=self.cuadro2textvar)
        self.cuadro2.grid(row=2,column=2)
        
        self.lblstock=Label(miframe,text="stock:",width=7,height=3)
        self.lblstock.grid(row=3,column=1)
        
        self.cuadro3textvar=StringVar()
        self.cuadro3=Entry(miframe,textvariable=self.cuadro3textvar)
        self.cuadro3.grid(row=3,column=2)

        self.lblcategoria=Label(miframe,text="categoria:",width=7,height=3)
        self.lblcategoria.grid(row=4,column=1)

        self.cuadro4textvar=StringVar()
        self.cuadro4=Entry(miframe,textvariable=self.cuadro4textvar)
        self.cuadro4.grid(row=4,column=2)

        self.lblvencimiento=Label(miframe,text="vencimiento:",width=10,height=3)
        self.lblvencimiento.grid(row=5,column=1)

        self.cuadro5textvar=StringVar()
        self.cuadro5=Entry(miframe,textvariable=self.cuadro5textvar)
        self.cuadro5.grid(row=5,column=2)

        self.textonombre=Entry(miframe,)

        #botones
        miframe2=Frame(self.root)
        miframe2.pack()

        self.botonatras=Button(miframe2,text="atrás")
        self.botonatras.grid(row=1,column=1,sticky="e",padx=10,pady=10)

        self.botoncrear=Button(miframe2,text="crear")
        self.botoncrear.grid(row=1,column=2,sticky="e",padx=10,pady=10)
    def getNombreText(self):
        return self.cuadro1textvar.get()
    def getPrecioText(self):
        return self.cuadro2textvar.get()
    def getStockText(self):
        return self.cuadro3textvar.get()
    def getCategoriaText(self):
        return self.cuadro4textvar.get()
    def getVencimientoText(self):
        return self.cuadro5textvar.get()

#MODIFICAR PRODUCTO
class v_modificar_producto:
    def __init__(self,root:Tk):
        self.root=root
        self.root.title("modificar un producto")
        self.root.geometry("350x450")
        self.root.resizable(0,0)
        self.createWidgets()
    
    def createWidgets(self):
        miframe=Frame(self.root)
        miframe.pack()
        self.lblvacio=Label(miframe,text="MODIFICACION DE PRODUCTO",width=25,height=2)
        self.lblvacio.grid(row=0,column=2)
        self.lblvacio.anchor("e")
        
        self.lblmensaje=Label(miframe,text="ingrese id: ")
        self.lblmensaje.grid(row=1,column=1)

        self.cuadrotexto1textvar=StringVar()
        self.cuadrotexto1=Entry(miframe,textvariable=self.cuadrotexto1textvar)
        self.cuadrotexto1.grid(row=1,column=2)

        self.botonbuscar=Button(miframe,text="buscar",padx=5,pady=5)
        self.botonbuscar.grid(row=1,column=3)

        self.lblmensaje2=Label(miframe,text="datos del producto",width=25,height=3)
        self.lblmensaje2.grid(row=2,column=2)

        miframe2=Frame(self.root)
        miframe2.pack()

        ## nombre
        self.lblnombre=Label(miframe2,text="nombre: ",width=10,height=3)
        self.lblnombre.grid(row=1,column=1)

        self.cuadrotexto2textvar=StringVar()
        self.cuadrotexto2=Entry(miframe2,textvariable=self.cuadrotexto2textvar)
        self.cuadrotexto2.grid(row=1,column=2)

        ## precio
        self.lblprecio=Label(miframe2,text="precio: ",width=10,height=3)
        self.lblprecio.grid(row=2,column=1)

        self.cuadrotexto3textvar=StringVar()
        self.cuadrotexto3=Entry(miframe2,textvariable=self.cuadrotexto3textvar)
        self.cuadrotexto3.grid(row=2,column=2)

        ## stock
        self.lblstock=Label(miframe2,text="stock: ",width=10,height=3)
        self.lblstock.grid(row=3,column=1)

        self.cuadrotexto4textvar=StringVar()
        self.cuadrotexto4=Entry(miframe2,textvariable=self.cuadrotexto4textvar)
        self.cuadrotexto4.grid(row=3,column=2)

        # categoria
        self.lblcategoria=Label(miframe2,text="categoria: ",width=10,height=3)
        self.lblcategoria.grid(row=4,column=1)

        self.cuadrotexto5textvar=StringVar()
        self.cuadrotexto5=Entry(miframe2,textvariable=self.cuadrotexto5textvar)
        self.cuadrotexto5.grid(row=4,column=2)

        ## vencimiento
        self.lblvencimiento=Label(miframe2,text="vencimiento: ",width=10,height=3)
        self.lblvencimiento.grid(row=5,column=1)

        self.cuadrotexto6textvar=StringVar()
        self.cuadrotexto6=Entry(miframe2,textvariable=self.cuadrotexto6textvar)
        self.cuadrotexto6.grid(row=5,column=2)

        miframe3=Frame(self.root)
        miframe3.pack()
        
        self.botonatras=Button(miframe3,text="atras",padx=30)
        self.botonatras.grid(row=1,column=1)

        self.botonmodificar=Button(miframe3,text="guardar cambios")
        self.botonmodificar.grid(row=1,column=2,padx=30)
    #gets
    def getIdText(self):
        return self.cuadrotexto1textvar.get()
    def getNombreText(self):
        return self.cuadrotexto2textvar.get()
    def getPrecioText(self):
        return self.cuadrotexto3textvar.get()
    def getStockText(self):
        return self.cuadrotexto4textvar.get()
    def getCategoriaText(self):
        return self.cuadrotexto5textvar.get()
    def getVencimientoText(self):
        return self.cuadrotexto6textvar.get()

    #set
    def setIdText(self,id):
        self.cuadrotexto1textvar.set(id)
    def setNombreText(self,nombre):
        self.cuadrotexto2textvar.set(nombre)
    def setPrecioText(self,precio):
        self.cuadrotexto3textvar.set(precio)
    def setStockText(self,stock):
        self.cuadrotexto4textvar.set(stock)
    def setCategoriaText(self,cat):
        self.cuadrotexto5textvar.set(cat)
    def setVencimientoText(self,venc):
        self.cuadrotexto6textvar.set(venc)

    def cargarCuadros(self,nombre,precio,stock,categoria,vencimiento):
        self.setNombreText(nombre)
        self.setPrecioText(precio)
        self.setStockText(stock)
        self.setCategoriaText(categoria)
        self.setVencimientoText(vencimiento)

    def limpiarCuadros(self):
        self.setIdText("")
        
        self.setNombreText("")
        self.setPrecioText("")
        self.setStockText("")
        self.setCategoriaText("")
        self.setVencimientoText("")
    



#VENTAS
class v_ventas:
    def __init__(self,root: Tk):
        self.root=root
        self.root.title("Historial de ventas")
        self.root.geometry("850x400")
        #self.root.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        miframe=Frame(self.root)
        miframe.pack()

        self.labelusuario=Label(miframe,text="id de usuario: ",width=10,height=2)
        self.labelusuario.grid(row=1,column=1)

        self.cuadrotexto1var=StringVar()
        self.textousuario=Entry(miframe,textvariable=self.cuadrotexto1var)
        self.textousuario.grid(row=1,column=2,padx=4,pady=4)

        self.botonbuscarusuario=Button(miframe,width=10, text="buscar ventas")
        self.botonbuscarusuario.grid(row=1,column=3,padx=4,pady=4)

        miframe2=Frame(self.root)
        miframe2.pack()
        self.tablaventas=ttk.Treeview(miframe2,height=10, columns=('#1','#2','#3','#4')) 
        self.tablaventas.grid(row=3,column=0,columnspan=4)
        self.tablaventas['show']='headings'
        self.tablaventas.heading("#1",text="id venta",anchor=CENTER)
        self.tablaventas.heading("#2",text="id usuario",anchor=CENTER)
        self.tablaventas.heading("#3",text="username",anchor=CENTER)
        self.tablaventas.heading("#4",text="fecha",anchor=CENTER)
        self.tablaventas.bind("<Double -1>",self.click_tabla)

        #self.tablaventas.insert("",END,values=(1,12,"cristian","12-12-2022"))
        #self.tablaventas.insert("",END,values=(2,14,"daniel","13-12-2022"))

        miframe3=Frame(self.root)
        miframe3.pack()
        self.labelidventavalue=StringVar()
        self.labelidventavalue=""

        self.labelusernamevalue=""
        self.labelidusuariovalue=""
        self.labelfechavalue=""

        self.labelidventa=Label(miframe3,width=10,height=4, text=self.labelidventavalue)
        self.labelusername=Label(miframe3,width=10,height=4,text=self.labelusernamevalue)
        self.labelidusuario=Label(miframe3,width=10,height=4,text=self.labelidusuariovalue)
        self.labelfecha=Label(miframe3,width=10,height=4,text=self.labelfechavalue)

        self.labelidventa.grid(row=4,column=1)
        self.labelusername.grid(row=4,column=2)
        self.labelidusuario.grid(row=4,column=3)
        self.labelfecha.grid(row=4,column=4)

        miframe4=Frame(self.root)
        miframe4.pack()
        self.botonatras=Button(miframe4,width=10,text="ATRAS",padx=8,pady=3)
        self.labelespaciador=Label(miframe4,width=40)
        self.botonbuscar=Button(miframe4,width=10,text="BUSCAR",padx=8,pady=3)

        self.botonatras.grid(row=5,column=1)
        self.botonbuscar.grid(row=5,column=3)
        self.labelespaciador.grid(row=5,column=2)

    ##
    def getIdLabel(self):
        return self.labelidventavalue.get()
    def getIdText(self):
        return self.cuadrotexto1var.get()
    def click_tabla(self,event):
        item=self.tablaventas.selection()[0]
        valores=self.tablaventas.item(item)
        t=valores['values']

        self.labelidventa.config(text=t[0])
        
        self.labelusername.config(text=t[1])
        self.labelidusuario.config(text=t[2])
        self.labelfecha.config(text=t[3])

        #print("id venta:",valores['values'][0],"\nid usuario:",valores['values'][1]," \nusername:",valores['values'][2])
    #
    def limpiar_tabla(self):
        for i in self.tablaventas.get_children():
            self.tablaventas.delete(i)
    
    def cargar_tabla_datos(self,lista):
    #self.tablaventas.insert("",END,values=(1,12,"cristian","12-12-2022"))
        for elemento in lista:
            self.tablaventas.insert("",END,values=(elemento[0],elemento[1],elemento[2],elemento[3]))

class v_detalle_venta:
    def __init__(self,root:Tk):
        #self.id_venta=id_venta
        self.root=root
        self.root.title("Detalles de venta")
        self.root.geometry("550x400")
        self.root.resizable(0,0)
        self.createWidgets()
    def createWidgets(self):
        miframe=Frame(self.root)
        miframe.pack()
        self.labelmensaje1=Label(miframe,text="PRODUCTOS COMPRADOS",pady=5)
        self.labelmensaje1.grid(row=1,column=2)

        self.labelventa=Label(miframe,text="Nº Venta")
        self.labelventa.grid(row=2,column=0)
        self.labelfecha=Label(miframe,text="Fecha")
        self.labelfecha.grid(row=3,column=0)

        self.tabladetalle=ttk.Treeview(miframe,height=10,columns=('#1','#2','#3','#4'))
        self.tabladetalle.grid(row=4,column=0,columnspan=5)
        self.tabladetalle['show']='headings'
        self.tabladetalle.heading("#1",text="producto",anchor=CENTER)
        self.tabladetalle.heading("#2",text="precio",anchor=CENTER)
        self.tabladetalle.heading("#3",text="cantidad",anchor=CENTER)
        self.tabladetalle.heading("#4",text="subtotal",anchor=CENTER)
        self.tabladetalle.column("#2",stretch=NO,width=100)
        self.tabladetalle.column("#3",stretch=NO,width=100)
        self.tabladetalle.column("#4",stretch=NO,width=100)

        miframe2=Frame(self.root)
        miframe2.pack()
        self.labelmensajetotal=Label(miframe2,text="TOTAL: $", pady=5)
        self.labelmensajetotal.grid(row=2,column=0)
        self.labeltotal=Label(miframe2,text="X",pady=5)
        self.labeltotal.grid(row=2,column=1)

        self.botonaceptar=Button(miframe2,text="ACEPTAR",pady=5,padx=7)
        self.botonaceptar.grid(row=4,column=5)
    
    def setLabelVenta(self,id_venta):
        self.labelventa.config(text=id_venta)
    def setLabelFecha(self,fecha):
        self.labelfecha.config(text=fecha)
    def setLabelTotal(self,total):
        self.labeltotal.config(text=total)

    def CargarDatosTabla(self,lista):
        for registro in lista:
            self.tabladetalle.insert("",END,values=(registro[0],registro[1],registro[2],registro[3]))
    

### VentanaRegistro
#from tkinter import *

class v_inicioSesion:
    def __init__(self,root:Tk):
        self.root=root
        self.root.title("Inicio Sesion")
        self.root.geometry("300x270")
        self.root.resizable(0,0)
        #self.root.eval("tk::PlaceWindow .  center")
        self.creacionWidgets()
    def creacionWidgets(self):
        miframe=Frame(self.root)
        miframe.pack()
        #LABELS
        #   Correo
        self.lblUsername=Label(miframe,text="Username:",width=7,height=3)
        self.lblUsername.grid(row=1,column=1)

        self.cuadroUsernameTextVar=StringVar()
        self.cuadroUsername=Entry(miframe,textvariable=self.cuadroUsernameTextVar)
        self.cuadroUsername.grid(row=1,column=2)

        #   Mensaje de Correo erroneo
        self.lblMensaje=Label(miframe,text="",fg='red',width=15,height=3)
        self.lblMensaje.grid(row=2,column=1)

        #   Contraseña
        self.lblContra=Label(miframe,text="Contraseña:",width=9,height=3)
        self.lblContra.grid(row=3,column=1)

        self.cuadroContraTextVar=StringVar()
        self.cuadroContra=Entry(miframe,textvariable=self.cuadroContraTextVar,show='*')
        self.cuadroContra.grid(row=3,column=2)
        
        #BOTONES
        #   Boton Inicio sesion
        self.botonInicio=Button(miframe,text="Iniciar Sesion",width=15,height=2)
        self.botonInicio.grid(row=4,column=1,padx=5,pady=5)
        #self.botonInicio.
        #   Boton Registro
        self.botonRegistro=Button(miframe,text="Registro",width=15,height=2)
        self.botonRegistro.grid(row=4,column=2,padx=5,pady=5)
        #   Boton Salir
        aux=Frame(self.root)
        aux.pack()
        self.botonSalir=Button(aux,text="Salir",width=15,height=2)
        self.botonSalir.grid(row=1,column=2,padx=5,pady=5)

    def getUsernameText(self):
        return self.cuadroUsernameTextVar.get()
    def getContraText(self):
        return self.cuadroContraTextVar.get()
    def setMensajeCorreo(self,texto):
        self.lblMensaje.config(text=texto)

class v_Registro:
    def __init__(self,root:Tk):
        self.root=root
        self.root.title("Registro")
        self.root.geometry("300x380")
        self.root.resizable(0,0)
        #self.root.eval("tk::PlaceWindow .  center")
        self.creacionWidgets()
    def creacionWidgets(self):
        miframe=Frame(self.root)
        miframe.pack()
        # Username
        self.lblUsername=Label(miframe,text="Username:",width=7,height=3)
        self.lblUsername.grid(row=1,column=1)

        self.cuadroUsernameTextVar=StringVar()
        self.cuadroUsernameTextVar=Entry(miframe,textvariable=self.cuadroUsernameTextVar)
        self.cuadroUsernameTextVar.grid(row=1,column=2)

        #   Contraseña
        self.lblContra=Label(miframe,text="Contraseña:",width=9,height=3)
        self.lblContra.grid(row=2,column=1)

        self.cuadroContraTextVar=StringVar()
        self.cuadroContraTextVar=Entry(miframe,textvariable=self.cuadroContraTextVar)
        self.cuadroContraTextVar.grid(row=2,column=2)

        #   Correo
        self.lblCorreo=Label(miframe,text="Correo:",width=7,height=3)
        self.lblCorreo.grid(row=3,column=1)

        self.cuadroCorreoTextVar=StringVar()
        self.cuadroCorreoTextVar=Entry(miframe,textvariable=self.cuadroCorreoTextVar)
        self.cuadroCorreoTextVar.grid(row=3,column=2)

        #   Telefono
        self.lblTelefono=Label(miframe,text="Telefono:",width=7,height=3)
        self.lblTelefono.grid(row=4,column=1)

        self.cuadroTelefonoTextVar=StringVar()
        self.cuadroTelefonoTextVar=Entry(miframe,textvariable=self.cuadroTelefonoTextVar)
        self.cuadroTelefonoTextVar.grid(row=4,column=2)
        
         #   Direccion
        self.lblDireccion=Label(miframe,text="Direccion:",width=7,height=3)
        self.lblDireccion.grid(row=5,column=1)

        self.cuadroDireccionTextVar=StringVar()
        self.cuadroDireccionTextVar=Entry(miframe,textvariable=self.cuadroDireccionTextVar)
        self.cuadroDireccionTextVar.grid(row=5,column=2)

        #   Nombre
        # self.lblNombre=Label(miframe,text="Nombre:",width=7,height=3)
        # self.lblNombre.grid(row=3,column=1)

        # self.cuadroNombreTextVar=StringVar()
        # self.cuadroNombre=Entry(miframe,textvariable=self.cuadroNombreTextVar)
        # self.cuadroNombre.grid(row=3,column=2)
        #   Apellido
        # self.lblApellido=Label(miframe,text="Apellido:",width=7,height=3)
        # self.lblApellido.grid(row=4,column=1)

        # self.cuadroApellidoTextVar=StringVar()
        # self.cuadroApellido=Entry(miframe,textvariable=self.cuadroApellidoTextVar)
        # self.cuadroApellido.grid(row=4,column=2)

        #   MENSAKE DE CORREO VALIDO/INVALIDO
        self.lblMensajeCorreo=Label(miframe,text="",fg='green',width=13,height=3)
        self.lblMensajeCorreo.grid(row=7,column=1)

        self.lblMensajeCorreo2=Label(miframe,text="",fg='red',width=13,height=3)
        self.lblMensajeCorreo2.grid(row=7,column=2)

        #BOTONES
        #   Boton Registro
        self.botonRegistro=Button(miframe,text="Registrarse",width=15,height=2)
        self.botonRegistro.grid(row=8,column=2,padx=5,pady=5)
        #   Boton Regresar
        #self.botonRegresar=Button(miframe,text="Regresar",width=15,height=2)
        #self.botonRegresar.grid(row=8,column=2,padx=5,pady=5)
    def getUsername(self):
        return self.cuadroUsernameTextVar.get()    
    def getCorreo(self):
        return self.cuadroCorreoTextVar.get()
    def getContra(self):
        return self.cuadroContraTextVar.get()
    # def getNombre(self):
    #     return self.cuadroNombreTextVar.get()
    # def getApellido(self):
    #     return self.cuadroApellidoTextVar.get()
    def getDireccion(self):
        return self.cuadroDireccionTextVar.get()
    def getTelefono(self):
        return self.cuadroTelefonoTextVar.get()

    def setMensajeCorreo(self,mensaje):
        self.lblMensajeCorreo.config(text=mensaje)
    def setMensajeCorreo2(self,mensaje):
        self.lblMensajeCorreo2.config(text=mensaje)
    def limpiarCuadroCorreo(self):
        self.cuadroCorreoTextVar.set("")

if __name__=='__main__':
    root=Tk()
    #view=v_inicioSesion(root)
    view=v_Registro(root)
    #view=v_menu_admin(root)
    #view=v_cargar_producto(root)
    #view=v_modificar_producto(root)
    #view=v_ventas(root)
    #view=v_detalle_venta(root)
    root.mainloop()