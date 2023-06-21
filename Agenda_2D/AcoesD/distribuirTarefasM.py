from Python.Agenda_2D.menuM.tracoM import Traco
from Python.Agenda_2D.menuM.headerM import Header
from Python.Agenda_2D.utilsD.escolhaM import Escolha
from Python.Agenda_2D.menuM.printMenuM import Print_Menu
from Python.Agenda_2D.bancoDadosD.abrirCriarArquivoM import Abrir_Criar_Arquivo


def Distribuir_Tarefas(pacoteBairro):
    opcoesMenu = pacoteBairro[0]
    header = pacoteBairro[1]
    frase = pacoteBairro[2]
    arquivo = pacoteBairro[3]
    Traco("=")
    Header(header)
    Traco("=")
    Print_Menu(opcoesMenu)
    Abrir_Criar_Arquivo(arquivo)
    escolha = Escolha(frase, 0, len(opcoesMenu) - 2)
    pacote = [arquivo, header]
    if escolha == len(opcoesMenu) -1 : pacote = []
    else: opcoesMenu[escolha](pacote)