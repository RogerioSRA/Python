def Print_Menu(opcoesMenu):
    print()
    enum = 1
    for funcao in opcoesMenu:
        if funcao == "": continue
        if funcao == "Adicionar Local de Tarefas" or funcao == "Tarefas  para  o  Amanhã":
            corInicial = "\033[33m"
            corFinal = "\033[m"
        else:
            corInicial = ""
            corFinal = ""
        if funcao == "Sair":
            enum = 0
            print()
        print(f"{enum:2} - {corInicial}{funcao}{corFinal}")
        enum += 1


        