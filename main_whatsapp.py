import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
from whatsapp import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.abrir_whatsapp)

    def abrir_whatsapp(self):
        whatsapp_link = "https://dontpad.com/143desktop"
        webbrowser.open(whatsapp_link)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())