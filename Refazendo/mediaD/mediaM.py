import os
from utilsD.tracosM import Tracos
from utilsD.escolhaM import Escolha


def Media_Entre_Valores():
    # Monta a tela
    os.system("clear")
    Tracos()
    Tracos(" MÉDIA ENTRE NÚMEROS ", " ")
    Tracos()
    print()
    # Quantos números ?
    quantidadeNumeros =input("A média será tirada de quantos números? : ")
    print()
    # Recebe os valores
    contagem = 1
    numeros = []
    while contagem <= int(quantidadeNumeros):
        numeros.append(input(f"{contagem:>3}o número : "))
        contagem += 1    
    # É tirada a média dos valores digitados
    mediaEntreValores = 0
    for valor in numeros:
        mediaEntreValores += int(valor)
    print(f"\nA soma entre os {quantidadeNumeros} valores resulta em {mediaEntreValores} e a média é {mediaEntreValores/int(quantidadeNumeros)}")
    # Nova média ?
    frase = "\nGostaria de nova média? 1-Sim  2-Não : "
    escolha = Escolha(frase, 1, 2)
    if escolha == 1: Media_Entre_Valores()
    else: return


