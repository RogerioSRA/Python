def RegistraBancoDadosLocais(arquivo, arquivoBackup, opcoesMenu):
    print(len(opcoesMenu))
    print(opcoesMenu)
    if len(opcoesMenu) == 2 :
        bdLocal = open(arquivo, "wt")
        for opcao in opcoesMenu:
            bdLocal.write(opcao+"\n")
        bdLocal.close()


    if len(opcoesMenu) > 2:
        bdLocal = open(arquivo, "rt")
        bdLBackup = open(arquivoBackup, "wt")
        for local in bdLocal:
            bdLBackup.write(local)
        bdLocal = open(arquivo,"wt")
        for item in opcoesMenu:
            bdLocal.write(item+"\n")
        bdLocal.close()
        bdLBackup.close()


