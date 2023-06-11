import os
os.system('clear')

# print("23")
# print("Eu tenho",10,"anos")
# print("Ola")
# print("pessoa")
# print("Ola \npessoa")
# # help(print)

# a = "Eu tenho"
# b = 12
# c = "carros"

# print(a, b, c)

# x = 10
# y = 3
# print(x/y)
# print(x//y)
# print(x%y)
# print(10**3)
# x += 1
# print(x+1)
# print(x)

# x = 12
# y = 10
# soma = x + y
# print("A soma de ",x," + ",y," dá ",soma)

# x = 10
# y = 3
# print("Valor de 'X'=>", x ,"Valor de 'Y'=>", y)
# print("Soma=>", x + y)
# print("Subtração=>", x - y)
# print("Multiplicação=>", x * y)
# print("Divisão=>", x / y)
# print("Divisão Inteira=>", x // y)
# print("Resto=>", x % y)

# x = input("Numero=> ")
# print(100 - int(x))
# print(100 < 80)
# x = bool(1)
# if x:
#     print(x)
# else:
#     print("Falso")

# print((10<15)<2)

# n = 10
# cont = 0
# while cont <= n:
#     print(cont)
#     cont += 1


# n = 11
# for cont in range(2, n, 2):
#     print(cont)

# print(10/3)
# print("%.2f"%(10/3))
# print("%10.2f"%(10/3))

# import math as b
# print("%.2f"%(b.sin(30)))


"""
# TUPLA (,)
lista = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(type (lista))
# lista += (12)
print(lista[1:3])
print(lista)
print(len(lista))
for i in lista:
    print("=>",i)

# LIST [,]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type (lista))
lista += [12]
lista.append(18)
print(lista[1:3])
print(lista)
print(len(lista))
for i in lista:
    print("=>",i)

# SET {,,}
lista = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type (lista))
# lista += {12}
lista.add(17)
# print(lista{1:3})
print(lista)
print(len(lista))
for i in lista:
    print("=>",i)

# DICT {:,}
lista = {1:"bola", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
print(type (lista))
# lista += {12}
# lista.add(17)
# print(lista{1:3})
print(lista)
print(len(lista))
# for key, value in lista:
#     print("=>",key,value)


# Método SLICE
# Copiando lista completa
# Colocando (-1) no lugar de (1) a lista é copiada na ordem inversa

# lista = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# li_01 = lista[::1]
# li_01 += [21]

# print(lista)
# print(li_01)
# li_01.remove(10)
# print(li_01)
"""

'''
lista = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

aux = lista[::1]
print(aux)

for rep in aux:
    clear = aux.count(rep)
    if clear > 1:
        aux.remove(rep)
    for rep in aux:
        clear = aux.count(rep)
        if clear > 1:
            aux.remove(rep)
print(aux)
'''
"""
# import random
# print(random.randrange (1,10))
"""

"""
lista = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(lista)
lista.pop(2)
print(lista)
"""

"""
x = 5
i = 8

print("O elemento %d se encontra no indice %d"%(x, i))
"""

'''
# FUNÇÃO WHILE COM MAIS DE UMA CONDIÇÃO
i = 0
a = 10
b = 20
foi = False

while not foi and i <= b:
    print(i)
    if i == a :
        foi = True
        print("Encontrei")
    i += 1
'''


"""
# MOSTRANDO POSIÇÃO DE UM ÍTEM
lista = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista.index(7))
"""


"""
# INSERINDO NÚMERO EM LISTA
lista = [2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.insert(2, 121)
print(lista)
"""

"""
# ORGANIZANDO NÚMERO EM LISTA (Ordem Crescente)
lista = [9,5,8,4,7,3,6,1,10,2]
lista.sort()
print(lista)
"""

"""
# LIMPANDO UMA LISTA
lista = [9,5,8,4,7,3,6,1,10,2]
lista.clear()
print(lista)
"""

"""
# COPIANDO UMA LISTA
lista = [9,5,8,4,7,3,6,1,10,2]
lista.sort()
li = lista.copy()
print(li)
"""

"""
a = ["a", "c", "g", "e", "d", "f", "b", "h"]
print(a)
a.sort()
print(a)
"""


"""
a = [4, 4]
b = [4, 4, 4]
print(a < b)
print(a == b)
print(a > b)
"""

