import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ati10 import Ui_MainWindow

class Main10(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonEnviar.clicked.connect(self.listas)

    def listas(self):

        lista = [4, 1, 3, 9, 5]
        self.ui.labelLista.setText(f'Lista atual: {lista}')
        lista_crescente = sorted(lista)
        lista_decrescente = sorted(lista, reverse=True)
        self.ui.labelResposta.setText(f"Crescente: {lista_crescente}\nDecrescente: {lista_decrescente}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main10()
    window.show()
    sys.exit(app.exec_())