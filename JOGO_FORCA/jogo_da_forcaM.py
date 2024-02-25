import os, sys, random, unidecode, platform

class Jogo_Forca:
    def __init__(self) -> None:
        self.Inicia_Jogo()


    def Inicia_Jogo(self):
        sistema = platform.system()
        if sistema == 'Linux':
            self.clear = 'clear'
            self.negrito = '\033[1m'
            self.cor_padrao = '\033[m'
            self.cor_amarela = '\033[1;33m'
            self.cor_fundo_azul = '\033[44m'
            self.cor_vermelha = '\033[1;31m'
        else:
            self.clear = 'cls'
            self.negrito = self.cor_padrao = self.cor_amarela = self.cor_fundo_azul = self.cor_vermelha = ''
        try:
            os.system(self.clear)
        except:
            self.clear = 'clr'
            os.system(self.clear)
        self.chances = 7
        self.estado = True
        self.palavras = [
            # veiculos
            ['helicóptero', 'ultraleve', 'tanque', 'carro', 'moto', 'avião', 'barco', 'bicicleta', 'velocípede', 'lancha', 'jetsky', 'caminhao', 'trator', 'ônibus', 'triciclo', 'quadriciclo', 'monociclo', 'carreta', 'carroça', 'iate', 'canôa', 'gôndola', 'ciclomotor', 'furgão', 'metrô', 'trem'], 

            # alimento
            ['arroz', 'feijão', 'salsicha', 'linguiça', 'risoto', 'batata', 'angú', 'inhame', 'mandioca', 'abóbora', 'abobrinha', 'cereal'],
            
            # frutas
            ['maçã', 'pêra', 'banana', 'melância', 'goiaba', 'cereja', 'ameixa', 'manga', 'abacate', 'abacaxi', 'uva', 'pêssego', 'jabuticaba', 'kiwi', 'damasco', 'tâmara', 'morango', 'limão', 'laranja', 'melão', 'mamão', 'cana-de-açúcar', 'carambola', 'graviola'], 
            
            #animais
            ['siri', 'boi', 'frango', 'jabuti', 'cachorro', 'gato', 'cavalo', 'égua', 'papagaio', 'arara', 'tartaruga', 'coelho', 'onça', 'tigre', 'leão', 'hipopótamo', 'rinoceronte', 'rato', 'pato', 'sapo', 'cangurú', 'cavalo', 'égua', 'cadela', 'cachorra', 'ganso', 'sisne', 'javali', 'porco', 'girafa', 'elefante', 'jacaré', 'maritaca', 'tucano', 'urubú', 'abutre', 'águia', 'gavião', 'pássaro', 'baleia', 'peixe', 'enguia', 'arraia', 'tubarão', 'polvo', 'camarão', 'lagosta'], 
            # geral
            ['ar', 'água', 'chão', 'gelo', 'vento', 'chuva', 'tufão', 'tempestade', 'tsunami', 'terremoto', 'redemoinho', 'maremoto', 'terremoto', 'granizo', 'neve', 'frio', 'calor', 'frescor', 'mormaço', 'mar', 'oceano', 'lago', 'córrego', 'riacho', 'lagoa', 'sereno', 'serração', 'neblina', 'ventania'], 
            
            # portugues
            ['proparoxítona', 'paroxítona', 'monossílabo', 'hiato', 'ditongo', 'tritongo', 'trissílabo', 'polissílaba', 'letra', 'palavra', 'arroba', 'vírgula', 'reticências', 'acento', 'circunflexo', 'agudo', 'parágrafo', 'travessão', 'sílaba', 'silábica', 'expressões'], 
            
            # temperos
            ['yakisoba', 'pimenta', 'açafrão', 'alho', 'cebola', 'raiz-forte', 'chimichurri', 'coentro', 'sal', 'estragão', 'louro', 'erva-doce', 'cebolinha', 'orégano', 'salsa', 'salsinha', 'manjericão', 'alecrim', 'hortelã', 'pimenta-do-reino', 'pimenta-dedo-de-moça', 'pimenta-malagueta', 'pimenta-biquinho']]
        self.array = random.randrange(0, len(self.palavras))
        self.palavra = random.choice(self.palavras[self.array])
        match self.array:
            case 0: self.dica = ("Veículo")
            case 1: self.dica = ("Comida")
            case 2: self.dica = ("Fruta")
            case 3: self.dica = ("Animal")
            case 4: self.dica = ("Geral")
            case 5: self.dica = ("Português")
            case 6: self.dica = ("Tempêro")
        self.comprimento = {0:10, 1:9, 2:9, 3:8, 4:8, 5:11}
        self.letras_registradas = [' ', '-', '_']
        print()
        self.Jogo()


    def Jogo(self):
        errado = False
        self.boneco = False
        if self.estado == True:
            self.palavraMontada = self.PalavraSectreta()
            self.Imprime_Tela()
        letraTentada = input("Entre com uma letra: ")
        # Letra já está registrada
        for lr in self.letras_registradas:
            if unidecode.unidecode(lr) == unidecode.unidecode(letraTentada):
                errado = True
                print("Está errado")
                break
        # Palavra tem essa letra
        if errado == False:
            self.letras_registradas += [letraTentada]
            errado = True
            for letra in self.palavra:
                if unidecode.unidecode(letra) == unidecode.unidecode(letraTentada):
                    errado = False
                    break
        if errado == True:
            print("Errado")
            self.boneco = True
            self.chances -= 1
        else:
            print("Certo")
            self.boneco = False
            print("Está certo, Registrando letra")
        self.PalavraSectreta()
        self.Jogo()


    def PalavraSectreta(self):
        self.palavraMontada = ""
        # Montar Palavra
        for letra in self.palavra:
            tem = False
            # Se na palavra tem uma das letra das registradas
            for lr in self.letras_registradas:
                if unidecode.unidecode(lr) == unidecode.unidecode(letra):
                    tem = True
                    self.palavraMontada += letra+" "
                else:
                    tem == False
            if tem == False:
                self.palavraMontada += "_ "
        if self.estado == True: self.estado = False; return self.palavraMontada
        self.Imprime_Tela()


    def Imprime_Tela(self):
        try:
            os.system(self.clear)
        except:
            self.clear = 'clr'
            os.system(self.clear)
        print("JOGO DA FORCA")
        forca = ["__________",
                "|        |",
                "|        0",
                "|       /|)",
                "|       /(",
                "|__________"]
        if self.boneco == True:
            posHor = 0
            for key in self.comprimento:
                linha = forca[posHor]
                if self.comprimento[key] == len(linha):
                    posHor += 1
                else:
                    self.comprimento[key] += 1
                    break
        posHor = 0
        for linha in forca:
            print(linha[:self.comprimento[posHor]])
            posHor += 1
        print()
        print(self.palavraMontada)
        palavraMontada_conferencia = "".join(self.palavraMontada.split())
        if palavraMontada_conferencia == self.palavra:
            input("\nVOCÊ VENCEU  !!!!!!!!!!!!")
            self.Decisao()
        if self.chances > 0:
            print()
            print(f"Essa palavra tem {self.cor_amarela}{len(self.palavra)}{self.cor_padrao} letras.\nA dica é: {self.cor_vermelha}{self.dica}{self.cor_padrao}.\n\nVocê tem {self.cor_fundo_azul} {self.chances} {self.cor_padrao} tentativas.")
        else:
            print(f"\n{self.negrito}GAME OVER{self.cor_padrao}\n\n")
            self.Decisao()
        return


    def Decisao(self):
        decisao = input("Gostaria de nova tentativa ? 1-Sim 2-Não : ")
        if decisao == '1': self.Inicia_Jogo()
        else: sys.exit()
        
