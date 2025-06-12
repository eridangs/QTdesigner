import sys
from PyQt5 import QtGui, QtWidgets
from pokemon import Ui_MainWindow

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_verificar.clicked.connect(self.verificar_resposta)

    def verificar_resposta(self):
        self.ui.label_img.setPixmap(QtGui.QPixmap("img/pikachu.png"))
        self.ui.label_img.setScaledContents(True)

        self.ui.radioButton_1.setStyleSheet(f"color: red")
        self.ui.radioButton_2.setStyleSheet(f"color: green")
        self.ui.radioButton_3.setStyleSheet(f"color: red")
        self.ui.radioButton_4.setStyleSheet(f"color: red")
    
                

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())