import os
from tabuada.tabuada import Tabuada
from cadastro.cadastroMenu import Cadastro
from utils.tracos import MenuMontagem, Tracos
from media_numeros.mediaNumeros import MediaNumeros


tabuada = Tabuada
mediaNumeros = MediaNumeros
cadastro = Cadastro


def Menu():
    os.system('clear')
    print(Tracos(' Menu '),'\n')
    MenuMontagem(['1 - Tabuada', '2 - Média entre números', '3 - Cadastro de Clientes', '', '0 - Sair'])    
    option = input("\nOpção: ")
    while option == None:
        option = Menu()
    match option:
        case '1':
            tabuada()
        case '2':
            mediaNumeros()
        case '3':
            cadastro()
        case '0':
            print("\nObrigado, e até breve  !!!\n")         
        case _:
            Menu()

        