from UtilsD import escolhaM
from AcoesD import distribuirTarefasM
from UtilsD.impressaoMenusM import Impressao_De_Menus
from Dir_BancoDeDados.criarBancoDadosM import Criar_Banco_Dados


def Tarefas_Para_Amanha(funcao, titulo, traco="=", comprimentoDoTraco=50):
    titulo = funcao
    Impressao_De_Menus(traco = traco, comprimentoDoTraco = comprimentoDoTraco, titulo = titulo, itensMenu = None)
    
    input("Momentâneamente isolada.\nQualquer tecla para voltar")
    return