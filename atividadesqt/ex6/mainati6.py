import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati6 import Ui_MainWindow

class Main6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.ehprimo)

    def ehprimo(self):
        num = int(self.ui.lineEditNum.text())
        if num <= 1:
            valor = "não é primo."
        else:
            for i in range(2, num):
                if num % i == 0:
                    valor = "não é primo."
                    break
            else:
                valor = "é primo."
        self.ui.labelResposta.setText(f"Número: {valor}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main6()
    window.show()
    sys.exit(app.exec_())
