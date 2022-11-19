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