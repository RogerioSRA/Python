def ImprimeMenu(opcoesMenu):
    print()
    posicao = 0
    for item in opcoesMenu:
        if item == "":continue
        posicao += 1
        if item == "Sair":
            print()
            posicao = 0
        print(f"{posicao:>3} - {item}")

    pass