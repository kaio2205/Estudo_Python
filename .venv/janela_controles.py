import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton,QVBoxLayout 

class JanelaControles(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("cadastro de Clientes")
        self.setGeometry(15,20,500,400)      
        # criar um layout p organizar os componetes 
        layout = QVBoxLayout()
        
        # criar p titulo da janela
        label_titulo = QLabel("gerenciar os clientes")
        label_titulo.setStyleSheet("QLabel{font-size: 30pt;color:#E8C446;font-weight:bold}")
        
        # criar elementos de textos p pedir ao usuarios dados dos clientes criaremos as labels
        label_nome = QLabel("Nome do cliente")
        label_nome.setStyleSheet("QLabel{font-size: 30pt;color:#000000;font-weight:bold}")
        label_email = QLabel("Email")
        label_email.setStyleSheet("QLabel{font-size: 30pt;color#000000;font-weight:bold}")
        label_telefone = QLabel("Telefone")
        label_telefone.setStyleSheet("QLabel{font-size: 30pt;color:#000000;font-weight:bold}")
        # criar elementos para que o usuario possa escrever as labels que estao pedindo 
        edit_nome = QLineEdit()
        edit_nome.setStyleSheet("QLineEdit{font-size: 15pt;padding:10px;border-radius:10px}")
        edit_email = QLineEdit()
        edit_email.setStyleSheet("QLineEdit{font-size: 15pt;padding:10px;border-radius:10px}")
        edit_telefone = QLineEdit()
        edit_telefone.setStyleSheet("QLineEdit{font-size: 15pt;padding:10px;border-radius:10px}")
        
        # criar um controle de botao p realizar um possivel cadastro  
        btn_cadastro = QPushButton("cadastrar")
 
        layout.addWidget(label_titulo)
        #add os controles de label edit  ao layout
        layout.addWidget(label_nome)
        layout.addWidget(edit_nome)
        
        layout.addWidget(label_email)
        layout.addWidget(edit_email)
        
        
        layout.addWidget(label_telefone)
        layout.addWidget(edit_telefone)
        
        layout.addWidget(btn_cadastro) 
        
        
        #  adicionar  o layout na janela 
        self.setLayout(layout)
        
app =QApplication(sys.argv)
tela=JanelaControles()
tela.show()
app.exec_()     