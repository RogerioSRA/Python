import sys, os, construtor
from escolha import Escolha

path_ = construtor.path_
path_perm = construtor.path_perm
path_backup = construtor.path_backup


def Direciona(funcao=None, lista=None, extratitle=None, menu=None):
    eval(funcao)(lista=lista)
    Organiza_Lista(lista)


def Apagar(lista=None):
    while True:
        nome = input(f'Entre com o número ou nome do contato da lista que deseja apagar ? : ')
        match nome:
            case '1': sys.exit()
            case '2': return
        if (nome.replace(' ', '').isalnum()): nome = nome.title()
        check, row = Confere_Contato_Existe(nome=nome, telefone=nome, lista=lista)
        if (check == None):
            input(f'Não existe contato registrado com este {check}...')
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        # confere se é mesmo o contato
        print(f"\n\n{'Nome:':<50}{'Telefone:':>12}")
        print('+'+49*"-"+'+'+19*'-'+'+')
        print(f"|{row.split(';')[0][:48]:<49}{'|'}{row.split(';')[1]:>19}{'|':<19}")
        print('+'+49*"-"+'+'+19*'-'+'+')
        resposta = Escolha('É este o contato a ser apagado', sn=True)
        print()
        if (resposta == 2):
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        break
    # se existe, verifica 
    # se estiver vazia ou for autorizado, apaga do menú
    row_perm = row
    a_nome = row_perm.split(';')[0]
    a_telefone = row_perm.split(';')[1]
    with open(path_+lista, 'r') as arq:
        with open(path_backup+lista, 'w') as arqB:
            for row in arq:
                if (row.split(';')[0] == nome or row.split(';')[1] == nome): continue
                arqB.write(row)
    with open(path_+lista, 'w') as arq:
        with open(path_backup+lista, 'r') as arqB:
            for row in arqB:
                arq.write(row)
    print(f"\nContato de nome {a_nome} e telefone {a_telefone} apagado com sucesso  !")
    input("Tecle <ENTER> para voltar ..")
    return


def Editar(lista=None):
    while True:
        nome = input('Qual o nome ou número do contato a ser editado ? : ')
        match nome:
            case '1': sys.exit()
            case '2': return
        if (nome.replace(' ', '').isalnum()): nome = nome.title()
        check, row = Confere_Contato_Existe(nome=nome, telefone=nome, lista=lista)
        if (check == None):
            print(f'Não existe contato registrado para essa busca...')
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        # se existir
        print(f"\n\n{'Nome:':<50}{'Telefone:':>12}")
        print('+'+49*"-"+'+'+19*'-'+'+')
        print(f"|{row.split(';')[0][:48]:<49}{'|'}{row.split(';')[1]:>19}{'|':<19}")
        print('+'+49*"-"+'+'+19*'-'+'+')
        resposta = Escolha('Este é o contato que gostaria de editar', sn=True)
        print()
        if (resposta == 2):
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        break
    row_perm = row
    a_nome = row_perm.split(';')[0]
    a_telefone = row_perm.split(';')[1]
    n_nome = a_nome
    n_telefone = a_telefone
    while True:
        novo_nome = input(f'Qual o novo {check} deseja para o contato de {check} {nome} ? : ')
        match novo_nome:
            case '1': sys.exit()
            case '2': return
        if (novo_nome.replace(' ', '').isalnum()): novo_nome = novo_nome.title()
        check, row = Confere_Contato_Existe(nome=novo_nome, telefone=novo_nome, lista=lista)
        if (check != None):
            print()
            print(f"\n\n{'Nome:':<50}{'Telefone:':>12}")
            print('+'+49*"-"+'+'+19*'-'+'+')
            print(f"|{row.split(';')[0][:48]:<49}{'|'}{row.split(';')[1]:>19}{'|':<19}")
            print('+'+49*"-"+'+'+19*'-'+'+')
            print(f'Já existe contato registrado com este {check}...')
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        break
    # cria um backup já com o novo nome da lista
    with open(path_+lista, 'r') as arq:
        with open(path_backup+lista, 'w') as arqB:
            for row in arq:
                if (row.split(';')[0] == nome):
                    row = novo_nome+';'+row_perm.split(';')[1]+';'+'\n'
                    n_nome = novo_nome
                if (row.split(';')[1] == nome):
                    row = row_perm.split(';')[0]+';' + novo_nome+';'+'\n'
                    n_telefone = novo_nome
                arqB.write(row)
    # recria menú inicial já com a lista editada
    with open(path_+lista, 'w') as arq:
        with open(path_backup+lista, 'r') as arqB:
            for row in arqB:
                arq.write(row)
    print(f"\nContato (nome: {a_nome}, telefone {a_telefone}) editado para (nome: {n_nome}, telefone {n_telefone}) com sucesso  !")
    input("Tecle <ENTER> para voltar ..")
    return


