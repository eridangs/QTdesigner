import sys
import os #importado
from PyQt5.QtCore import QUrl #importado
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent #importado
from PyQt5.QtWidgets import QApplication, QMainWindow
from reprodutormusical import Ui_MainWindow

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = QMediaPlayer(self)

        self.ui.pushButton_play.clicked.connect(self.reprodutormusical)
        self.ui.pushButton_stop_1.clicked.connect(self.parar)
        self.ui.pushButton_play_2.clicked.connect(self.reprodutormusical2)
        self.ui.pushButton_stop_2.clicked.connect(self.parar)
        self.ui.pushButton_play_3.clicked.connect(self.reprodutormusical3)
        self.ui.pushButton_stop_3.clicked.connect(self.parar)

    def parar(self):
        self.player.stop()
        print("A musica parou!")

    def reprodutormusical (self):
        caminho_music = os.path.abspath("Kiss.mp3")
        print("Local da música: ",caminho_music)
        url = QUrl.fromLocalFile(caminho_music)
        if url.isValid():
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            print("Tocando música...")
        else:
            print("Erro: Caminho do arquivo inválido.")

    def reprodutormusical2 (self):
        caminho_music = os.path.abspath("Epic.mp3")
        print("Local da música: ",caminho_music)
        url = QUrl.fromLocalFile(caminho_music)
        if url.isValid():
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            print("Tocando música...")
        else:
            print("Erro: Caminho do arquivo inválido.")

    def reprodutormusical3 (self):
        caminho_music = os.path.abspath("Djonga.mp3")
        print("Local da música: ",caminho_music)
        url = QUrl.fromLocalFile(caminho_music)
        if url.isValid():
            self.player.setMedia(QMediaContent(url))
            self.player.play()
            print("Tocando música...")
        else:
            print("Erro: Caminho do arquivo inválido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())
