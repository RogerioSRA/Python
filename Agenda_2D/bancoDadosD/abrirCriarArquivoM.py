def Abrir_Criar_Arquivo(arquivos):
    for arquivo in arquivos:
        try:
            bancoDados = open(arquivo, "rt")
            bancoDados.close()
        except:
            bancoDados = open(arquivo, "xt")
            bancoDados.close()