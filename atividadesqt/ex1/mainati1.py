import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati1 import Ui_MainWindow

class Main1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.fatorial)

    def fatorial(self):
        num = int(self.ui.lineEditNum.text())
        fatorial = 1
        for i in range(1, num + 1):
            fatorial *= i
        self.ui.labelResult.setText(f"Fatorial : {fatorial}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main1()
    window.show()
    sys.exit(app.exec_())