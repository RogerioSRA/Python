from AcoesD.locaisM import Locais


def Abrir_Criar_Arquivo(arquivos):
    arquivoParaRetorno = []
    for arquivo in arquivos:
        arquivo = Locais(arquivo)
        arquivoParaRetorno.append(arquivo)
        try:
            bancoDados = open(arquivo, "rt")
            bancoDados.close()
        except:
            bancoDados = open(arquivo, "xt")
            bancoDados.close()
    return arquivoParaRetorno


