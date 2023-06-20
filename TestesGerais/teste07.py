import random, os

def Organizando(apostas):
    print("Organizando apostas:\n")
    apostasOrganizadas = []
    for chaves in apostas:
        chaves.sort()
        apostasOrganizadas.append(chaves)
    apostasOrganizadas.sort()
    print()
    print("Apostas Organizadas e limpas:\n")
    for chaves in apostasOrganizadas:
        for num in chaves:
            print(f"{num:>2}, ", end = "")
        print()


class JogosLoteria:
    def Menu():
        os.system("clear")
        menu = "1 - Quina\n2 - Mega-Sena\n3 - Lotofacil"
        print(menu)
        print()
        jogo = input("Sobre qual tipo de jogo gostaria de receber apostas? ")
        if jogo.isnumeric:
            qtdAp = input("De quantas sugestões gostaria? ")
            if qtdAp.isnumeric:
                jogo = int(jogo)
                qtdAp = int(qtdAp)
                JogosLoteria.EscolhaDaLoteria(jogo, qtdAp)
        else:
            JogosLoteria.Menu()


    def EscolhaDaLoteria(jogo, qtdAp):
        tipoJogo = (0, 80, 60, 25)
        qtdNumAp = (0, 5, 6, 15)
        
        qtdNum = qtdNumAp[jogo]
        numFinal = tipoJogo[jogo]
        qtdAp
        JogosLoteria.Jogo(qtdNum, numFinal, qtdAp)


    def Jogo(qtdNum = 5, numFinal = 25, qtdAp = 1):
        print()
        apostas = []
        while qtdAp > 0:
            num = []
            cont = qtdNum
            while cont > 0:
                numEscolhido = (random.randint(1, numFinal))
                if num.__contains__(numEscolhido):
                    # print("Repetiu")
                    continue
                num.append(numEscolhido)
                cont -= 1
            num.sort()
            apostas.append(num)
            print(f"=> {num}")
            qtdAp -= 1
        Organizando(apostas)


JogosLoteria.Menu()




# Organizando()