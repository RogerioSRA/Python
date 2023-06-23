import os
from time import sleep
from datetime import date
from menuD.tracoM import Traco
from menuD.headerM import Header
from AcoesD.locaisM import Locais
from utilsD.escolhaM import Escolha
from AcoesD import distribuirTarefasM
from AcoesD.salvaPacotesM import Salva_Pacotes
from bancoDadosD.registraBancoDadosTarefasM import RegistraBancoDadosTarefas


def Acrescentar_Tarefa(pacoteDistribuir):
    # tarefa, header, frase, arquivo
    tarefa = pacoteDistribuir[0]
    header = pacoteDistribuir[1]
    frase = pacoteDistribuir[2]
    arquivo = pacoteDistribuir[3]
    os.system("clear")
    Traco("=")
    Header(header)
    Traco("=")
    header = " Adicionando Tarefas "
    Header(header)
    Traco("=")    
    tarefa = input("Qual o nome da tarefa ? : \n",)
    tarefa = tarefa.capitalize()
    frase = "Está correto este nome ? 1-Sim  2-Não : "
    escolha = Escolha(frase, 1, 2)
    if escolha == 1:
        arquivo = Locais(arquivo)
        pacoteAcrescenta = [arquivo, tarefa]
        RegistraBancoDadosTarefas(pacoteAcrescenta)
        print(f"\nTarefa registrada na data de {date.today().day}-{date.today().month}-{date.today().year}")
        frase = "Gostaria de um novo registro ? : 1-Sim  2-Não : "
        escolha = Escolha(frase, 1, 2)
        if escolha == 1: return Acrescentar_Tarefa(pacoteDistribuir)
        else:
            pacoteBairro = Salva_Pacotes()
            print(pacoteBairro)
            return distribuirTarefasM.Distribuir_Tarefas(pacoteBairro)
    if escolha == 2: return Acrescentar_Tarefa(pacoteDistribuir)


    