def Escolha(frase = "null", min = 0, max = 1):
    print()
    escolha = input(frase + f"( {min} - {max} ) : ")
    if escolha.isnumeric():
        escolha = int(escolha)
        if escolha == 0: exit()
        if escolha >= min and escolha <= max:
            return escolha
        else:
            return Escolha(frase, min, max)
    else:
        return Escolha(frase, min, max)
    

