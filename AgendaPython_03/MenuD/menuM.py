import os
from MenuD import tracoM, tituloM
from UtilsD.escolhaM import Escolha
from MenuD.imprimeMenuM import ImprimeMenu


def Menu():
    # Limpa console
    os.system("clear")


    # Monta Cabeçalho
    menuTraco = "="
    menuTitulo = "AGENDA"
    comprimentoTraco = 50
    tracoM.Traco(menuTraco, comprimentoTraco)
    tituloM.Titulo(menuTitulo, comprimentoTraco)
    tracoM.Traco(menuTraco, comprimentoTraco)


    # Monta Menú
    menuOpcoes = ["", "Acrescentar local de tarefa", "Tarefas para amanha", "Sair"]
    ImprimeMenu(menuOpcoes)
    

    max  = len(menuOpcoes) - 2
    pergunta = Escolha("Qual opção deseja ? : ", 0, max)


