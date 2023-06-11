import os
from utilsD.escolhaM import Escolha
from tabuadaD.tabuadaM import Tabuada
from cadastroD.cadastroM import Cadastro
from mediaD.mediaM import Media_Entre_Valores
from utilsD.tracosM import MenuMontagem, Tracos


def Menu():
    # Monta a tela
    os.system("clear")
    Tracos()
    Tracos(" MENÚ ", " ")
    Tracos()
    print()
    menu=["", Tabuada, Cadastro, Media_Entre_Valores, exit]
    MenuMontagem(menu)
    # Opções de direcionamento
    pergunta = "Qual opção deseja ? "
    escolha = Escolha(pergunta, 0, (len(menu)-1))
    menu[escolha]()
    Menu()

