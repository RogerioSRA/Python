import os
from tracoM import Traco
from headerM import Header
from printMenuM import Print_Menu
from utilsD.escolhaM import Escolha
from abrirCriarArquivoM import Abrir_Criar_Arquivo
from Python.Agenda_2D.bancoDadosD.abrirCriarArquivoM import*
from registraBancoDadosLocaisM import RegistraBancoDadosLocais


def Menu():
    os.system("clear")
    arquivo = "Locais_Para_Tarefas.txt"
    Abrir_Criar_Arquivo(arquivo)
    opcoesMenu = ["", "Sair"]
    RegistraBancoDadosLocais("local", opcoesMenu)
    
    
    header = " AGENDA "
    Traco("=")
    Header(header)
    Traco("=")
    Print_Menu(opcoesMenu)
    frase = "Gostaria de registrar um local de tarefa? 1-Sim  2-Não : "
    escolha = Escolha(frase, 1, 2)
    if escolha == 1:
        localDeTarefa = input("Entre o um 'Local De Tarefa': ")
        localDeTarefa = localDeTarefa.title()
        localDeTarefa = localDeTarefa.replace(" ","_")
        opcoesMenu.insert(len(opcoesMenu)-1, localDeTarefa)
        return Menu()
    frase = "Qual a sua escolha? "
    escolha = Escolha(frase, 0, len(opcoesMenu) - 2)
    opcoesMenu[escolha]()



def Voltar_ao_Menu(pacote):
    Menu()



def Tarefas_para_Amanha():
    print("Tarefas para Amanhã")


Menu()


