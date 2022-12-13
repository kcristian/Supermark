from enum import Enum,auto
#CLASE ROL
class Rol(Enum):
    CLIENTE=auto()
    ADMINISTRADOR=auto()
    DIRECCION=auto()
    STAFF=auto()
#CLASE USUARIO
class Usuario():
    def __init__(self,id,username,password,fecha_registro,rol,email,telefono,direccion):
        self.__user_id=id
        self.__username=username
        self.__password=password
        self.__fecha_reg=fecha_registro
        self.__rol=rol
        self.__email=email
        self.__telefono=telefono
        self.__direccion=direccion
    #getters y setters
    def getId(self):
        return self.__user_id
    def getUsername(self): 
        return self.__username
    def getPassword(self):
        return self.__password
    def getFechaRegistro(self):
        return self.__fecha_reg
    def getRol(self):
        return self.__rol
    def getEmail(self):
        return self.__email
    def getTelefono(self):
        return self.__telefono
    def getDireccion(self):
        return self.__direccion

    def setId(self,id):
        self.__user_id=id
    def setUsername(self,username):
        self.__username=username
    def setPassword(self,password):
        self.__password=password
    def setFechaRegistro(self,fecha_r):
        self.__fecha_reg=fecha_r
    def setRol(self,rol):
        self.__rol=rol
    def setEmail(self,email):
        self.__email=email
    def setTelefono(self,telefono):
        self.__telefono=telefono
    def setDireccion(self,direccion):
        self.__direccion=direccion
    
    def __str__(self):
        respuesta="userid: "+str(self.getId())+"\n"
        respuesta+="username: "+self.getUsername()+"\n"
        respuesta+="password: "+self.getPassword()+"\n"
        respuesta+="fecha de registro: "+str(self.getFechaRegistro())+"\n"
        respuesta+="rol: "+str(self.getRol())+"\n"
        respuesta+="email: "+self.getEmail()+"\n"
        respuesta+="telefono: "+self.getTelefono()+"\n"
        respuesta+="direccion: "+self.getDireccion()+"\n"
        return respuesta
#CLASE PRODUCTO
class Producto():
    def __init__(self,codigo,descripcion,precio,stock,categoria,fecha_venc):
        self.__codigo=codigo
        self.__descripcion=descripcion
        self.__precio=precio
        self.__stock=stock
        self.__peso=0
        self.__categoria=categoria
        self.__fecha_venc=fecha_venc
    #setter y getters
    def getCodigo(self):
        return self.__codigo
    def getDescripcion(self):
        return self.__descripcion
    def getPrecio(self):
        return self.__precio
    def getStock(self):
        return self.__stock
    def getPeso(self):
        return self.__peso
    def getCategoria(self):
        return self.__categoria
    def getFechavenc(self):
        return self.__fecha_venc
    
    def setCodigo(self,codigo):
        self.__codigo=codigo
    def setDescripcion(self,descripcion):
        self.__descripcion=descripcion
    def setPrecio(self,precio):
        self.__precio=precio
    def setStock(self,stock):
        self.__stock=stock
    def setPeso(self,peso):
        self.__peso=peso
    def setCategoria(self,categoria):
        self.__categoria=categoria
    def setFecha(self,fecha):
        self.__fecha_venc=fecha

    def __str__(self):
        respuesta= "informacion de producto:\n"
        respuesta+= "codigo: "+ str(self.getCodigo()) + "\n"
        respuesta+= "descripcion: "+ self.getDescripcion() + "\n"
        respuesta+= "precio: "+ str(self.getPrecio()) + "\n"
        respuesta+= "stock: "+ str(self.getStock()) + "\n"
        respuesta+= "peso: "+ str(self.getPeso()) + "\n"
        respuesta+= "categoria: "+ self.getCategoria().getNombre() + "\n"
        respuesta+= "fecha de vencimiento: "+ str(self.getFechavenc()) + "\n"
        return respuesta

#CLASE LINEA DE COMPRA       
class DetalleCompra():
    def __init__(self,producto,cantidad):
        self.__producto=producto
        self.__cantidad=cantidad
        
    #getters y setters
    def getProducto(self):
        return self.__producto
    def getCantidad(self):
        return self.__cantidad
    def getSubtotal(self):
        return self.getProducto().getPrecio()*self.getCantidad()
    
    def setProducto(self,producto):
        self.__producto=producto
    def setCantidad(self,cantidad):
        self.__cantidad=cantidad
    
    def __str__(self):
        respuesta= self.getProducto().getDescripcion()+" ------ "+str(self.getCantidad())+" ------ $"+str(self.getProducto().getPrecio())+" ------ $"+str(self.getSubtotal())+"\n"
        return respuesta
#CLASE COMPRA
class Compra:
    def __init__(self,usuario,fecha):
        self.__usuario=usuario
        self.__fecha_compra=fecha
        self.__lista_productos=list()
    def getusuario(self):
        return self.__usuario
    def getFecha(self):
        return self.__fecha_compra
    def setUsuario(self,usuario):
        self.__usuario=usuario
    def setFecha_compra(self,fecha):
        self.__fecha_compra=fecha
    def getLista_producto(self):
        return self.__lista_productos
    def agregar_linea(self,producto,cantidad):
        linea=DetalleCompra(producto,cantidad)
        self.__lista_productos.append(linea)
    def eliminar_linea(self,producto,cantidad):
        for elemento in self.getLista_producto():
            if elemento.getProducto().getCodigo()==producto.getProducto().getCodigo():
                self.getLista_producto().remove(elemento)
    def Calcular_Total(self):
        total=0
        for elemento in self.getLista_producto():
            total+=elemento.getSubtotal()
        return total
    
    