def ResgataBancoDados(arquivo):
    # print(arquivo)
    dados = []
    try:
        bdados = open(arquivo, "rt")
        for dado in bdados:
            dado = dado.split("\n")
            dados.append(dado[0])
        return dados
    except:
        input("Não existem tarefas registradas neste local\nQualquer tecla para voltar : ")
        return False


    