"""
def bolota(n = ""):
    n = "tentativa"
    return n


frase = "paçoca"
frase01 = bolota(frase)
print(frase01)

frase = "caçarola"
bolota(frase)
print(frase)
"""

"""
def bolota(m, n, o):
    m = "ten 01"
    n = "ten 02"
    o = "ten 03"
    return m, n, o
f1 = ""
f2 = ""
f3 = ""
print(bolota(f1, f2, f3))
# ou
f1, f2, f3 = bolota(f1, f2, f3)
print(f2)
"""

"""
# TUPLA (imutável)
t = (1, 2, 3, (4, 5), 6, [7, 8, 9])
print(t)
print(t[1])
print(t[3][1])
t[5][2] = 5
print(t)

a = 1, 2, 3
b = 4, 5, 6

a += b
print(a)
print(a*3)
a *= 3
print(a.index(2))
print(a.count(2))
print(a[2:4])
"""

"""
# ARGUMENTOS VARIÁVEIS
# (o asterístico antes da variável avisa que a variável recebeerá uma lista de argumentos)
def soma (num = 0, *lista):
    print(num)
    print(lista)
li = soma(1, 2, 3, 4, 5, 6, 7)
"""


"""
def incrementa(x):
    x += 10
    print("inc",x)
    x += 10
    return x
x = 3
incrementa(x)
print("return",incrementa(x))
print(x)
def inc02():
    global x
    print("2",x)
    x += 100
    print("2",x)
print("fora",x)
inc02()
print("fora",x)
"""

"""
def poli(a):
    a[0] += 21

a = [1, 2, 3]
poli(a)
print(a)
"""


"""
def po(teste00):
    teste00 = "Deu !!!"
    teste00 = 5
    return teste00
print (po(''))
"""


# <============= STRINGS =============>

# print(20*"=")
# print("Eu tenho " +str(10) + " anos")
# print("Eu vi ""10"" pássaros")
# print(17)
# print(str(17))
# print("""
# Meu
# Nome
# \v
# é:        
# """)

# print("Eu tenho %s anos"%"string")
# print("Eu tenho %3g anos"%7)
## %i = INTEIRO
## %d = DECIMAL
## %f = FLOAT
## %g = GERAL (inicio de escrita da DIREITA para a ESQUERDA)
## %s = STRING

# print("eu")
# print("eu")
# print("eu")
# print("eu")
# print("eu")

# print("tu", end = " ")
# print("tu", end = " ")
# print("tu", end = " ")
# print("tu", end = " ")
# print("tu", end = " ")
# print("\n")

## ,end = Decide o que será colocado ao final de cada impressão

# nome = "Frederico"
# for charactere in nome:
#     print(charactere)

# "Pedro"[1] = "s"


#32
# i = 40
# while i < 100:
#     letra = "%c"%i
#     print("codigo ",ord("%c"%i), i ,"%c"%i)
#     i += 1



# nome = "caçarola"
# nomeCapitalize = nome.capitalize()
# print(nomeCapitalize)

'''


 o     o
/|\   /|\
| |   / \



'''





'''
arquivo = open("DOCUMENTO_PYTHON.txt", "w")
arquivo.write("Teste de escrita com PYTHON.\n")
arquivo.write("Vendo como")
arquivo.write("\n")
arquivo.write("funciona\n")

# Comando para escrever varias strings ao mesmo tempo
arquivo.writelines(['oi\n', 'esse\n', 'comando\n', 'escreve\n', 'varias\n', 'strings\n'])


arquivo.close()


arquivo = open("DOCUMENTO_PYTHON.txt", "r")
# print(arquivo.read())


# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

print(arquivo.readlines())

arquivo.close()

arquivo = open("DOCUMENTO_PYTHON.txt", "a")

arquivo.write("\n\nEssa parte foi escrita com APPEND")

arquivo.close()



arq = open("teste02.txt", "w")

arq.write(5*"bla bla bla \n")

arquivo.close()


'''

# def variavel():
#     global a
#     a = 5
#     ver()
    

# def ver():
#     try:
#         print (a)
#     except:
#         print("A não chega aqui")
# global a
# variavel()

a = []
a.append({'nome':'eu', 'idade':10})

print(a[0]['nome'])

b = 8
c = 10

print("b = %i c = %i" %(b, c))
print("b = %i"%b,10*'=',"c = %i"%c)