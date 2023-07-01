from UtilsD.inicioM import Arquivos_Iniciais


def ResgataDados(requisicao):
    caminho = Arquivos_Iniciais()[3]
    requisicao = caminho+requisicao+".txt"
    try:
        entrega = open(requisicao, "rt")
        entrega.close()
        return requisicao
    except:
        return False
    

    