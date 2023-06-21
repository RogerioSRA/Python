from datetime import date
from Agenda_2D.utilsD import zerosM


def RegistraBancoDadosTarefas(pacote, tarefa):
    data = str(zerosM.Zeros(date.today().day)) + "-" + str(zerosM.Zeros(date.today().month)) + "-" + str(date.today().year)
    bancoDados = open(pacote[0], 'at')
    bancoDados.write(data + ";" + tarefa + "\n")
    bancoDados.close()