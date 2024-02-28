import criar_bloco_notas
import editar_bloco_notas
from escolha import Escolha
from impressao import Impressao


def Menu():
    while True:
        title = 'Menú'
        subtitle = 'Listas'
        menu_inicial = criar_bloco_notas.Menu_Inicial(ini=True)
        Impressao(title=title, subtitle=subtitle, menu=menu_inicial)
        pergunta = "Qual a sua escolha"
        max = len(menu_inicial)
        resposta = Escolha(pergunta=pergunta, max=max)
        funcao = menu_inicial[resposta -1]
        if (resposta < 5):
            menu_opcoes_menu = ['Sair', 'Voltar']
            Impressao(title=title, subtitle=funcao, menu=menu_opcoes_menu)
            criar_bloco_notas.Direciona(menu_inicial[resposta -1])
            continue
        extratitle = 'Contatos'
        Submenu(title=title, subtitle=funcao, extratitle=extratitle)
            

def Submenu(title=None, subtitle=None, extratitle=None):
    while True:
        menu_inicial = criar_bloco_notas.Menu_Inicial()
        menu_inicial.insert(1, 'Voltar')
        menu_inicial.insert(4, 'Listar')
        menu_inicial.append('Encontrar')
        Impressao(title=title, subtitle=subtitle, extratitle=extratitle, menu=menu_inicial)
        pergunta = "Qual a sua escolha"
        max = len(menu_inicial)
        resposta = Escolha(pergunta=pergunta, max=max)
        if(resposta == 2): return
        funcao = menu_inicial[resposta -1]
        if (funcao != 'Listar'):
            menu_opcoes_menu = ['Sair', 'Voltar']
        else:
            menu_opcoes_menu = None
        Impressao(title=title, subtitle=subtitle, extratitle=funcao, menu=menu_opcoes_menu)
        editar_bloco_notas.Direciona(funcao=funcao, lista=subtitle, extratitle=funcao, menu=menu_opcoes_menu)

