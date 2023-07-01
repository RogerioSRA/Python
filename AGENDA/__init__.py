from MenuD.menuM import Menu
from Dir_BancoDeDados.criarBancoDadosM import Criar_Banco_Dados
from UtilsD.inicioM import Arquivos_Iniciais


# def Arquivos_Iniciais():
pacote_arquivos_iniciais = Arquivos_Iniciais()
opcoesDoMenu = pacote_arquivos_iniciais[0]
arquivo_OpcoesDoMenu = pacote_arquivos_iniciais[1]
banco_de_dados_para_BancoDeDados = pacote_arquivos_iniciais[2]
caminho = pacote_arquivos_iniciais[3]
Menu()


