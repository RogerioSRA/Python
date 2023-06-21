def Abrir_Criar_Arquivo(pacote):
    try:
        bancoDados = open(pacote[0], "rt")
        bancoDados.close()
    except:
        bancoDados = open(pacote[0], "x")
        bancoDados.close()