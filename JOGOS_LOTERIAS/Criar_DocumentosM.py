from datetime import date
import ConstrutorM as cttm
from Ler_DocumentosM import Ler_DocumentosF


def Criar_DocumentosF(nomeDoJogo, existe=None, jogo=[], reescrever = True):
    data = str(date.today().strftime('%d-%m-%Y'))
    if (reescrever == True):
        try:
            with open(cttm.path_ + nomeDoJogo + ".txt", 'r') as criando:
                if (existe != None):
                    descarta, qtdDeJogos = Ler_DocumentosF(nomeDoJogo=nomeDoJogo)
                    return True, qtdDeJogos
        except:
            with open(cttm.path_ + nomeDoJogo + ".txt", "w") as criando:
                criando.write(10 * "/" + data + 10 * "\\" + "\n")
                print(f"Documento {nomeDoJogo}.txt criado com sucesso  !")
                return False, 0
    Registrando_Jogo(nomeDoJogo, jogo)


def Registrando_Jogo(nomeDoJogo, jogo):
    with open(cttm.path_ + nomeDoJogo + ".txt", "a") as criando:
        cont = 0
        final = ", "
        for num in jogo:
            cont += 1
            if (cont == len(jogo)):
                final = "\n"
            if (num < 10):
                num = "0" + str(num)
            criando.write(str(num) + final)

