import os
import menuD.menuM as menuM
from menuD.tracoM import Traco
from menuD.tituloM import Titulo
from AcoesD.locaisM import Locais
from utilsD.escolhaM import Escolha
from menuD.printMenuM import Print_Menu
from AcoesD.salvaPacotesM import Salva_Pacotes
from AcoesD.listarTarefasM import Listar_Tarefas
from AcoesD.excluirTarefasM import Excluir_Tarefa
from AcoesD.acrescentarTarefaM import Acrescentar_Tarefa


def Distribuir_Tarefas(local, pergunta, tarefa, titulo, retorno, arquivo, subtitulo):

    # local = local
    # pergunta = pergunta
    # tarefa = tarefa
    # titulo = titulo
    # retorno = retorno
    # arquivo = arquivo
    # subtitulo = subtitulo

    # local = pacote[0]
    # pergunta = pacote[1]
    # tarefa = pacote[2]
    # titulo = pacote[3]
    # retorno = pacote[4]
    # arquivo = pacote[5]
    # subtitulo = pacote[6]
    os.system("clear")
    # print(pacote)


    # Salva ítens atuais do menú
    Salva_Pacotes(local, pergunta)


    # Monta menú
    opcoesMenu = ["", "Acrescentar Tarefa", "Excluir Tarefa", "Listar Tarefas", "Voltar", "Sair"]
    arquivo = local.title()
    local = arquivo
    titulo = f" {local} "
    arquivo = arquivo.replace("  ","-")
    arquivo = arquivo.replace(" ","-") +"-tarefas.txt"
    arquivo = Locais(arquivo)
    Traco("=")
    Titulo(titulo)
    Traco("=")
    Print_Menu(opcoesMenu)


    escolha = Escolha(pergunta, 0, len(opcoesMenu) - 2)
    if escolha == 0 :
        return exit()
    elif escolha == len(opcoesMenu) -2 :
        return menuM.Menu()
    else:
        tarefa = opcoesMenu[escolha]
        retorno = Distribuir_Tarefas
        # pacoteTarefa = [tarefa, header, frase, arquivo, local]
        eval(opcoesMenu[escolha].replace(" ","_"))(local = local, pergunta = pergunta, tarefa = tarefa, titulo = titulo, retorno = retorno, arquivo = arquivo, subtitulo = subtitulo)
        # eval(opcoesMenu[escolha].replace(" ","_"))(pacoteTarefa)
    return Distribuir_Tarefas(local = local, pergunta = pergunta, tarefa = tarefa, titulo = titulo, retorno = retorno, arquivo = arquivo, subtitulo = subtitulo)


