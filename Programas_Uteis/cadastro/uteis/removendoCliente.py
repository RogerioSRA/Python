from cadastro.uteis.confirmacao import Correto
from cadastro.Armazenamento.bancoDeDados import CaminhoParaDados


def Removendo(excluirNome):
    bancoDeDadosVar = 'BancoDeDados'
    caminho = CaminhoParaDados().format(bancoDeDadosVar)
    arquivo = open(caminho+'.txt','rt')
    arquivoTXT = arquivo.readlines()
    for nome in arquivoTXT:
        nomeX = nome.split(';')
        if nomeX[0].lower() == excluirNome.lower():
            print(f"\nNome encontrado: {nomeX[0]}  =>  idade: {nomeX[1]}")
            resp = Correto('Esse é o cliente correto? 1-Sim  2-Não: ')
            if resp == False:
                continue
            if resp == True:
                print(f"\nCliente excluído: Nome: {nomeX[0]}  =>  idade: {nomeX[1]}")
                arquivoTXT.remove(nome)
                break
    else:
        print("\nCliente não encontrado...")
    arquivo = open(caminho+'.txt','wt')
    for nome in arquivoTXT:
        arquivo.write(nome)
    arquivo.close()

