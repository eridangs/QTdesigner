import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from formulario import Ui_MainWindow

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionNovo.triggered.connect(self.novo)
        self.ui.actionSair.triggered.connect(self.close)
     
    def salvar(self):
        nome = self.ui.lineEditNome.text()
        email = self.ui.lineEditEmail.text()
        idade = self.ui.lineEditIdade.text()
        
        if not nome or not email or not idade:
            QMessageBox.warning(self, "Atenção", "Por favor, preencha todos os campos.")
            return
        
        try:
            idade_int = int(idade)
            if idade_int < 18:
                QMessageBox.warning(self, "Atenção", "Você é menor de idade.")
                return
        except ValueError:
            QMessageBox.warning(self, "Atenção", "Idade deve ser um número válido.")
            return

        conteudo = f"Nome: {nome}\nE-mail: {email}\nIdade: {idade}"
        caminho = QFileDialog.getSaveFileName(self, "Salvar", "", "Text Files (*.txt)")[0]
        if caminho:
            try:
                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo:\n{str(e)}")
    
    def novo(self):
        self.ui.lineEditNome.clear()
        self.ui.lineEditEmail.clear()
        self.ui.lineEditIdade.clear()

    def abrir(self):
        caminho = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            try:
                with open(caminho, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                    # Parsear o conteúdo para preencher os campos
                    dados = {}
                    for linha in conteudo.split('\n'):
                        if ':' in linha:
                            chave, valor = linha.split(':', 1)
                            dados[chave.strip()] = valor.strip()
                    
                    # Preencher os campos com os dados lidos
                    self.ui.lineEditNome.setText(dados.get('Nome', ''))
                    self.ui.lineEditEmail.setText(dados.get('E-mail', ''))
                    self.ui.lineEditIdade.setText(dados.get('Idade', ''))
                    
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao abrir arquivo:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditorTexto()
    window.show()
    sys.exit(app.exec_())