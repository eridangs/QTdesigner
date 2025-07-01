import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from cadastro import Ui_MainWindow

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dados_candidatos = {}

        self.ui.pushButtonSalvar.clicked.connect(self.salvar)
        self.ui.pushButtonCancelar.clicked.connect(self.limpar)

    #-----------------------------------------------------------------------------------------------------------
    
    def salvar(self):
        cpf = int(self.ui.lineEditCpf.text())
        pt = int(self.ui.lineEditPt.text())
        mat = int(self.ui.lineEditMat.text())
        geral = int(self.ui.lineEditGeral.text())
        especifico = int(self.ui.lineEditEspecifico.text())
        media = 0
        if not pt or not mat or not geral or not especifico:
            QMessageBox.warning(self, "Atenção", "Por favor, preencha todos os campos.")
        else:
            try:

                self.dados_candidatos[cpf] = {
                    "Matematica": mat,
                    "Portugues": pt,
                    "Conhecimentos Gerais ": geral,
                    "Conhecimentos Especificos ": especifico,
                    "Media": media
                }

                self.salvar_json()
                QMessageBox.information(self, "Sucesso", "Dados salvos com sucesso!")

                self.limpar()

            except ValueError:
                QMessageBox.warning(self, "Atenção", "CPF e demais campos devem ser um número válido.")

    #-----------------------------------------------------------------------------------------------------------

    def salvar_json(self):
        try:

            #verificar se o arquivo existe
            if os.path.exists('dados_candidatos.json'):

                #se existir: carregar os dados
                with open ('dados_candidatos.json','r') as f:
                    dados_existentes = json.load(f)

                #Atualizar os dados existentes com os novos dados
                dados_existentes.update(self.dados_candidatos)

                #Abrir o arquivo em modo de escrita para salvar os dados atualizados
                with open('dados_candidatos.json', 'w') as f:
                    json.dump(dados_existentes,f,indent=4)

            # Se o arquivo não existir: salvar os dados
            else:
                with open('dados_candidatos.json', 'w') as f:
                    json.dump(self.dados_candidatos, f, indent=4)
        
        except Exception as e:
            QMessageBox.warning(self, "Erro ao salvar", f"Ocorreu um erro ao salvar os dados.")


    #-----------------------------------------------------------------------------------------------------------
            
    def limpar(self):
        self.ui.lineEditCpf.clear()
        self.ui.lineEditPt.clear()
        self.ui.lineEditMat.clear()
        self.ui.lineEditGeral.clear()
        self.ui.lineEditEspecifico.clear()

    #-----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

# pt *= 2
# mat *= 2
# geral *= 2
# especifico *= 2
# media = pt * 0.2 + mat * 0.2 + geral * 0.2 + especifico * 0.5
# media /= 10

# return media