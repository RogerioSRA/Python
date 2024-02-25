from JogosM import Jogos
from TituloM import TituloF
from EscolhaM import EscolhaF


def MenuF():
    while True:
        titulo = "Menu"
        subtitulo = "Criado por: Rogério S.R.A."
        menu = ["Sair", "Quina", "Mega_Sena", "Lotofacil"]
        TituloF(titulo=titulo, subtitulo=subtitulo, menu=menu)
        max = len(menu) - 1
        pergunta = "Para qual Jogo gostaria de sugestões ?:"
        resposta = EscolhaF(pergunta=pergunta, max=max)
        Jogos(menu[resposta], min=1, max=500, resposta=resposta)
    
