def Print_Menu(opcoesMenu):
    print()
    enum = 1
    for funcao in opcoesMenu:
        if funcao == "": continue
        if funcao == "Sair":
            enum = 0
            print()
        if funcao == "Adicionar Local de Tarefas":
            enum = 99
        print(f"{enum:2} - {funcao}")
        enum += 1


        