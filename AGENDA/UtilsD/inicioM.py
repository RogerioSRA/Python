from Dir_BancoDeDados.criarBancoDadosM import Criar_Banco_Dados


def Arquivos_Iniciais():


    # Primeiras opções do menu
    opcoesDoMenu = ["", "Adicionar Local para tarefas", "Tarefas para amanhã", "Sair"]


    # Define nome banco de dados para opções do menu
    arquivo_OpcoesDoMenu = "Menu_Opcoes" # .txt


    # Define nome banco de dados geral para banco de dados
    banco_de_dados_para_BancoDeDados = "Banco_De_Dados_Geral"


    # Cria Banco de Dados Geral, Banco de Dados com opções de Menu e salva as opções existentes
    caminho = Criar_Banco_Dados(opcoesDoMenu = opcoesDoMenu)


    pacote_arquivos_iniciais = [opcoesDoMenu, arquivo_OpcoesDoMenu, banco_de_dados_para_BancoDeDados, caminho]
    return pacote_arquivos_iniciais


