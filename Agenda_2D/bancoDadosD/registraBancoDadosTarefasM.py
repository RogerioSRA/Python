from datetime import date
from time import sleep
from utilsD import zerosM


def RegistraBancoDadosTarefas(pacoteAcrescenta):
    data = str(zerosM.Zeros(date.today().day)) + "-" + str(zerosM.Zeros(date.today().month)) + "-" + str(date.today().year)
    arquivo = pacoteAcrescenta[0]
    tarefa = pacoteAcrescenta[1]
    posicao = EncontraUltimoArquivo(arquivo)
    bancoDados = open(arquivo, 'at')
    bancoDados.write(posicao + ";" + data + ";" + tarefa + "\n")
    bancoDados.close()


def EncontraUltimoArquivo(arquivo):
    try:
        bdados = open(arquivo, "rt")
        for num in bdados:
            pass
        posicao = num.split(";")
        posicao = int(posicao[0]) + 1
        print(posicao)
        print("Try: posição = ", posicao)
        return str(posicao)
    except:
        posicao = 0
        print("Except: posição = ", posicao)
        return str(posicao)

    