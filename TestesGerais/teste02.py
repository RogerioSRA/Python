import os
os.system('clear')

# def Nome():
#     inome = input("Nome: ")
#     return inome
# def Idade():
#     iidade = int(input("Idade: "))
#     return iidade
# def Registro():
#     nome = Nome()
#     if nome == None or nome == '': return Registro()
#     idade = Idade()
#     print("Nome => {}\nIdade => {}".format(nome, idade))
#     StopIteration

# Registro()
# print("Acabou...")


def BancoDadosOrganizacao21(nomeArquivo):
        caminho = '/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/{}'
        bancoDados = open(caminho.format(nomeArquivo),'rt')
        dadosCopy = []
        dados = bancoDados.readlines()
        for dado in dados:
                prov00 = dado.split(';')
                prov00[0] = prov00[0].capitalize()
                dadosCopy.append(prov00[0]+';'+prov00[1])
        dadosCopy.sort()
        bancoDadosCopy = open(caminho.format('BancoDeDadosCopy.txt'),'wt')
        for nome in dadosCopy:
                bancoDadosCopy.write(nome)
        bancoDados.close()
        bancoDadosCopy.close()
BancoDadosOrganizacao21('BancoDeDados.txt')

