import sys


def Escolha(pergunta=None, min=1, max=2, sn=False):
    while True:
        if (sn == False):
            resposta = input(f"{pergunta} ? ({min} - {max}) : ")
        else:
            resposta = input(f"{pergunta} (1-Sim - 2-Não) : ")
        if (resposta.isdecimal()): resposta = int(resposta)
        else: continue
        if (sn == False and resposta == 1): sys.exit()
        if (min <= resposta <= max): return resposta

