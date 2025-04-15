import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati5 import Ui_MainWindow

class Main5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.maiormenor)

    def maiormenor(self):
        num1 = int(self.ui.lineEditNum.text())
        num2 = int(self.ui.lineEditNum_2.text())
        num3 = int(self.ui.lineEditNum_3.text())
        num4 = int(self.ui.lineEditNum_4.text())
        num5 = int(self.ui.lineEditNum_5.text())
        maior = num1
        menor = num1
        numeros = [num1, num2, num3, num4, num5]
        i = 1
        while i < len(numeros):
            if numeros[i] > maior:
                maior = numeros[i]
            if numeros[i] < menor:
                menor = numeros[i]
            i += 1

        self.ui.labelResposta.setText(f"Maior {maior}\nMenor {menor}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main5()
    window.show()
    sys.exit(app.exec_())
