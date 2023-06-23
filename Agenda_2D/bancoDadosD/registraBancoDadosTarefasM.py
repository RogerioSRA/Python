from datetime import date
from utilsD import zerosM


def RegistraBancoDadosTarefas(pacoteAcrescenta):
    data = str(zerosM.Zeros(date.today().day)) + "-" + str(zerosM.Zeros(date.today().month)) + "-" + str(date.today().year)
    arquivo = pacoteAcrescenta[0]
    tarefa = pacoteAcrescenta[1]
    bancoDados = open(arquivo, 'at')
    bancoDados.write(data + ";" + tarefa + "\n")
    bancoDados.close()

    