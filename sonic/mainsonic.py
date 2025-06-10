import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from sonic import Ui_MainWindow
from PyQt5.QtGui import QPixmap

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.pushButton_sonic.clicked.connect(lambda:self.alterar_imagem("Sonic"))
        self.ui.pushButton_shadow.clicked.connect(lambda:self.alterar_imagem("Shadow"))
        self.ui.pushButton_amy.clicked.connect(lambda:self.alterar_imagem("Amy"))
        self.ui.pushButton_dr_eggman.clicked.connect(lambda:self.alterar_imagem("Dr. Eggman"))
        self.ui.pushButton_tails.clicked.connect(lambda:self.alterar_imagem("Tails"))
        self.ui.pushButton_knuckles.clicked.connect(lambda:self.alterar_imagem("Knuckles"))

    def alterar_imagem(self,nome_personagem):
        caminho_img = {
            "Sonic": "img/sonic.png",
            "Amy": "img/amy.png",
            "Tails": "img/tails.png",
            "Dr. Eggman": "img/eggman.png",
            "Shadow": "img/shadow.png",
            "Knuckles": "img/knuckles.png",
        }

        if nome_personagem in caminho_img:
            pixmap = QPixmap(caminho_img[nome_personagem])
            self.ui.label_PersonagemSelecionado.setPixmap(pixmap)
            self.ui.label_PersonagemSelecionado.setScaledContents(True)
        else:
            print(f"Imagem para {nome_personagem} não encontrada!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
