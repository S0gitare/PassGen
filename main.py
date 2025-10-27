from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QSpinBox,
    QCheckBox,
)
from PyQt5 import uic
import utilsfunc


class Gerador(QMainWindow):
    ui_file = "layout.ui"

    def __init__(self):
        super().__init__()
        uic.loadUi(self.ui_file, self)
        self.setWindowTitle("Gerador de Senhas")

        # Campo do tamanho da senha
        self.tamanho_senha = self.findChild(QSpinBox, "spinBox_length")

        # CheckBox de Letras Maiúsculas
        self.Masc = self.findChild(QCheckBox, "checkBox_uppercase")

        # CheckBox de Letras Minúsculas
        self.Minsc = self.findChild(QCheckBox, "checkBox_lowercase")

        # CheckBox de Números
        self.Nums = self.findChild(QCheckBox, "checkBox_numbers")

        # CheckBox de Símbolos
        self.Simbs = self.findChild(QCheckBox, "checkBox_special")

        self.senha = ""

        btn_gerar = self.findChild(QPushButton, "pushButton_generate")
        btn_gerar.clicked.connect(
            lambda: self.lineEdit_password.setText(utilsfunc.gerar_senha(self))
        )
        self.campo_senha = self.findChild(QLineEdit, "lineEdit_password")
        btn_copiar = self.findChild(QPushButton, "pushButton_copy")
        btn_copiar.clicked.connect(
            lambda: utilsfunc.copiar_senha(self, self.campo_senha.text())
        )


app = QApplication([])
janela = Gerador()
janela.show()
app.exec_()
