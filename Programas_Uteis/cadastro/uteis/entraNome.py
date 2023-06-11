def Nome(frase):
    inputNome = input(frase)
    while inputNome == None or inputNome.strip() == '':
        inputNome = Nome(frase)
    return inputNome