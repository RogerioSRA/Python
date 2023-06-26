import os
from utilsD.escolhaM import Escolha
from menuD import tituloM, tracoM, printMenuM
from AcoesD.distribuirTarefasM import Distribuir_Tarefas
from AcoesD.tarefasParaAmanhaM import Tarefas_para_Amanha
from bancoDadosD import resgataBancoDadosM, abrirCriarArquivoM, registraBancoDadosLocaisM


def Menu():
    local = pergunta = tarefa = titulo = retorno = arquivo = subtitulo = ""


    # cria banco dados para locais
    arquivos = ["Locais-Para-Tarefas.txt", "Locais-Para-Tarefas__Backup.txt"]
    arquivos = abrirCriarArquivoM.Abrir_Criar_Arquivo(arquivos)
    arquivo = arquivos[0]
    arquivoBackup = arquivos[1]


    # Resgata(se tiver) ou Registra primeiras opções
    opcoesMenu = resgataBancoDadosM.ResgataBancoDados(arquivo)
    if opcoesMenu == []:
        opcoesMenu = ["", "Adicionar Local de Tarefas", "Tarefas  para  o  Amanhã", "Sair"]
        registraBancoDadosLocaisM.RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu)


    # Imprime o menu do Menu
    ImprimirMenu()
    printMenuM.Print_Menu(opcoesMenu) 
    pergunta = "Qual a sua escolha? "
    escolha = Escolha(pergunta, 0, len(opcoesMenu) - 2)


    # Registra uma Tarefa no Banco De Dados
    if escolha == 1:
        ImprimirMenu()
        tituloM.Titulo(opcoesMenu[escolha])
        tracoM.Traco("=")
        print()
        localDeTarefa = input("Entre com o 'Local De Tarefa': ")
        localDeTarefa = localDeTarefa.title()
        opcoesMenu.insert(len(opcoesMenu)-1, localDeTarefa)
        registraBancoDadosLocaisM.RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu)
        return Menu()
    
    
    # Tarefas para o dia de amanhã
    if escolha == 2:
        local = opcoesMenu[escolha]
        Tarefas_para_Amanha(local, pergunta)
    
    
    # Reune informações em pacote para tomada de decisões
    local = opcoesMenu[escolha]
    Distribuir_Tarefas(local = local, pergunta = pergunta, tarefa = tarefa, titulo = titulo, retorno = retorno, arquivo = arquivo, subtitulo = subtitulo)


def ImprimirMenu():
    os.system("clear")
    titulo = " AGENDA "
    tracoM.Traco("=")
    tituloM.Titulo(titulo)
    tracoM.Traco("=")





