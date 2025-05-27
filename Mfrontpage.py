import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow
from frontpage import Ui_MainWindow

class link(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(self.abrir_whatsapp)
        self.ui.pushButton_2.clicked.connect(self.abrir_instagram)
        self.ui.pushButton_3.clicked.connect(self.abrir_github)
        self.ui.pushButton_4.clicked.connect(self.abrir_linkedin)

    def abrir_whatsapp(self):
        whatsapp_link = "https://wa.me/67991234567"
        webbrowser.open(whatsapp_link)
    def abrir_instagram(self):
        instagram_link = "https://www.instagram.com/eridangsl/"
        webbrowser.open(instagram_link)
    def abrir_github(self):
        github_link = "https://www.linkedin.com/in/lara-eridan-genes-santiago/"
        webbrowser.open(github_link)
    def abrir_linkedin(self):
        linkedin_link = "https://github.com/eridangs"
        webbrowser.open(linkedin_link)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = link()
    window.show()
    sys.exit(app.exec_())
