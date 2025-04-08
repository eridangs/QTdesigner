import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati3 import Ui_MainWindow

class Main3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.tabuada)

    def tabuada(self):
        n = int(self.ui.lineEditNum.text())
        tabuada = []
        for i in range(1,11):
            result = n*i
            tabuada.append(result)
        self.ui.labelResult.setText(f"Tabuada: {tabuada}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main3()
    window.show()
    sys.exit(app.exec_())
