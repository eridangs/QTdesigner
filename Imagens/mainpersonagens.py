import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from personagens import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonLimpar.clicked.connect(self.limpar)
        
    def salvar(self):
        nomeCompleto = self.ui.lineEditNome.text()
        nomeUsuario = self.ui.lineEditUser.text()
        email = self.ui.lineEditEmail.text()
        senha = self.ui.lineEditSenha.text()
        idade = int(self.ui.lineEditIdade.text())
        personagem = "Pooh" if self.ui.radioButton.isChecked() else "Leitão" if self.ui.radioButton_2.isChecked() else "Tigrão" if self.ui.radioButton_3.isChecked() else "Coelho" if self.ui.radioButton_4.isChecked() else "Bisonho" if self.ui.radioButton_5.isChecked() else "Não selecionado"
    
        if not (nomeCompleto and nomeUsuario and email and senha):
            QMessageBox.warning(self, "Atenção", "Por favor, preencha o campo corretamente.")
            return
       
        if idade < 18:
            QMessageBox.warning(self, "Atenção", "Você é menor de idade.")
            return

        conteudo = f"Nome Completo: {nomeCompleto}\nNome de Usuário: {nomeUsuario}\nE-mail: {email}\nSenha: {senha}\nIdade: {idade}\nPersonagem: {personagem}"

        caminho = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt)")[0]
        if caminho:
            try:
                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo:\n{str(e)}")



    def limpar (self):
        self.ui.lineEditNome.clear()
        self.ui.lineEditUser.clear()
        self.ui.lineEditEmail.clear()
        self.ui.lineEditSenha.clear()
        self.ui.lineEditIdade.clear()
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.radioButton_4.setChecked(False)
        self.ui.radioButton_5.setChecked(False)
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())