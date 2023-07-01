from MenuD import menuM
from UtilsD.escolhaM import *
from AcoesD.listarTarefasM import Listar_Tarefas
from AcoesD.excluirTarefaM import Excluir_Tarefas
from UtilsD.impressaoMenusM import Impressao_De_Menus
from AcoesD.adicionarTarefaM import Adicionar_Tarefas
from AcoesD.tarefasParaAmanhaM import Tarefas_Para_Amanha


def Distribuir_Tarefas(funcao, titulo=""):
    itensMenu = ["", "Adicionar Tarefas", "Excluir Tarefas", "Listar Tarefas", "Voltar", "Sair"]
    funcao = Validar_Escolha(funcao, operacao = 2)
    subtitulo = ""
    if titulo != "": subtitulo=funcao
    else: titulo = funcao
    qtd_opcoes = Impressao_De_Menus(titulo=titulo, itensMenu=itensMenu, subtitulo=subtitulo)
    escolha = Escolha("O que deseja fazer ? : ", max = qtd_opcoes)


    if escolha == len(itensMenu) - 2: return menuM.Menu()
    funcao = Validar_Escolha(itensMenu[escolha], operacao = 1)
    # input(funcao)
    titulo_boolV = eval(funcao)(titulo)
    funcao = titulo_boolV[0]
    Distribuir_Tarefas(funcao)



