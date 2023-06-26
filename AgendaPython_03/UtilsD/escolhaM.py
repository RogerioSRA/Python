def Escolha(pergunta, min = 0, max = 1):
    print(2*"\n")
    resposta = input(f"{pergunta} ({min} - {max}) : ")
    if resposta == "0": exit()
    return resposta