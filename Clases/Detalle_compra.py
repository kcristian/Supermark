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
        respuesta= self.getProducto().getDescripcion()+" ------ "+str(self.getCantidad())+" ------ $"+str(self.getProducto().getPrecio())+" ------ $"+str(self.getSubtotal())
        return respuesta