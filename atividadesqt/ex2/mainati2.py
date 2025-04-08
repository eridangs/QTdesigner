import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati2 import Ui_MainWindow

class Main2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.soma)

    def soma(self):
        num = int(self.ui.lineEditNum.text())
        soma = sum(range(1, num + 1))
        self.ui.labelResult.setText(f"Soma dos numeros: {soma}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main2()
    window.show()
    sys.exit(app.exec_())
