from controller import Ctrl_producto
from controller import Ctrl_u_producto
from controller import Ctrl_ventas
from controller import Controlador_Sesion
from model import Modelo
from views import v_cargar_producto
from views import v_modificar_producto
from views import v_ventas
from views import v_inicioSesion
from tkinter import *

if __name__=="__main__":
    root=Tk()
    vista=v_inicioSesion(root)
    modelo=Modelo()
    controlador=Controlador_Sesion(modelo,vista)
    root.mainloop()
