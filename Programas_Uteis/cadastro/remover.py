import os
import cadastro.cadastroMenu
from utils.tracos import Tracos
from cadastro.uteis.removendoCliente import Removendo
        
        
def Remover(nomePar = 'vazio'):
    os.system('clear')
    print(Tracos(' Cadastro de Clientes '),'\n')
    print(Tracos(' Removendo '),'\n')
    if nomePar == 'vazio':
        try:
            print('\nNome do cliente a ser removido: ',excluirNome)
        except:
            excluirNome = input('\nNome do cliente a ser removido: ')
    else:
        excluirNome = nomePar
    Removendo(excluirNome)
    input("\nQualquer tecla para voltar")
    cadastro.cadastroMenu.Cadastro()

