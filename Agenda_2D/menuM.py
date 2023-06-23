import os
from utilsD.escolhaM import Escolha
from menuD import tracoM, headerM, printMenuM
from AcoesD.distribuirTarefasM import Distribuir_Tarefas
from bancoDadosD import resgataBancoDadosM, abrirCriarArquivoM, registraBancoDadosLocaisM


def Menu():
    # cria banco dados para locais
    arquivos = ["Locais_Para_Tarefas.txt", "Locais_Para_Tarefas_Backup.txt", "Salva_Pacotes.txt"]
    abrirCriarArquivoM.Abrir_Criar_Arquivo(arquivos)
    arquivo = arquivos[0]
    arquivoBackup = arquivos[1]


    # registra primeiras opções
    opcoesMenu = resgataBancoDadosM.ResgataBancoDados(arquivo)
    if opcoesMenu == []:
        opcoesMenu = ["", "Sair", "Adicionar Local de Tarefas"]
        registraBancoDadosLocaisM.RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu)
    MenuMenu()
    printMenuM.Print_Menu(opcoesMenu) 
    frase = "Qual a sua escolha? "
    escolha = Escolha(frase, 0, len(opcoesMenu) - 3)
    if escolha == 0: return exit()
    if escolha == 99:
        MenuMenu()
        print()
        localDeTarefa = input("Entre o um 'Local De Tarefa': ")
        localDeTarefa = localDeTarefa.title()
        opcoesMenu.insert(len(opcoesMenu)-2, localDeTarefa)
        registraBancoDadosLocaisM.RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu)
        return Menu()
    tarefa = opcoesMenu[escolha]
    pacoteBairro = [tarefa, frase]
    Distribuir_Tarefas(pacoteBairro)


def MenuMenu():
    os.system("clear")
    header = " AGENDA "
    tracoM.Traco("=")
    headerM.Header(header)
    tracoM.Traco("=")


def Tarefas_para_Amanha():
    print("Tarefas para Amanhã")

