import sys
from PyQt5 import QtWidgets,QtSql,uic 
from PyQt5.uic import loadUi
from Clases.supermark import *
import sqlite3

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Clases/ingreso_supermark.ui",self)
        
        self.datos=Datos("Clases/supermark.sqlite")
        self.setupUiComponents()

    def setupUiComponents(self):
        self.btningresar.clicked.connect(self.f_login)
    def f_login(self):
        usuario=self.txtusuario.text()
        passsword=self.txtpass.text()
        print(usuario,passsword)

        self.datos.traer_usuario(usuario,passsword)
def main():
    #app=QtWidgets.QApplication(sys.argv)

    #form=Login()
    #form.show()
    #app.exec_()
    con=sqlite3.connect('supermark.sqlite')
    cur=con.cursor()
    cur.execute(f"SELECT * FROM Productos")
    resultado=cur.fetchall()
    print(resultado)
    con.commit()
    
if __name__=='__main__':
    main()
