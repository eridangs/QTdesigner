import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from nome import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_exibir.clicked.connect(self.exibir_nome)

    def exibir_nome(self):
        nome = self.ui.lineEdit_nome.text()
        idade = self.ui.lineEdit_idade.text()
        self.ui.label_resposta.setText(f"Nome: {nome}\nIdade: {idade}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
