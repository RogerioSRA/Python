import unidecode


def Escolha(frase, min = 0, max = 1):
    escolha = input(f"{frase} ({min} - {max}) : ")
    if escolha.isnumeric() and (int(escolha) >= min and int(escolha) <= max):
        escolha = int(escolha)
        if escolha == 0: exit()
        else:
            return escolha
    else: return Escolha(frase, min, max)


def Validar_Escolha(funcao, operacao):
    funcao = " ".join(funcao.split())# Retira espaços em excesso
    if operacao == 1:
        funcao = funcao.title().replace(" ","_")# Troca espaços por 'underline'
        funcao = unidecode.unidecode(funcao)# Retira os acentos das palavras


    if operacao == 2:
        # Retira os pontos entre a função e a data, se houver
        funcao = funcao.title().replace("_"," ").split(".")[0]
    return funcao


