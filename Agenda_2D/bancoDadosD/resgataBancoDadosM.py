def ResgataBancoDados(arquivo):
    dados = []
    bdados = open(arquivo, "rt")
    for dado in bdados:
        dado = dado.split("\n")
        dados.append(dado[0])
    return dados

    