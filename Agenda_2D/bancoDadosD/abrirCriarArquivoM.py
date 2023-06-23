def Abrir_Criar_Arquivo(arquivos):
    arquivoParaRetorno = []
    pos = 0
    for arquivo in arquivos:
        arquivo = f"AgendaPython/{arquivo}"
        arquivoParaRetorno.append(arquivo)
        pos =+ 1
        try:
            print(arquivo)
            bancoDados = open(arquivo, "rt")
            bancoDados.close()
        except:
            print(arquivo)
            bancoDados = open(arquivo, "xt")
            bancoDados.close()
    return arquivoParaRetorno