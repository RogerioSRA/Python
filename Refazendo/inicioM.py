import os
import menuM
from time import sleep


def Letreiro():
    msn = 50*" "+"PORTIFÓLIO, programas gerais comprovando conhecimento na área de programação PYTHON ...     Rogerio Soares Rodrigues Adrego"+10*" "
    n = 0
    while int(n) < len(msn):
        os.system("clear")
        print(f"{msn[n:n+37]}")
        sleep(0.1)
        n += 1
    Inicio()
    

def Inicio():
    menuM.Menu()


# Letreiro()

Inicio()