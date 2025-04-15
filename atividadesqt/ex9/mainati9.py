import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati9 import Ui_MainWindow

class Main9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.palindromo)

    def palindromo(self):
        
        p = self.ui.lineEditNum.text()
        if p == p[::-1]:
            palavra = "Palíndromo."
        else:
            palavra = "Não é palíndromo."
        self.ui.labelResposta.setText(f"Resultado: {palavra}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main9()
    window.show()
    sys.exit(app.exec_())