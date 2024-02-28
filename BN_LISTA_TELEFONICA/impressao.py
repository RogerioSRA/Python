import os, construtor
import criar_bloco_notas as cbn


def Impressao(title=None, subtitle=None, extratitle=None, menu=None, trace="=", eTrace="~", wTrace=70):
    clear = construtor.clear
    os.system(clear)
    print(wTrace * trace)
    print(title.center(wTrace))
    print(wTrace * trace)
    if (subtitle != None):
        print(subtitle.center(wTrace))
        print(wTrace * trace)
        if (extratitle != None):
            print(extratitle.center(wTrace))
            print(wTrace * eTrace)
    print()
    if (menu != None):
        for pos, opcao in enumerate(menu, 1):
            if (pos == 5):
                print(20*"-")
            print(f"{pos:>2}) {opcao}")
    print()

