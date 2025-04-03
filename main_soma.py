import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from soma import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_calcular.clicked.connect(self.somar)

    def somar(self):
        num1 = float(self.ui.lineEdit_num1.text())
        num2 = float(self.ui.lineEdit_num2.text())
        resultado = num1 + num2
        self.ui.label_resposta.setText(f"{resultado}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())