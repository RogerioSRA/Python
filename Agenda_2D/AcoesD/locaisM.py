import os

from Python.Agenda_2D.AcoesD.distribuirTarefasM import Distribuir_Tarefas


def Locais():
    os.system("clear")
    # opcoesMenu = ["", Nova_Tarefa, Apagar_Tarefa, Tarefas_Concluidas, Listar_Tarefas, Voltar_ao_Menu, exit]
    header = " Tarefas para o Boa Vista"
    frase = "Qual a sua escolha? "
    arquivo = "TarefasBoaVista.txt"
    pacoteBairro = [opcoesMenu, header, frase, arquivo]
    Distribuir_Tarefas(pacoteBairro)

    