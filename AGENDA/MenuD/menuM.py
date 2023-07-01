from UtilsD import escolhaM
from AcoesD.distribuirTarefasM import Distribuir_Tarefas
from AcoesD.adicionarTarefaM import Adicionar_Tarefas
from UtilsD.impressaoMenusM import Impressao_De_Menus
from Dir_BancoDeDados.resgataDadosM import ResgataDados
from AcoesD.tarefasParaAmanhaM import Tarefas_Para_Amanha
from AcoesD.adicionarLocalM import Adicionar_Local_Para_Tarefas
from UtilsD.inicioM import Arquivos_Iniciais



def Menu():
    pacote = Arquivos_Iniciais()
    # opcoesDoMenu, arquivo_OpcoesDoMenu, banco_de_dados_para_BancoDeDados, caminho
    arquivo_OpcoesDoMenu = pacote[1]
    itensMenu = ResgataDados(arquivo_OpcoesDoMenu)
    titulo = "MENÚ AGENDA"
    qtd_opcoes, menu = Impressao_De_Menus(titulo=titulo, itensMenu=itensMenu)
    escolha = escolhaM.Escolha("O que deseja fazer ? : ", max = qtd_opcoes)
    escolha -= 1
    funcao = escolhaM.Validar_Escolha(menu[escolha], operacao = 1)
    if escolha == 0: Adicionar_Local_Para_Tarefas(titulo=titulo)
    else: Distribuir_Tarefas(funcao=funcao)
    Menu()

    



