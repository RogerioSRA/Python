import os
from Python.Agenda_2D.menuM.tracoM import Traco
from Python.Agenda_2D.menuM.headerM import Header


def Apagar_Tarefa(pacote):    
    os.system("clear")
    Traco("=")
    Header(pacote[1])
    Traco("=")
    header = " Apagando Tarefas "
    Header(header)
    Traco("=")
    tarefa = input("Qual a posição da tarefa a ser apagada ? : \n",)
    # tarefa = tarefa.capitalize()
    # frase = "Está correto este nome ? 1-Sim  2-Não : "
    # escolha = Escolha(frase, 1, 2)
    # if escolha == 1:
    #     RegistraBancoDados(pacote, tarefa)
    #     print(f"\nTarefa registrada na data de {date.today().day}-{date.today().month}-{date.today().year}")
    #     frase = "Gostaria de um novo registro ? : 1-Sim  2-Não : "
    #     escolha = Escolha(frase, 1, 2)
    #     if escolha == 1: return Nova_Tarefa(pacote)
    #     else: return Boa_Vista()
    # if escolha == 2: return Nova_Tarefa(pacote)