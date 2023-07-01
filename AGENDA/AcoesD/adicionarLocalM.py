from MenuD import menuM
from UtilsD import escolhaM
from UtilsD.impressaoMenusM import Impressao_De_Menus
from Dir_BancoDeDados.criarBancoDadosM import Acrescenta_Novo_Local, Criar_Banco_Dados
from UtilsD.inicioM import Arquivos_Iniciais


def Adicionar_Local_Para_Tarefas(titulo=""):


    Impressao_De_Menus(titulo = titulo, subtitulo = "Adicionar Local para tarefas")


    novoLocal = input("Entre com o nome do novo local para tarefas: ")
    escolha = escolhaM.Escolha("Este nome está correto ? : 1-Sim 2-Não : ", 1, 2)
    if escolha == 2: return Adicionar_Local_Para_Tarefas(titulo)
    else:
        novoLocal = escolhaM.Validar_Escolha(novoLocal, operacao = 2)
        dados = Arquivos_Iniciais()
        arquivo_OpcoesDoMenu = dados[1]
        caminho = dados[3]
        # print(caminho, arquivo_OpcoesDoMenu, novoLocal)
        # input()
        data = Acrescenta_Novo_Local(caminho, arquivo_OpcoesDoMenu, novoLocal = novoLocal)


    cor_In = "\033[4m"; cor_Out = "\033[m"
    print(f"\nLocal {cor_In}{novoLocal}{cor_Out} registrado em {cor_In}{data}{cor_Out} e pronto para uso.")
    escolha = escolhaM.Escolha("Gostaria de registrar um novo local ? : 1-Sim 2-Não : ", 1, 2)
    if escolha == 1: return Adicionar_Local_Para_Tarefas(titulo)
    else: return menuM.Menu()



