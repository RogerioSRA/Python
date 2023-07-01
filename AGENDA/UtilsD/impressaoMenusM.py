import os
from datetime import date
from UtilsD.escolhaM import Validar_Escolha
from Dir_BancoDeDados.resgataDadosM import ResgataDados


def Impressao_De_Menus(traco="=", comprimentoDoTraco=70, titulo="Não Informado", itensMenu=None, subtitulo=""):
    os.system("clear")
    print(traco*comprimentoDoTraco)
    print(" " * (int(comprimentoDoTraco/2 - len(titulo)/2)) + titulo)
    print(traco*comprimentoDoTraco)


    if subtitulo != "":
        print(" " * (int(comprimentoDoTraco/2 - len(subtitulo)/2)) + subtitulo)
        print(traco*comprimentoDoTraco)


    print()
    
    
    if type(itensMenu) == str:
        # print("String")
        qtd_opcoes = -1
        menu = []
        if itensMenu != None:
            pos = 1
            cor_in = "\033[m"
            cor_out = "\033[m"
            bdados = open(itensMenu)
            for item in bdados:
                if item == "" or item == "\n": continue
                item = item.split("\n")[0]
                if item == "Sair": pos = 0; print()
                if item == "Adicionar Local para tarefas" or item == "Tarefas para amanhã": cor_in = "\033[033m"
                if qtd_opcoes >=1 and item != "Voltar" and item != "Sair": cor_in = Confere_Data(item)
                print(f"{pos:>3} - {cor_in}{item}{cor_out}")
                cor_in = cor_out
                menu.append(item)
                qtd_opcoes += 1
                pos += 1
            bdados.close()
        print()
        return qtd_opcoes, menu

    if type(itensMenu) == list:
        print("List")
        qtd_opcoes = -1
        menu = []
        if itensMenu != "Vazio":
            pos = 1
            for item in itensMenu:
                if item == "": continue
                if item == "Sair": pos = 0; print()
                print(f"{pos:>3} - {item}")
                pos += 1
                qtd_opcoes += 1
        print()
        return qtd_opcoes
    
def Confere_Data(item):    
    cor_in = "\033[m"
    funcao = item
    # input(item)
    funcao = Validar_Escolha(funcao, operacao=2)
    funcao = Validar_Escolha(funcao, operacao=1)
    # print(funcao)
    funcao = ResgataDados(funcao)
    if funcao == False: return cor_in
    # input(funcao)


    try:
        arquivo = open(funcao, "rt")
        for dado in arquivo:
            dado = dado.split(";")[2].split("\n")[0].replace("(","").replace(")","")
            if dado < date.today().strftime('%d-%m-%Y'): cor_in = "\033[31m"
        arquivo.close()
        return cor_in
    except:
        return cor_in


