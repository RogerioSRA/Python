# import os
# os.system("clear")





# def variaveis(*valores):
#     # print('\n\n')
#     print(valores)
# a = 5
# b = 10
# # variaveis(1, 2, 3, 4, 5, 6, 7, a, b)


# def teste01(a, b, c, **chances):
#     # print('\n\n')
#     if chances.get("primeira") == "Primeira Palavra":
#         print("Funcionou")
#     if chances.get("segunda") == "Segunda":
#         print("Segunda é igual a segunda")
#         return a + b + c + 1
# # retorno = teste01(1, 2, 3, primeira = "Primeira Palavra", segunda = "Segunda")
# # print("Retorno = %s" %retorno)


# def Set():
#     # print('\n\n')
#     # SET serve para retirar ítens repetidos da lista

#     a = set(['carro', 'carro', 'carro', 'carro', 'carro', 'carro', 'moto', 'caminhão'])
#     b = set(['carro', 'skate', 'triciclo'])

#     print(a) # Lista a
#     print(b) # Lista b

#     print(a.intersection(b)) # Está em "a" e "b"
#     print(b.intersection(a)) # Está em "a" e "b"

#     print(a.symmetric_difference(b)) # Lista sem repetição
#     print(b.symmetric_difference(a)) # Lista sem repetição

#     print(a.difference(b)) # Ítens sem repetição
#     print(b.difference(a)) # Ítens sem repetição

#     print(a.union(b)) # Une as Listas sem repetição


# class Initiation:
#     # print('\n\n')
#     def __init__(self):
#         print("Funciona automaticamente")
#     def into():
#         print("Into")
# # Initiation()


# class teste:
#     # print('\n\n')
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def change1(self):
#         print("Nome => ", p1.nome, "\nIdade => ",p1.idade)
# p1 = teste('rogerio', 12)
# # p1.change1()


# x = 1j
# # print('\n\n')
# # print(x)
# # print(type(x))


# def While():
#     # print('\n\n')
#     i = 1
#     while i < 6:
#         print(i)
#         i += 1
#     else: print("i is no longer less than 6")


# def my_function(child3, child2, child1):
#     # print('\n\n')
#     print("The youngest child is " + child3)
# # my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# def my_function(**kid):
#     # print('\n\n')
#     print("His last name is " + kid["lname"])
# # my_function(fname = "Tobias", lname = "Refsnes")


# def my_function(country = "Norway"):
#     # print('\n\n')
#     print("I am from " + country)
# # my_function("Sweden")
# # my_function("India")
# # my_function()
# # my_function("Brazil")


# def my_function(food):
#     # print('\n\n')
#     for x in food:
#         print(x)
# fruits = ["apple", "banana", "cherry"]
# # my_function(fruits)


# def my_function(x):
#     # print('\n\n')
#     return 5 * x
# # print(my_function(3))
# # print(my_function(5))
# # print(my_function(9))



# # print('\n\n')
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple) # Substitui o For In
# # print(next(myit)) # Tem que usar NEXT
# # print(next(myit)) # Tem que usar NEXT
# # print(next(myit)) # Tem que usar NEXT

 
# class variable:
#     # print('\n\n')
#     global boia
#     boia = 10
#     def carro():
#        try:
#         print("Dentro do DEF ", boia)
#        except:
#           print("Ocorreu um erro, variavel não reconhecida")
#        else:
#           print("A variavel 'boia' vale : ",boia)
#        finally:
#           print("Até mais ver")
#     # carro()
# #     print("Dentro da classe ", boia)
# # print("Fora da classe ", boia)




# # print('\n\n')

# with open('/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/banco01.txt','rt') as arquivo01:
#     nomes = arquivo01.readlines()

#     with open('/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/banco02_operacoes.txt','wt') as arquivo02:
#         for nome in nomes:
#             if (nome.find('f') == -1):
#                 arquivo02.write(nome)
#         arquivo02.close()
# arquivo01 = open('/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/banco01.txt','wt')
# arquivo02 = open('/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/banco02_operacoes.txt','rt')
# msn = arquivo02.read()
# print(msn)
# arquivo01.write(msn)
# arquivo01 = open('/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/banco01.txt','rt')
# print("Arquivo 01:\n"+arquivo01.read())
# arquivo01.close()
# arquivo02.close()


arquivo01 = open('/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/banco01.txt','rt')
arquivo02 = open('/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/banco02_operacoes.txt','wt')

msn = arquivo01.read()
print("msn \n",msn)
msn = msn.split()
msn.remove('hh;100')

msn.pop(1)
del msn[0]
for item in msn:
    arquivo02.write(item+'\n')
arquivo02 = open('/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/banco02_operacoes.txt','rt')
print(arquivo02.read())




