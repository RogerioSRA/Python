from cadastro.Armazenamento.bancoDeDados import CaminhoParaDados


def CriarBancoDados(nomeArquivo):
        caminho = CaminhoParaDados()
        try:
            bancoDadosVar = open(caminho.format(nomeArquivo+'.txt'),'rt')
            bancoDadosVar.close()
        except:
            bancoDadosVar = open(caminho.format(nomeArquivo+'.txt'),'x')
            bancoDadosVar.close()
        try:
            bancoDadosCopy = open(caminho.format(nomeArquivo+'Copy'+'.txt'),'rt')
            bancoDadosCopy.close()
        except:
            bancoDadosCopy = open(caminho.format(nomeArquivo+'Copy'+'.txt'),'x')
            bancoDadosCopy.close()

