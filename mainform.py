import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from formulario import Ui_MainWindow

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
# Conectando as ações aos métodos
        self.ui.actionNovo.triggered.connect(self.novo_form)

        self.ui.actionAbrir.triggered.connect(self.abrir_form)

        
        self.ui.pushButtonLimpa.clicked.connect(self.limpar_form)

        self.ui.pushButtonSalva.clicked.connect(self.salvar_form)


        self.ui.actionSair.triggered.connect(self.close)


    def novo_form(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    def limpar_form(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    def salvar_form(self):
        caminho = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'w', encoding='utf-8') as f:
                f.write(self.ui.lineEdit.text()) ('\n')
                f.write(self.ui.lineEdit_2.text()) ('\n')
                f.write(self.ui.lineEdit_3.text())

    def abrir_form(self):
        caminho = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            with open(caminho, 'r', encoding='utf-8') as f:
                self.ui.lineEdit.setText(f.read())
                self.ui.lineEdit_2.setText(f.read())
                self.ui.lineEdit_3.setText(f.read())



