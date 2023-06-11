caminho = '/home/rogerio/Documentos/GitHub_Cursos/Python/Programas_Uteis/BancoDeDados/BancoDeDados.txt'




arquivo = open(caminho,'rt')
print('arquivo ',arquivo)
print('readline() ',arquivo.readline()[1].replace(';','o'))
print('readlines() ',arquivo.readlines()[14][1].replace(';','o'))
arquivo.close()
arquivo = open(caminho,'rt')
texto = arquivo.readlines()[14]
texto.replace(';','o')
arquivo = open(caminho,'rt')
arquivo.line_buffering()[14](arquivo.write(texto))
arquivo.close()
arquivo = open(caminho,'rt')
print(arquivo.readlines())
arquivo.close()
arquivo = open(caminho,'rt')
# arquivo.readlines()[14].remove()

