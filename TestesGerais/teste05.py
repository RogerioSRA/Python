import os
from time import sleep


os.system("clear")


def inicio_Um():
    print("Inicio")
    

def meio():
    print("Meio")


def fim():
    print("Fim")
    

escolhas = ["eu", inicio_Um, meio, fim]
# for item in escolhas:
#     if type(item) != str:
#         item = str(item).split()
#         print(str(item[1]))
    # else:
    #     print(item)
# opcao = input("Qual escolha? : ")
# resp = escolhas[int(opcao)]()






def Letreiro():
    msn = 50*" "+"PORTIFÓLIO, programas gerais comprovando conhecimento na área de programação PYTHON ..."+20*" "
    n = 0
    while int(n) < len(msn):
        os.system("clear")
        print(f"{msn[n:n+37]}")
        sleep(0.1)
        n += 1
# Letreiro()

print(f"potroca")
print(f"{'potroca':>23}"[:22])
