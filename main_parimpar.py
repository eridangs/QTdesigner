import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from par_impar import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_enviar.clicked.connect(self.verificar_numero)

    def verificar_numero(self):
        numero = int(self.ui.lineEdit_num.text())
        if numero % 2 == 0:
            self.ui.label_resposta.setText(f'O número é PAR!')
        else:
            self.ui.label_resposta.setText(f'O número é IMPAR!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())