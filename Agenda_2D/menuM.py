import os
from utilsD.escolhaM import Escolha
from menuD import tracoM, headerM, printMenuM
from AcoesD.distribuirTarefasM import Distribuir_Tarefas
from AcoesD.tarefasParaAmanhaM import Tarefas_para_Amanha
from bancoDadosD import resgataBancoDadosM, abrirCriarArquivoM, registraBancoDadosLocaisM


def Menu():
    # cria banco dados para locais
    arquivos = ["Locais-Para-Tarefas.txt", "Locais-Para-Tarefas__Backup.txt"]
    arquivos = abrirCriarArquivoM.Abrir_Criar_Arquivo(arquivos)
    arquivo = arquivos[0]
    arquivoBackup = arquivos[1]


    # registra primeiras opções
    opcoesMenu = resgataBancoDadosM.ResgataBancoDados(arquivo)
    if opcoesMenu == []:
        opcoesMenu = ["", "Adicionar Local de Tarefas", "Tarefas   para   o  Amanhã", "Sair"]
        registraBancoDadosLocaisM.RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu)


    # Imprime o menu do Menu
    ImprimirMenu()
    printMenuM.Print_Menu(opcoesMenu) 
    frase = "Qual a sua escolha? "
    escolha = Escolha(frase, 0, len(opcoesMenu) - 2)


    # Sair
    if escolha == 0: return exit()


    # Registra uma Tarefa no Banco De Dados
    if escolha == 1:
        ImprimirMenu()
        print()
        localDeTarefa = input("Entre com o 'Local De Tarefa': ")
        localDeTarefa = localDeTarefa.title()
        opcoesMenu.insert(len(opcoesMenu)-1, localDeTarefa)
        registraBancoDadosLocaisM.RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu)
        return Menu()
    
    # Tarefas para o dia de amanhã
    if escolha == 2:
        tarefa = opcoesMenu[escolha]
        pacoteBairro = [tarefa, frase]
        Tarefas_para_Amanha(pacoteBairro)
    
    
    # Reune informações em pacote para tomada de decisões
    tarefa = opcoesMenu[escolha]
    pacoteBairro = [tarefa, frase]
    Distribuir_Tarefas(pacoteBairro)


def ImprimirMenu():
    os.system("clear")
    header = " AGENDA "
    tracoM.Traco("=")
    headerM.Header(header)
    tracoM.Traco("=")





