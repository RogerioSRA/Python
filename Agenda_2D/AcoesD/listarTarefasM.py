import os
from datetime import date
from menuD.tracoM import Traco
from menuD.tituloM import Titulo
from bancoDadosD.resgataBancoDadosM import ResgataBancoDados


def Listar_Tarefas(local, pergunta, tarefa, titulo, retorno, arquivo, subtitulo = "Listando Tarefas"):
    # local = pacote[0]
    # pergunta = pacote[1]
    # tarefa = pacote[2]
    # titulo = pacote[3]
    # retorno = pacote[4]
    # arquivo = pacote[5]
    # subtitulo = "Listando Tarefas"


    # Monta cabeçalho/título
    os.system("clear")
    comprimentoTraco = 94
    Traco("=", comprimentoTraco)
    Titulo(titulo, comprimentoTraco)
    Traco("=", comprimentoTraco)
    Titulo(subtitulo, comprimentoTraco)
    Traco("=", comprimentoTraco)
    print()


    # Verifica existência e resgata dados
    # arquivo = arquivo.split("/")
    # arquivo = arquivo[1]
    bdados = ResgataBancoDados(arquivo)
    if bdados == False:
        return # Distribuir_Tarefas()
    print(f"{'Posição':<13}{'Data':<13}{'Tarefa':<50}{'Dias de registro':>18}")
    print()
    cores = "0"
    bancoDados = open(arquivo, "rt")
    for acao in bancoDados:
        acao = acao.split(";")
        posicao = acao[0]
        data = acao[1]
        acao = acao[2].split("\n")
        acao = acao[0]
        dataDeAtraso = data.split("-")
        diasDeAtraso = date.today() - date(int(dataDeAtraso[2]), int(dataDeAtraso[1]), int(dataDeAtraso[0]))
        diasDeAtraso = str(diasDeAtraso).split(",")
        diasDeAtraso = str(diasDeAtraso[0]).split(" ")
        if diasDeAtraso[0] == "0:00:00": diasDeAtraso[0] = ""; dias = "Hoje"
        elif int(diasDeAtraso[0]) > 1 : dias = "dias"
        else: dias = "dia "
        if cores == "\033[4;32m": cores = "\033[4;34m"
        else: cores = "\033[4;32m"
        print(f"{cores}{posicao:<13}{data:<13}{acao[:50]:<55}{diasDeAtraso[0]:>8}{dias:>5}\033[m")
        print()
    print()
    input("Qualquer tecla para continuar")
    return posicao
    # return retorno(local = local, pergunta = pergunta, tarefa = tarefa, titulo = titulo, retorno = retorno, arquivo = arquivo, subtitulo = subtitulo)


    