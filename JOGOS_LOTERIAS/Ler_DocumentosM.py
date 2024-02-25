import os
os.system("clear")
import ConstrutorM as cttm


def Ler_DocumentosF(nomeDoJogo=""):
    try:
        with open(cttm.path_ + nomeDoJogo + ".txt", 'r') as lendoArquivo:
            jogosDocumentados, qtdDeJogos = Criar_Array_De_Jogos_Prontos(nomeDoJogo)
            return jogosDocumentados, qtdDeJogos
    except:
        return [], 0


def Criar_Array_De_Jogos_Prontos(nomeDoJogo):
    with open(cttm.path_ + nomeDoJogo + ".txt", 'r') as lendoArquivo:
        array = []
        qtdDeJogos = 0
        jogosDocumentados = []
        for line in lendoArquivo.readlines():
            if (line[0] != "/" and line[0] != "=" and line.split("\n").__contains__("\n") == False):
                line = line.split("\n")[0]
                for num in line.split(", "):
                    array += [int(num)]
                jogosDocumentados += [array]
                qtdDeJogos += 1
                array = []
        return jogosDocumentados, qtdDeJogos
    
    