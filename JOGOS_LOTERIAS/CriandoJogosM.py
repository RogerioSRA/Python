import random
from time import sleep
import ConstrutorM as cttm
from Ler_DocumentosM import Ler_DocumentosF
from Criar_DocumentosM import Criar_DocumentosF


def CriandoJogos(escolha, qtdNum, numFinal, titulo):
    cor = ''
    jogosDocumentados, qtdDeJogos = Ler_DocumentosF(titulo)    
    while True:
        # Define os jogos
        print()
        jogo = []
        reescrever = True
        for jogos in range(0, escolha):
            if (cor == cttm.cor_verde): cor = cttm.cor_amarelo
            else: cor = cttm.cor_verde
            while len(jogo) < qtdNum:
                num = random.randint(1, numFinal)
                if (num in jogo):
                    print("Número repetido")
                    continue
                else:
                    jogo.append(num)
            jogo.sort()
            for array in jogosDocumentados:
                if (array == jogo):
                    print("Jogo repetido, REFAZENDO ... ")
                    continue
            # Cria arquivo com jogos
            Criar_DocumentosF(nomeDoJogo=titulo, jogo=jogo, reescrever=reescrever)
            reescrever = False
            # Imprime os jogos
            print()
            final = f"{cor}, "
            contadorDeNumeros = 1
            for num in jogo:
                if (contadorDeNumeros == qtdNum):final = "\n"
                if (num > 9):
                    print(f"{cor}{num}{cttm.cor_padrao}", end=final)
                else:
                    print(f"{cor}0{num}{cttm.cor_padrao}", end=final)
                contadorDeNumeros += 1
            print(((len(jogo)*4)-2)*f"{cor} ", end=f"{cttm.cor_padrao}")
            jogo = []
        sleep(1)
        input("\nQualquer tecla para retornar ao início.")
        return
    
    