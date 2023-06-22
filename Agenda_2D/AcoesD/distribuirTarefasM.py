from menuD.tracoM import Traco
from menuD.headerM import Header
from utilsD.escolhaM import Escolha
from menuD.printMenuM import Print_Menu


def Distribuir_Tarefas(pacoteBairro):
    opcoesMenu = pacoteBairro[0]
    header = pacoteBairro[1]
    frase = pacoteBairro[2]
    arquivo = pacoteBairro[3]
    Traco("=")
    Header(header)
    Traco("=")
    Print_Menu(opcoesMenu)
    escolha = Escolha(frase, 0, len(opcoesMenu) - 2)
    pacote = [arquivo, header]
    if escolha == len(opcoesMenu) -1 : pacote = []
    else: opcoesMenu[escolha](pacote)