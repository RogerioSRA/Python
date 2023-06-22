import os
from menuD.tracoM import Traco
from menuD.headerM import Header
from utilsD.escolhaM import Escolha
from menuD.printMenuM import Print_Menu
from bancoDadosD.resgataBancoDadosM import ResgataBancoDados
from bancoDadosD.abrirCriarArquivoM import Abrir_Criar_Arquivo
from AcoesD.distribuirTarefasM import Distribuir_Tarefas
from bancoDadosD.registraBancoDadosLocaisM import RegistraBancoDadosLocais


def Menu():
    os.system("clear")

    # cria banco dados para locais
    arquivos = ["Locais_Para_Tarefas.txt", "Locais_Para_Tarefas_Backup.txt"]
    Abrir_Criar_Arquivo(arquivos)
    arquivo = arquivos[0]
    arquivoBackup = arquivos[1]

    # registra primeiras opções
    opcoesMenu = ["", "Sair"]
    RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu)
    
    opcoesMenu = ResgataBancoDados(arquivo)
    
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
        RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu)
        return Menu()
    
    frase = "Qual a sua escolha? "
    escolha = Escolha(frase, 0, len(opcoesMenu) - 2)
    if escolha == len(opcoesMenu)-1: return exit()
    pacoteBairro = [opcoesMenu[escolha], header, frase, arquivo]
    Distribuir_Tarefas(pacoteBairro)



def Voltar_ao_Menu(pacote):
    Menu()



def Tarefas_para_Amanha():
    print("Tarefas para Amanhã")


Menu()


