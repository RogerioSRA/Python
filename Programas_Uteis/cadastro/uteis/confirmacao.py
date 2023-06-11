def Correto(pergunta):
        resp = input(pergunta)
        if resp == '1':
            return True
        elif resp == '2':
            return False
        else:
            return Correto(pergunta)