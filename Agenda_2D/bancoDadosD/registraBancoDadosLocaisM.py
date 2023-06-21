def RegistraBancoDadosLocais(pacote, tarefa):
    bancoDados = open(pacote[0], 'at')
    bancoDados.write(tarefa + "\n")
    bancoDados.close()