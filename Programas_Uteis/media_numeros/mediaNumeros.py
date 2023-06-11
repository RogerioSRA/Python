import os
import menu.menu
from utils.tracos import Tracos, Linha


def MediaNumeros():
    os.system('clear')
    print(Tracos(' Media números '),'\n')
    try:
        quant = int(input("Deseja a média de quantos números? "))
    except:
        mnOpcao = input("\nDados inválidos digitados.\nDeseja tentar novamente? 1-Sim 2-Não ")
        match mnOpcao:
            case '1':
                MediaNumeros()
            case _:
                menu.menu.Menu()                
    if (quant < 2):
        try:
            mnOpcao = input("\nEscolha entre, no mínimo, dois números.\nDeseja tentar novamente? 1-Sim 2-Não ")
            match mnOpcao:
                case '1':
                    MediaNumeros()
                case _:
                    menu.menu.Menu()                    
        except:
            menu.menu.Menu()        
    contador = 0
    num = []
    print(Linha())
    print("Entre com os números:\n")
    while contador < quant:
        try:
            num.append(float(input('%io número: '%(contador+1))))
        except:
            MediaNumeros()
        contador += 1
    contador = 0
    mnresultado = 0
    while contador < quant:
        mnresultado += num[contador]
        contador += 1
    if ((mnresultado % quant) < 1):
        print(f"\nA média entre os {quant} números é {int(mnresultado/quant)}  .")
    else:
        print(f"\nA média entre os {quant} números é {mnresultado/quant:.2}  .")
    print(Linha())
    try:
        mnOpcao = int(input("Nova pesquisa ? 1-Sim 2-Não "))
        match mnOpcao:
            case 1:
                MediaNumeros()
            case _:
                menu.menu.Menu()
    except:
        menu.menu.Menu()
        
        