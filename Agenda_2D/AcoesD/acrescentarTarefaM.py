import os
from time import sleep
from datetime import date
from menuD.tracoM import Traco
from menuD.tituloM import Titulo
from AcoesD.locaisM import Locais
from utilsD.escolhaM import Escolha
from AcoesD import distribuirTarefasM
from AcoesD.salvaPacotesM import Salva_Pacotes
from bancoDadosD.registraBancoDadosTarefasM import RegistraBancoDadosTarefas


def Acrescentar_Tarefa(local, pergunta, tarefa, titulo, retorno, arquivo, subtitulo):

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
    subtitulo = " Adicionando Tarefas "
    Titulo(subtitulo)
    Traco("=")    
    tarefa = input("Qual o nome da tarefa ? : \n",)
    tarefa = tarefa.capitalize()
    frase = "Está correto este nome ? 1-Sim  2-Não : "
    escolha = Escolha(frase, 1, 2)
    if escolha == 1:
        pacoteAcrescenta = [arquivo, tarefa]
        RegistraBancoDadosTarefas(pacoteAcrescenta)
        print(f"\nTarefa registrada na data de {date.today().day}-{date.today().month}-{date.today().year}")
        frase = "Gostaria de um novo registro ? : 1-Sim  2-Não : "
        escolha = Escolha(frase, 1, 2)
        if escolha == 1: return Acrescentar_Tarefa(local = local, pergunta = pergunta, tarefa = tarefa, titulo = titulo, retorno = retorno, arquivo = arquivo, subtitulo = subtitulo)
        else:
            # pacoteBairro = Salva_Pacotes(local, pergunta)
            # print(pacoteBairro)
            return distribuirTarefasM.Distribuir_Tarefas(local = local, pergunta = pergunta, tarefa = tarefa, titulo = titulo, retorno = retorno, arquivo= arquivo, subtitulo=subtitulo)
    if escolha == 2: return Acrescentar_Tarefa(local = local, pergunta = pergunta, tarefa = tarefa, titulo = titulo, retorno = retorno, arquivo = arquivo, subtitulo = subtitulo)


    
    