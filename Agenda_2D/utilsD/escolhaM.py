def Escolha(frase = "null", min = 0, max = 1):
    print()
    escolha = input(frase + f"( {min} - {max} ) : ")
    if escolha.isnumeric():
        escolha = int(escolha)
        if escolha >= min and escolha <= max:
            if escolha == 0: escolha = max + 1
            return escolha
        else:
            return Escolha(frase, min, max)
    else:
        return Escolha(frase, min, max)