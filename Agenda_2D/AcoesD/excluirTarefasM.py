import os
from menuD.tracoM import Traco
from menuD.tituloM import Titulo
from utilsD.escolhaM import Escolha
from AcoesD.listarTarefasM import Listar_Tarefas
from bancoDadosD.resgataBancoDadosM import ResgataBancoDados
from bancoDadosD.excluiBancoDadosTarefasM import Excluir_BancoDados


def Excluir_Tarefa(local, pergunta, tarefa, titulo, retorno, arquivo, subtitulo):

    # local = pacote[0]
    # pergunta = pacote[1]
    # tarefa = pacote[2]
    # titulo = pacote[3]
    # retorno = pacote[4]
    # arquivo = pacote[5]
    # subtitulo = pacote[6]
    os.system("clear")
    Traco("=")
    Titulo(titulo)
    Traco("=")
    subtitulo = " Excluindo Tarefas "
    Titulo(subtitulo)
    Traco("=")
    print()


    # Lista as Tarefas
    subtitulo = "Exlcuindo Tarefas"
    retorno = Excluir_Tarefa
    posicao = Listar_Tarefas(local = local, pergunta = pergunta, tarefa = tarefa, titulo = titulo, retorno = retorno, arquivo = arquivo, subtitulo = subtitulo)
    pergunta = "Qual a posição da tarefa a ser excluída ? : "
    escolha = Escolha(pergunta, 1, int(posicao))


    excluido = Excluir_BancoDados(local = local, arquivo = arquivo, escolha = str(escolha))
    print("Tarefa excluída:\n"+str(excluido))
    print("Deseja excluir outra tarefa ? : ")
    exit()


