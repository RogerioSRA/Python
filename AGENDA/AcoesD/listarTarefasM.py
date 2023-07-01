from UtilsD.escolhaM import Validar_Escolha
from UtilsD.impressaoMenusM import Impressao_De_Menus
from Dir_BancoDeDados.resgataDadosM import ResgataDados


def Listar_Tarefas(funcao, titulo="", subtitulo = "Listar tarefas"):
    if titulo == "": titulo = funcao
    Impressao_De_Menus(titulo = titulo, subtitulo = subtitulo)
    arquivo = Validar_Escolha(titulo, operacao=1)
    arquivo = ResgataDados(arquivo)
    arquivo = str(arquivo)
    # print("Listar Tarefas")
    # input()
    qtdTarefas = 0
    if arquivo != "False":
        bdados = open(arquivo, "rt")
        print(f"{'Posição':<10}{'Tarefa':<45}{'Data de Entrada'}"[:70])
        print()
        for tarefa in bdados:
            qtdTarefas += 1
        if qtdTarefas > 0:
            bdados = open(arquivo, "rt")
            for dado in bdados:
                dadoS = str(dado).split(";")
                dadoS[2] = dadoS[2].split("\n")[0]
                print(f"{dadoS[0]:>3}{'--':>4}{'':<3}{dadoS[1][:46]:.<48}{dadoS[2]:.>0}"[0:70])
            print()
        else:
            arquivo = "False"
    if arquivo == "False":
        print("Não existem tarefas registradas para este local.")
        print()
    if subtitulo == "Listar tarefas" or arquivo == "False":
        input("Qualquer tecla para voltar: ")
    titulo_boolV = [titulo, arquivo, qtdTarefas]
    return titulo_boolV


