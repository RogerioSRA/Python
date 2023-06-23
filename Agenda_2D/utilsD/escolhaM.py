def Escolha(frase = "null", min = 0, max = 1):
    print()
    escolha = input(frase + f"( {min} - {max} ) : ")
    if escolha.isnumeric():
        if escolha == '99':
            escolha = 99
            return escolha
        escolha = int(escolha)
        if escolha >= min and escolha <= max:
            return escolha
        else:
            return Escolha(frase, min, max)
    else:
        return Escolha(frase, min, max)
    

