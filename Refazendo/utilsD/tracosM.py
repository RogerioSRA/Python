# Monta cabeçalho do Menú
def Tracos(titulo = "", traco = "="):
    comprimento = 30
    print((comprimento-int(len(titulo)/2))*traco+titulo+(comprimento-int(len(titulo)/2))*traco)
# Expõe as opções do menú
def MenuMontagem(menu):
    numerador = 1
    for opcao in menu:
        if opcao == "": continue
        if type(opcao)!= str:
            opcao = str(opcao).split()
            if opcao[1] == "exit()":
                opcao[1] = "Sair\n"
                numerador = 0
                print()
            print(str(numerador) + " - " + opcao[1])
        else:
            print(str(numerador) + " - " + opcao)
        numerador += 1


