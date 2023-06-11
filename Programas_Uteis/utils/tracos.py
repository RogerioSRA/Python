def Tracos(titulo):
    comprimento = int((32 - len(titulo))/2)
    return comprimento*'='+titulo+comprimento*'='


def Linha():
    return '\n'+30*'-'+'\n'


def MenuMontagem(lista):
    for item in lista:
        print(item)

