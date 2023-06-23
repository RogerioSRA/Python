import os
from funcao10 import teste10

os.system("clear")

def EncontraArquivo():
    arquivo = 'EncontraArquivo.txt'
    eArquivo = open(arquivo, "rt")

    numeracao = 0
    for num in eArquivo:
        pass
    ultimoNumero = num.split(";")[0]
    # print(ultimoNumero)
    print(num)
    print(ultimoNumero)



EncontraArquivo()

# file_lines = content_variable.readlines () content_variable.close () 

