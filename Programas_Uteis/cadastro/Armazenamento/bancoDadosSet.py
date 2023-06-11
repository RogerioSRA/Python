from cadastro.Armazenamento.bancoDeDados import CaminhoParaDados
from cadastro.Armazenamento.bancoDadosOrganizar import BancoDadosOrganizacao


def BancoDadosSet(nomeArquivo, dados):
        caminho = CaminhoParaDados()
        bancoDadosVar = open(caminho.format(nomeArquivo+'.txt'),'at')
        bancoDadosVar.write(dados)
        bancoDadosVar.close()
        BancoDadosOrganizacao(nomeArquivo)

