import os
import menu.menu
from utils.tracos import Linha, Tracos
from tabuada.tabuadaZeros import Tabuada_Zeros


def Tabuada():
    os.system('clear')
    print(Tracos(' Tabuada '),'\n')
    try:
        numero = int(input("Entre com o número: "))
    except:
        Tabuada()
    print(Linha())
    zeros = Tabuada_Zeros
    contador = 0
    while contador <= 10:
        soma = numero * contador
        print(f"{zeros(numero)} x {zeros(contador)} = {zeros(soma)}")
        contador += 1
    print(Linha())
    tab_opcao = input("Novo número: 1-Sim 2-Não : ")
    match tab_opcao:
        case '1':
            Tabuada()
        case _:
            menu.menu.Menu()
        

