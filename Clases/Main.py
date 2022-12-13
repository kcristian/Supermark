from Clases import *
from Clases.ingreso_supermark import vista_ingreso
from datetime import date
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

def main():
    # print("hola")
    # f=date(2022,12,10)
    # c=Categoria(1,"cereal")
    # p=Producto(10,"arroz perseguido 500 gr",120,200,c,f)
    # p2=Producto(11,"fideo matarazzo 500 gr",140,500,c,f)
    # detalle=DetalleCompra(p,7)
    # detalle2=DetalleCompra(p2,4)
    # #print(detalle)

    # user=Usuario(100,"cristian","argentina2022",date(2022,11,21),Rol.CLIENTE,"cristian@gmail.com","44853",'alvarado 1100')
    # carrito=list()
    # carrito.append(detalle)
    # carrito.append(detalle2)
    # compra=Compra(1,carrito,user)
    # print(compra)


    #mi_rol=Rol.STAFF
    #print(mi_rol)
    #print(mi_rol.value)

    app=QApplication(sys.argv)
    GUI=vista_ingreso()
    GUI.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()