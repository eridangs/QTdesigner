import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculadora import Ui_MainWindow

class MainCalculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonCalcular.clicked.connect(self.calcular)

    def calcular(self):
        num1 = float(self.ui.lineEditNum1.text())
        num2 = float(self.ui.lineEditNum2.text())
        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        divisao = num1 / num2
        self.ui.labelResultado.setText(f"Soma: {soma} \nSubtração: {subtracao} \nMultiplicação: {multiplicacao} \nDivisão: {divisao}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainCalculadora()
    window.show()
    sys.exit(app.exec_())