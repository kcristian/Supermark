class Categoria():
    def __init__(self,codigo,nombre):
        self.__codigo=codigo
        self.__nombre=nombre
    #getter y setter
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    
    def setCodigo(self,codigo):
        self.__codigo=codigo
    def setNombre(self,nombre):
        self.__nombre=nombre

    def __str__(self):        
        respuesta=" categoria: "+self.getNombre()+"\n"
        return respuesta