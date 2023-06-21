import os
from datetime import date
from Python.Agenda_2D.menuM.tracoM import Traco
from Python.Agenda_2D.menuM.headerM import Header


def Listar_Tarefas(pacote):
    os.system("clear")
    compTraco = 80
    Traco("=", compTraco)
    Header(pacote[1], compTraco)
    Traco("=", compTraco)
    header = " Listando Tarefas "
    Header(header, compTraco)
    Traco("=", compTraco)
    print()
    print(f"{'Data':<13}{'Tarefa':<50}{'Dias de atraso'}")
    print()
    cores = "0"
    bancoDados = open(pacote[0], "rt")
    for acao in bancoDados:
        data = acao.split(";")
        acao = acao.split(";")
        acao = acao[1].split("\n")
        dataDeAtraso = str(data[0]).split("-")
        diasDeAtraso = date.today() - date(int(dataDeAtraso[2]), int(dataDeAtraso[1]), int(dataDeAtraso[0]))
        diasDeAtraso = str(diasDeAtraso).split(",")
        diasDeAtraso = str(diasDeAtraso[0]).split(" ")
        if diasDeAtraso[0] == "0:00:00": diasDeAtraso[0] = "Hoje"
        elif int(diasDeAtraso[0]) > 1 : dias = "  dias"
        else: dias = "  dia "
        if cores == "\033[4;32m": cores = "\033[4;34m"
        else: cores = "\033[4;32m"
        print(f"{cores}{data[0]:<13}{acao[0][:50]:<50}{diasDeAtraso[0]:>5}{dias}\033[m")
        print()
    print()