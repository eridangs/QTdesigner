import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati4 import Ui_MainWindow

class Main4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.regressiva)

    def regressiva(self):
        n = int(self.ui.lineEditNum.text())
        regressiva = []
        while n > 0:
            regressiva.append(n)
            n -= 1
        self.ui.labelResult.setText(f"Contagem regressiva: {regressiva}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main4()
    window.show()
    sys.exit(app.exec_())
