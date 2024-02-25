import os
import ConstrutorM as cttm


def TituloF(trace="=", titulo=None, widTrace=50, subtitulo=None, menu=None):
    os.system(cttm.clear)
    # Imprime título
    print(widTrace * trace)
    print(titulo.center(widTrace))
    print(widTrace * trace)
    # Imprime subtítulo, se houver
    if (subtitulo != None):
        print(subtitulo.center(widTrace))
        print(widTrace * trace)
    print()
    # Imprime o Menú, se houver    
    if (menu != None):
        for pos, item in enumerate(menu):
            print(f"{pos:>2}){item}")
            
            