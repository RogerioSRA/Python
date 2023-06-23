import os
import menuM
from menuD.tracoM import Traco
from menuD.headerM import Header
from utilsD.escolhaM import Escolha
from menuD.printMenuM import Print_Menu
from AcoesD.salvaPacotesM import Salva_Pacotes
from AcoesD.acrescentarTarefaM import Acrescentar_Tarefa


def Distribuir_Tarefas(pacoteBairro):
    # tarefa, frase
    os.system("clear")


    # Salva ítens atuais do menú
    Salva_Pacotes(pacoteBairro)


    # Monta menú
    opcoesMenu = ["", "Acrescentar Tarefa", "Excluir Tarefa", "Listar Tarefas", "Voltar", "Sair"]
    arquivo = pacoteBairro[0].title()
    arquivo = arquivo.replace("  ","-")
    arquivo = arquivo.replace(" ","-") +"__tarefas.txt"
    header = f" {pacoteBairro[0]} "
    frase = pacoteBairro[1]
    Traco("=")
    Header(header)
    Traco("=")
    Print_Menu(opcoesMenu)


    escolha = Escolha(frase, 0, len(opcoesMenu) - 2)
    if escolha == 0 :
        return exit()
    elif escolha == len(opcoesMenu) -2 :
        return menuM.Menu()
    else:
        tarefa = opcoesMenu[escolha]        
        pacoteTarefa = [tarefa, header, frase, arquivo]
        eval(opcoesMenu[escolha].replace(" ","_"))(pacoteTarefa)


