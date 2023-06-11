def Escolha(frase, menor = 0, maior = 1):
    escolha = input(frase)
    try:
        escolha = escolha.strip()
        escolha = int(escolha)
    except:
        return Escolha(frase, menor, maior)
    else:
        if escolha == None or escolha < menor or escolha > maior: return Escolha(frase, menor, maior)
        else:
            if escolha == 0:
                escolha = maior
            return escolha

