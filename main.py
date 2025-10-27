from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5 import uic
import sys


class Gerador(QMainWindow):
    ui_file = "layout.ui"

    def __init__(self):
        super().__init__()
        uic.loadUi(self.ui_file, self)
        self.setWindowTitle("Gerador de Senhas")

    


app = QApplication([])
janela = Gerador()
janela.show()
app.exec_()
