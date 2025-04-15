import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati8 import Ui_MainWindow

class Main8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.lista)

    def lista(self):
        lista = [1, 2, 3, 4]
        n = int(self.ui.lineEditNum.text())
        lista.append(n)
        lista.reverse()
        self.ui.labelResposta.setText(f"Lista invertida: {lista}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main8()
    window.show()
    sys.exit(app.exec_())