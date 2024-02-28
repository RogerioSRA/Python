import sys, os, construtor
from escolha import Escolha

path_ = construtor.path_
path_perm = construtor.path_perm
path_backup = construtor.path_backup
menu_inicial_bn = construtor.menu_inicial_bn


def Menu_Inicial(ini=False):
    menu_inicial = ['Sair', 'Apagar', 'Editar', 'Cadastrar']
    if (ini == True):
        with open(path_+menu_inicial_bn, "r") as arq:
            for opcao in arq:
                menu_inicial.append(opcao.split()[0])
    return menu_inicial


def Direciona(funcao):
    eval(funcao)()


def Apagar():
    nome_lista = input(f"Entre com o nome da lista que deseja apagar ? : ")
    match nome_lista:
        case "1": sys.exit()
        case "2": return
    if (nome_lista.isalnum()): nome_lista = nome_lista.title()
    check = Confere_Lista_Existe(nome_lista)
    if (check == False): input("Não existe lista registrada com este nome..."); return
    # se existe, verifica se está vazia, se não, pede autorização
    with open(path_+nome_lista, 'r') as arq:
        if (arq.readline() != ''):
            resposta = Escolha(pergunta="Essa lista não está vazia, gostaria de apagá-la mesmo assim", sn=True)
            if (resposta == 2): return
    # se estiver vazia ou for autorizado, apaga do menú
    with open(path_+menu_inicial_bn, 'r') as arq:
        with open(path_backup+menu_inicial_bn, 'w') as arqB:
            for row in arq:
                if (row.split()[0] == nome_lista): continue
                arqB.write(row)
    with open(path_+menu_inicial_bn, 'w') as arq:
        with open(path_backup+menu_inicial_bn, 'r') as arqB:
            for row in arqB:
                arq.write(row)
    # apaga do diretório
    os.remove(path_+nome_lista)
    os.remove(path_backup+nome_lista)
    print()
    print(f"Lista telefônica de nome {nome_lista} apagada com sucesso !!")
    input("Tecle <ENTER> para voltar ..")


def Editar():
    nome_lista = input("Qual o nome da lista a ser editado ? : ")
    match nome_lista:
        case "1": sys.exit()
        case "2": return
    if (nome_lista.isalnum()): nome_lista = nome_lista.title()
    check = Confere_Lista_Existe(nome_lista)
    if (check == False): input("Não existe lista registrada com este nome..."); return
    # se existir
    novo_nome = input(f"Qual o novo nome deseja para lista {nome_lista} ? : ")
    match novo_nome:
        case "1": sys.exit()
        case "2": return
    if (novo_nome.isalnum()): novo_nome = novo_nome.title()
    # cria um backup já com o novo nome da lista
    with open(path_+menu_inicial_bn, 'r') as arq:
        with open(path_backup+menu_inicial_bn, 'w') as arqB:
            for row in arq:
                if (row.split()[0] == nome_lista):
                    row = novo_nome+"\n"
                arqB.write(row)
    # recria menú inicial já com a lista editada
    with open(path_+menu_inicial_bn, 'w') as arq:
        with open(path_backup+menu_inicial_bn, 'r') as arqB:
            for row in arqB:
                arq.write(row)
    # renomeia o diretório
    os.rename(path_+nome_lista, path_+novo_nome)
    os.rename(path_perm+nome_lista, path_perm+novo_nome)
    os.rename(path_backup+nome_lista, path_backup+novo_nome)
    print()
    print(f"Nome de lista telefônica {nome_lista} editada para {novo_nome} com sucesso !!")
    input("Tecle <ENTER> para voltar ..")


def Cadastrar():
    # ADICIONA O NOME DA lista AO MENÚ INICIAL
    nome_lista = input("Qual nome deseja para a lista ? : ")
    match nome_lista:
        case "1": sys.exit()
        case "2": return
    if (nome_lista.isalnum()): nome_lista = nome_lista.title()
    check = Confere_Lista_Existe(nome_lista)
    # se não existir, a lista será adicionada ao menú principal
    if (check == True):
        input("Já existe uma lista com este nome ...")
        return
    with open(path_+menu_inicial_bn, "a") as arq:
        arq.write(nome_lista+"\n")

    # CRIA A lista COMO ARQUIVO
    with open(path_+nome_lista, 'x') as arq: pass
    with open(path_backup+nome_lista, 'x') as arq: pass
    try:
        with open(path_perm+nome_lista, 'x') as arq: pass
    except:pass
    Menu_Inicial()
    print()
    print(f"Nova lista telefônica de nome {nome_lista} criada com sucesso !!")
    input("Tecle <ENTER> para voltar ..")

def Confere_Lista_Existe(nome_lista):
    check = False
    with open(path_+menu_inicial_bn, 'r') as arq:
        for row in arq:
            if (row.split()[0] == nome_lista): check = True; break
    return check

