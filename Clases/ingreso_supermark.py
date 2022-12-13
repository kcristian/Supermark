import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class vista_ingreso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Clases\ingreso_supermark.ui",self)
if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI=vista_ingreso()
    GUI.show()
    sys.exit(app.exec_())