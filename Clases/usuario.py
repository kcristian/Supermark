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