import os
from utils.tracos import Tracos
from cadastro import cadastroMenu
from cadastro.cadastrar import Registro
from cadastro.uteis.entraNome import Nome
from cadastro.Armazenamento.bancoDeDados import *
from cadastro.uteis.removendoCliente import Removendo
        
        
def Editar():
    global bancoDeDadosVar
    bancoDeDadosVar = 'BancoDeDados'
    os.system('clear')
    print(Tracos(' Cadastro de Clientes '),'\n')
    print(Tracos(' Editando '),'\n')
    excluirNome = Nome('\nNome do cliente a ser editado: ')
    Removendo(excluirNome)
    Registro(nomeFrase = "\nNome do cliente para substituição: ", idadeFrase = "Idade do cliente para substituição: ", modulo = 'Editar')
    cadastroMenu.Cadastro()



