import menu.menu
from cadastro.editar import*
from cadastro.cadastrar import *
from cadastro.remover import Remover
from cadastro.verLista import VerLista
from utils.tracos import Tracos, MenuMontagem


def Cadastro():
    os.system('clear')
    print(Tracos(' Cadastro de Clientes '),'\n')
    MenuMontagem(['1 - Cadastrar cliente', '2 - Ver clientes cadastrados', '3 - Remover um cliente', '4 - Editar cadastro de cliente', '', '0 - Menu Principal'])
    cadOpcao = input("\nQual a operação desejada? ")
    match cadOpcao:
        case '1':
            Cadastrar()
        case '2':
            VerLista()
        case '3':
            Remover()
        case '4':
            Editar()
        case '0':
            menu.menu.Menu()
        case _:
            Cadastro()

