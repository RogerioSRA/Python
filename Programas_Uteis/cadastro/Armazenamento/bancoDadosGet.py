from cadastro.Armazenamento.bancoDeDados import CaminhoParaDados
from cadastro.Armazenamento.bancoDadosCriar import CriarBancoDados
from cadastro.Armazenamento.bancoDadosOrganizar import BancoDadosOrganizacao


def BancoDadosGet(nomeArquivo):
    caminho = CaminhoParaDados()
    try:
        bancoDadosVar = open(caminho.format(nomeArquivo+'.txt'),'rt')
    except:
            CriarBancoDados(nomeArquivo)
    else:
        BancoDadosOrganizacao(nomeArquivo)
        return bancoDadosVar
        
