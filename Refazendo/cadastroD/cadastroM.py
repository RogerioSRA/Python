def Cadastro():
    print("Cadastro")
    bancoDados = "NovoBancoDados"
    complemento = ".txt"
    CriarArquivo(bancoDados, complemento)


def CriarArquivo(nomeArquivo, complemento):
    try:
        bancoDados = open(nomeArquivo+complemento, "rt")
        bancoDados.close()
        print("Try")
    except:
        bancoDados = open(nomeArquivo+complemento, "xt+")
        bancoDados.close()
        print("except")
    else:
        print("Else")
        return
Cadastro()