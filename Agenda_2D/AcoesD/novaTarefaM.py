import os
from datetime import date
from Python.Agenda_2D.menuM.tracoM import Traco
from Python.Agenda_2D.menuM.headerM import Header
from Python.Agenda_2D.utilsD.escolhaM import Escolha
from Python.Agenda_2D.bancoDadosD.registraBancoDadosTarefasM import RegistraBancoDadosTarefas


def Nova_Tarefa(pacote):
    os.system("clear")
    Traco("=")
    Header(pacote[1])
    Traco("=")
    header = " Adicionando Tarefas "
    Header(header)
    Traco("=")    
    tarefa = input("Qual o nome da tarefa ? : \n",)
    tarefa = tarefa.capitalize()
    frase = "Está correto este nome ? 1-Sim  2-Não : "
    escolha = Escolha(frase, 1, 2)
    if escolha == 1:
        RegistraBancoDadosTarefas(pacote, tarefa)
        print(f"\nTarefa registrada na data de {date.today().day}-{date.today().month}-{date.today().year}")
        frase = "Gostaria de um novo registro ? : 1-Sim  2-Não : "
        escolha = Escolha(frase, 1, 2)
        if escolha == 1: return Nova_Tarefa(pacote)
        # else: return Boa_Vista()
    if escolha == 2: return Nova_Tarefa(pacote)