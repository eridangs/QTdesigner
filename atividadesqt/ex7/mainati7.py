import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati7 import Ui_MainWindow

class Main7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.fibonnaci)

    def fibonnaci(self):
        n = int(self.ui.lineEditNum.text())
        a, b = 0, 1
        fibonnaci = []
        for _ in range(8):
            fibonnaci.append(a)
            a, b = b, a + b

        self.ui.labelResposta.setText(f"Sequencia: {fibonnaci}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main7()
    window.show()
    sys.exit(app.exec_())
