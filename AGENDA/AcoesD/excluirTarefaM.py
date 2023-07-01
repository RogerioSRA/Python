from AcoesD.listarTarefasM import Listar_Tarefas
from UtilsD.escolhaM import Escolha
from UtilsD.inicioM import Arquivos_Iniciais
from UtilsD.impressaoMenusM import Impressao_De_Menus
from Dir_BancoDeDados.excluirDadosM import Excluir_Dados


def Excluir_Tarefas(funcao, titulo=""):
    if titulo == "": titulo = funcao
    Impressao_De_Menus(titulo=titulo, itensMenu=None, subtitulo = "Excluir tarefas")


    # Busca e imprime a lista do 'Local' desejado
    # print("Excluir tarefas")
    # input()
    titulo_boolV = Listar_Tarefas(funcao, titulo=titulo, subtitulo="Excluir tarefas")
    # titulo_boolV=[titulo, true/false, qtd de tarefas em um arquivo]
    titulo = titulo_boolV[0]
    boolV = titulo_boolV[1]
    qtdTarefas = titulo_boolV[2]
    if boolV == "False":
        return titulo_boolV
    else:
        # Leva para o banco de dados, busca o arquivo e apaga
        if qtdTarefas > 1:
            tarefaExcluir = input("Qual a posição da tarefa a ser excluída ? : ")
        if qtdTarefas == 1:
            tarefaExcluir = Escolha("Gostaria de excluir essa tarefa ? 1-Sim 2-Não: ", 1, 2)
            if tarefaExcluir == 2:
                input("Tarefa \033[31mNÃO\033[m excluída.\nQualquer tecla para voltar: ")
                return titulo_boolV
            else:
                tarefaExcluir = str(tarefaExcluir)
        if tarefaExcluir.isnumeric() == False or int(tarefaExcluir) < 1 or int(tarefaExcluir) > qtdTarefas: return Excluir_Tarefas(titulo)
        caminho = Arquivos_Iniciais()
        caminho = caminho[3]
        Excluir_Dados(caminho=caminho, titulo=titulo, tarefaExcluir=tarefaExcluir)


        print(f"Tarefa da posição {tarefaExcluir} excluída")
        print()
        qtdTarefas -= 1
        if qtdTarefas > 0:
            escolha = Escolha("Gostaria de excluir outra tarefa ? : ", 1, 2)
        else:
            escolha = 2
            input("Qualquer tecla para voltar: ")
    if escolha == 1: return Excluir_Tarefas(titulo)
    else: return titulo_boolV


