import random
import string
from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox


def gerar_senha(self):

    if self.tamanho_senha.value() <= 0:
        return ""
    else:
        if self.Masc.isChecked():
            self.senha += string.ascii_uppercase
        if self.Minsc.isChecked():
            self.senha += string.ascii_lowercase
        if self.Nums.isChecked():
            self.senha += string.digits
        if self.Simbs.isChecked():
            self.senha += string.punctuation
        if not self.senha:
            return ""
        else:
            senha_gerada = "".join(
                random.choice(self.senha) for _ in range(self.tamanho_senha.value())
            )
            return senha_gerada


def copiar_senha(self, senha_gerada):
    self.campo_senha = self.findChild(QLineEdit, "lineEdit_password")
    clipboard = QApplication.clipboard()
    clipboard.setText(senha_gerada)  # type: ignore
    msg = QMessageBox()
    msg.setWindowTitle("Senha Copiada")
    msg.setText("Senha copiada para a área de transferência!")
    msg.exec_()
