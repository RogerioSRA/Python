def Idade(frase):
    try:
        inputIdade = int(input(frase))
        while inputIdade == None or inputIdade <1 or inputIdade > 150:
            return Idade(frase)
        return inputIdade
    except:
        inputIdade = 0
        while inputIdade == None or inputIdade <1 or inputIdade > 150:
            return Idade(frase)
        return inputIdade