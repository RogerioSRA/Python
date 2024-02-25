import sys
from datetime import date
import ConstrutorM as cttm
from TituloM import TituloF
from EscolhaM import EscolhaF
from Ler_DocumentosM import Criar_Array_De_Jogos_Prontos
from CriandoJogosM import CriandoJogos, Criar_DocumentosF


def Jogos(titulo, min, max, resposta):
    while True:
        data = str(date.today().strftime('%d-%m-%Y'))
        match(resposta):
            case 1: # Quina
                valorAposta = 2.50
                numFinal = 80
                qtdNum = 5
            case 2: # Mega-Sena
                valorAposta = 5
                numFinal = 60
                qtdNum = 6
            case 3: # Lotofacil
                valorAposta = 3
                numFinal = 25
                qtdNum = 15
        subtitulo = f"R$ {valorAposta:.2f} Reais"
        # Conferir se Documento título existe
        documento_existe, qtdDeJogos = Criar_DocumentosF(nomeDoJogo=titulo, existe="existe?")
        if (documento_existe and qtdDeJogos > 0):
            menu = ["Sair", "Voltar", "Apagar jogo(s) existente(s) e salvar novos jogos", "Acrescentar novos jogos ao(s) existente(s)", "Listar jogo(s) salvo(s)"]
            TituloF(titulo=titulo, subtitulo=subtitulo, menu=menu)
            escolha_menu = EscolhaF(f"Já existe um documento chamado {titulo} e contém {qtdDeJogos} jogo(s).\nO que deseja fazer?", max=len(menu)-1)
            match (escolha_menu):
                case 1: return
                case 2: # Se escolheu apagar o arquivo e começar do zero
                    subtitulo = menu[escolha_menu]
                    TituloF(titulo=titulo, subtitulo=subtitulo, menu=None)
                    with open(cttm.path_ + titulo + ".txt", "w") as criando:
                        criando.write(10 * "/" + data + 10 * "\\" + "\n")
                    qtd_jogos = Estilo_De_Jogo(valorAposta, min=min, max=max)
                    CriandoJogos(escolha=qtd_jogos, qtdNum=qtdNum, numFinal=numFinal, titulo=titulo)
                    return
                case 3: # Se escolheu acrescentar mais jogos, sem apagar
                    with open(cttm.path_ + titulo + ".txt", "a") as criando:
                        criando.write(30*"=" + "\n" + 10 * "/" + data + 10 * "\\" + "\n")
                    qtd_jogos = Estilo_De_Jogo(valorAposta, min=min, max=max)
                    CriandoJogos(escolha=qtd_jogos, qtdNum=qtdNum, numFinal=numFinal, titulo=titulo)
                    return
                case 4: # Listar Jogos salvos 
                    subtitulo = menu[escolha_menu]
                    TituloF(titulo=titulo, subtitulo=subtitulo, menu=None)
                    jogosDocumentados, descartado = Criar_Array_De_Jogos_Prontos(titulo)
                    for array in jogosDocumentados:
                        final = ", "
                        contVirgula = 1
                        for num in array:
                            if contVirgula == qtdNum:
                                final = "\n"
                            if (num < 10):
                                num = "0"+str(num)
                            print(str(num),end=final)
                            contVirgula += 1
                    input("\nQualquer tecla para voltar ")                    
        else:
            menu = ["Sair", "Voltar"]
            TituloF(titulo=titulo, subtitulo=subtitulo, menu=menu)
            qtd_jogos = Estilo_De_Jogo(valorAposta, min=min, max=max)
            if (qtd_jogos != False):
                CriandoJogos(escolha=qtd_jogos, qtdNum=qtdNum, numFinal=numFinal, titulo=titulo)
            return


def Estilo_De_Jogo(valorAposta, min, max):
    while True:
        escolha = input("\nGostaria de jogar por valor(A) ou por número de jogos(B)? (A - B) : ").lower()
        if (escolha.isalpha() and (escolha != "a" and escolha != "b")
            or escolha.isnumeric() and (int(escolha) < 0  or int(escolha) > 1)): continue
        else: break
    match escolha:
        case "0": sys.exit()
        case "1": return False
        case "a":
            pergunta = "Qual o valor gostaria de jogar"
            min = 30
            escolha = EscolhaF(pergunta=pergunta, min=min, max=max)
            escolha = round(escolha / valorAposta)
            print(f"\nCom esse valor, serão criados {escolha} jogos custando R$ {valorAposta:.2f} Reais cada.")
        case "b":
            pergunta = "Para quantos jogos gostaria de sugestão ?:"
            max = round(max / valorAposta)
            escolha = EscolhaF(pergunta=pergunta, min=min, max=max)
    return escolha

