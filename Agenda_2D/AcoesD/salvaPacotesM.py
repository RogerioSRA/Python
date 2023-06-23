from time import sleep


def Salva_Pacotes(pacoteRecebido = []):
    arquivoPacote = "Salva_Pacotes.txt"
    pacote = pacoteRecebido
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

