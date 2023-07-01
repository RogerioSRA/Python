from UtilsD import escolhaM
from AcoesD import distribuirTarefasM
from UtilsD.impressaoMenusM import Impressao_De_Menus
from Dir_BancoDeDados.criarBancoDadosM import Criar_Banco_Dados


def Adicionar_Tarefas(funcao, titulo = ""):
    if titulo == "": titulo = funcao
    Impressao_De_Menus(titulo = titulo, itensMenu = None, subtitulo = "Adicionar tarefas")
    novaTarefa = input("Entre com a nova tarefa: ")
    escolha = escolhaM.Escolha("Essa tarefa está correta ? : 1-Sim 2-Não : ", 1, 2)
    if escolha == 2: return Adicionar_Tarefas(titulo)
    else:
        titulo = escolhaM.Validar_Escolha(titulo, operacao = 1)
        novaTarefa = escolhaM.Validar_Escolha(novaTarefa, operacao = 2)
        data = Criar_Banco_Dados(banco_de_dados_para_BancoDeDados = "", arquivo_OpcoesDoMenu = titulo, novaTarefa = novaTarefa)
    cor_In = "\033[4m"; cor_Out = "\033[m"
    print(f"\nTarefa {cor_In}{novaTarefa}{cor_Out} registrada em {cor_In}{data}{cor_Out}.")
    escolha = escolhaM.Escolha("Gostaria de registrar uma nova tarefa ? : 1-Sim 2-Não : ", 1, 2)
    if escolha == 1: return Adicionar_Tarefas(titulo)
    else: 
        return distribuirTarefasM.Distribuir_Tarefas(funcao=titulo)



