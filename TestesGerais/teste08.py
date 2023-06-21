import os
from datetime import date

os.system("clear")




arquivo = "Locais_Para_Tarefas.txt"

local = input("Local da tarefa: ")
local = local.title()
local = local.replace(" ","")

array = [""]
array.append(local)

try: bdados = open(arquivo, "rt"); bdados.close()
except: bdados = open(arquivo, "xt"); bdados.close()

bdados = open(arquivo, "at")
bdados.write(local+"\n")
bdados.close()

bdados = open(arquivo, "rt")
texto = bdados.readlines()
print(texto)

texto = texto[0].split("\n")
Frase = texto[0]

print(texto[0])
print(Frase)






def Distribui():
    bdados = open(arquivo, "rt")
    texto = bdados.readlines()
    print(texto)


    texto = texto[0].split("\n")
    Frase = texto[0]

    try:
        bdadosLocal = open(Frase+"_Tarefas.txt", "rt")
    except:
        bdadosLocal = open(Frase+"_Tarefas.txt", "xt")




Distribui()