def Listar(lista=None):
    with open(path_+lista, 'r') as arq:
        if (arq.readline() != ''):
            with open(path_+lista, 'r') as arq:
                print(f"{'  Nome:':>2}{'Telefone:':>55}")
                for registro in arq:
                    print('+'+49*"-"+'+'+19*'-'+'+')
                    print(f"|{registro.split(';')[0][:48]:<49}{'|'}{registro.split(';')[1]:>19}{'|':<19}")
                print('+'+49*"-"+'+'+19*'-'+'+')
        else:
            print("Não existe registro nesta lista telefônica.")
        input("\n\nTecle <ENTER> para voltar ..")


def Cadastrar(lista=None):
    while True:
        # registra um contato
        nome = input('Entre com o nome do contato : ')
        match nome:
            case '1': sys.exit()
            case '2': return
        if (nome.replace(' ', '').isalnum()): nome = nome.title()
        check, row = Confere_Contato_Existe(nome=nome, lista=lista)
        if (check != None):
            print(f"\n\n{'Nome:':>2}{'Telefone:':>55}")
            print('+'+49*"-"+'+'+19*'-'+'+')
            print(f"|{row.split(';')[0][:48]:<49}{'|'}{row.split(';')[1]:>19}{'|':<19}")
            print('+'+49*"-"+'+'+19*'-'+'+')
            print(f'Este {check} já está registrado na lista ...')
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        break
    while True:
        telefone = input('Entre com o número de telefone : ')
        match telefone:
            case '1': sys.exit()
            case '2': return
        check, row = Confere_Contato_Existe(telefone=telefone, lista=lista)
        # se existir, avisa e retorna
        if (check != None):
            print(f"\n\n{'Nome:':>2}{'Telefone:':>55}")
            print('+'+49*"-"+'+'+19*'-'+'+')
            print(f"|{row.split(';')[0][:48]:<49}{'|'}{row.split(';')[1]:>19}{'|':<19}")
            print('+'+49*"-"+'+'+19*'-'+'+')
            print(f'Este {check} já está registrado na lista ...')
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        break
    #se não existir, acrescenta contato à lista selecionada
    diretorio=[path_, path_backup, path_perm]
    for dir in diretorio:
        with open(dir+lista, 'a') as arq:
            arq.write(nome+';'+telefone+';'+'\n')
        arq.close()
    print(f"\nContato de nome {nome} e telefone {telefone} registrado com sucesso  !")
    input("Tecle <ENTER> para voltar ..")
    return


def Encontrar(lista=None):
    while True:
        nome = input('Qual o nome ou número do contato que gostaria de encontrar ? : ')
        match nome:
            case '1': sys.exit()
            case '2': return
        if (nome.replace(' ', '').isalnum()): nome = nome.title()
        check, row = Confere_Contato_Existe(nome=nome, telefone=nome, lista=lista)
        if (check == None):
            print(f'Não existe contato registrado para essa busca...')
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        # se existir
        print(f"\n\n{'Nome:':>2}{'Telefone:':>55}")
        print('+'+49*"-"+'+'+19*'-'+'+')
        print(f"|{row.split(';')[0][:48]:<49}{'|'}{row.split(';')[1]:>19}{'|':<19}")
        print('+'+49*"-"+'+'+19*'-'+'+')
        print()
        resposta = Escolha('Este é o contato procurado', sn=True)
        print()
        if (resposta == 2):
            resposta = Escolha('Gostaria de tentar novamente', sn=True)
            print()
            if (resposta == 1): continue
            else: return
        break
    input("Tecle <ENTER> para voltar ..")


def Confere_Contato_Existe(nome=None, telefone=None, lista=None):
    check = None
    row = None
    nomes_encontrados = []
    with open(path_+lista, 'r') as arq:
        if(arq.readline() != ''):
            with open(path_+lista, 'r') as arq:
                for row in arq:
                    contato = row.split(';')[0]
                    contato = contato.split()
                    for item in contato:
                        if (item == nome):
                            check = 'nome'
                            nomes_encontrados.append(row)
                        elif (row.split(';')[1] == telefone): check = 'número'; break
    if (len(nomes_encontrados) > 1):
        print(f"{'No':<7}{'nome:':<50}")
        for pos, registro in enumerate(nomes_encontrados):
            print('+'+5*"-"+'+'+63*'-'+'+')
            print(f"|{pos:<5}{'|'}{registro.split(';')[0][:48]:<63}{'|':<63}")
        print('+'+5*"-"+'+'+63*'-'+'+')
        print("Foram encontrados mais de um registro com o mesmo nome.")
        while True:
            num = input("Entre com o número que representa o contato desejado : ")
            if (num.isdecimal()):
                num = int(num)
                row = nomes_encontrados[num]
                break
            else: continue
    return check, row


def Organiza_Lista(lista=None):
    lista_array = []
    with open(path_+ lista, 'r') as arq:
        for item in arq:
            lista_array.append(item)
    lista_array.sort()
    with open(path_backup + lista, 'w') as arqBkp:
        for item in lista_array:
            arqBkp.write(item)
    with open(path_ + lista, 'w') as arq:
        for item in lista_array:
            arq.write(item)

