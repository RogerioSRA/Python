import os
from utilsD.escolhaM import Escolha
from utilsD.tracosM import MenuMontagem, Tracos

def Tabuada():

    #Monta a tela:
    os.system("clear")
    Tracos()
    Tracos(" TABUADA ", " ")
    Tracos()
    print()

    # Pega os dados (Número, Operação):
    frase = "Escolha um número para a tabuada: "
    escolha = Escolha(frase, 0, 100)
    print()
    frase = "Escolha a operação: "
    operacao = ['Adição', 'Subtração', 'Multiplicaçao', 'Divisão\n']
    MenuMontagem(operacao)

    # Monta a tabuada com 'número' e 'operação' escolhidos
    opcoes = Escolha(frase, 1, 4)
    enumerate = ['x','+', '-', '*', '/']
    print()
    Tracos()
    print()
    contagemReferencia = 1
    contagem = contagemReferencia
    final = 10
    if opcoes == 2:
        contagem = escolha + 1
        final = escolha + 10
    if opcoes == 4:
        contagem = escolha
        final = escolha * 10
    while contagem <= final:
        res = int(eval(f"{contagem}{enumerate[opcoes]}{escolha}"))
        if opcoes == 2 or opcoes == 4:
                print(f"{contagem:>3}  {enumerate[opcoes]} {escolha:>3}  = {res:>3}")
        if opcoes == 1 or opcoes == 3:
                print(f"{escolha:>3}  {enumerate[opcoes]} {contagem:>3}  = {res:>3}")
        contagemReferencia += 1
        if opcoes == 4:
            contagem = contagemReferencia * escolha
        else:
            contagem += 1        
    Tracos()

    # Nova operação ?
    print()
    frase = "Deseja nova tabuada ? 1-Sim  2-Não : "
    resp = Escolha(frase, 1, 2)
    if resp == 1: Tabuada()
    else: return


