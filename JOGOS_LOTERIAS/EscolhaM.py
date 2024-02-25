import sys


def EscolhaF(pergunta, min=0, max=1):
    while True:
        resposta = input(f"\n{pergunta} ({min} - {max}) ? : ")
        if (resposta.isnumeric()):
            resposta = int(resposta)
            if (min <= resposta <= max):
                if (resposta == 0): sys.exit()
                else: return resposta
                
