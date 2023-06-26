from time import sleep
from AcoesD.locaisM import Locais


def Salva_Pacotes(*pacote):

    local = pacote[0]
    pergunta = pacote[1]
    # tarefa = pacote[2]
    # titulo = pacote[3]
    # retorno = pacote[4]
    # arquivo = pacote[5]
    # subtitulo = pacote[6]
    arquivoPacote = Locais("Salva-Pacotes.txt")
    pacote = [local, pergunta]
    if pacote != []:
        pacoteBackup = pacote
        bdPacotes = open(arquivoPacote, "wt")
        for item in pacoteBackup:            
            bdPacotes.write(str(item)+"\n")
        bdPacotes.close()
    bdPacotes = open(arquivoPacote, "rt")
    backup = bdPacotes
    pacoteBackup = []
    for itemBack in backup:
        itemBack =  itemBack.split("\n")
        pacoteBackup.append(str(itemBack[0]))
    bdPacotes.close()
    return pacoteBackup



