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
        self.isPaused = False
        self.ui.horizontalSlider_volume.valueChanged.connect(self.controlar_volume)
        self.ui.pushButton_stop.clicked.connect(self.parar)
        self.ui.pushButton_pausar.clicked.connect(self.pausar)

        self.ui.pushButton_play.clicked.connect(self.play)
        self.ui.pushButton_play_2.clicked.connect(self.play2)
        self.ui.pushButton_play_3.clicked.connect(self.play3)
        self.ui.pushButton_play_4.clicked.connect(self.play4)
        self.ui.pushButton_play_5.clicked.connect(self.play5)

    def parar(self):
        self.player.stop()
        self.isPaused = False
        print("A musica parou!")

    def pausar(self):
        self.player.pause()
        self.isPaused = True
        print("A musica pausou!")

    def controlar_volume(self):
        volume = self.ui.horizontalSlider_volume.value()
        self.player.setVolume(volume)
        print(f"Volume ajustado para: {volume}")
    

    def play (self):
        caminho_music = os.path.abspath("Kiss.mp3")
        print("Local da música: ",caminho_music)
        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:

            url = QUrl.fromLocalFile(caminho_music)
            
            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")

            else:
                print("Erro: Caminho do arquivo inválido.")
    
    def play2 (self):
        caminho_music = os.path.abspath("Epic.mp3")
        print("Local da música: ",caminho_music)
        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:
        
            url = QUrl.fromLocalFile(caminho_music)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")

            else:
                print("Erro: Caminho do arquivo inválido.")

    def play3 (self):
        caminho_music = os.path.abspath("Djonga.mp3")
        print("Local da música: ",caminho_music)
        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:

            url = QUrl.fromLocalFile(caminho_music)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")

            else:
                print("Erro: Caminho do arquivo inválido.")

    def play4 (self):
        caminho_music = os.path.abspath("Quemnaoquersoueu.mp3")
        print("Local da música: ",caminho_music)
        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:

            url = QUrl.fromLocalFile(caminho_music)

            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando música...")

            else:
                print("Erro: Caminho do arquivo inválido.")
    
    def play5 (self):
        caminho_music = os.path.abspath("Tetodevidro.mp3")
        print("Local da música: ",caminho_music)
        if self.isPaused:
            self.player.play()
            self.isPaused = False

        else:

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
