def Print_Menu(opcoesMenu):
    print()
    enum = 1
    for funcao in opcoesMenu:
        if funcao == "": continue
        if funcao == "Sair":
            enum = 0
        print(f"{enum} - {funcao}")
        enum += 1