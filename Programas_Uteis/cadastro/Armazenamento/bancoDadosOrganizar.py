from cadastro.Armazenamento.bancoDeDados import CaminhoParaDados


def BancoDadosOrganizacao(nomeArquivo):
        caminho = CaminhoParaDados()
        bancoDadosVar = open(caminho.format(nomeArquivo+'.txt'),'rt')
        dados = bancoDadosVar.readlines()
        dadosCopy = []
        for dado in dados:
                prov00 = dado.split(';')
                prov00[0] = prov00[0].capitalize()
                dadosCopy.append(prov00[0]+';'+prov00[1])
        dadosCopy.sort()
        bancoDadosCopy = open(caminho.format(nomeArquivo+'Copy'+'.txt'),'wt')
        bancoDadosCopy.write("")
        for nome in dadosCopy:
                bancoDadosCopy = open(caminho.format(nomeArquivo+'Copy'+'.txt'),'at')
                bancoDadosCopy.write(nome)
                bancoDadosCopy = open(caminho.format(nomeArquivo+'Copy'+'.txt'),'rt')
        bancoDadosVar = open(caminho.format(nomeArquivo+'.txt'),'wt')
        bancoDadosCopy = open(caminho.format(nomeArquivo+'Copy'+'.txt'),'rt')
        for nome in bancoDadosCopy.readlines():
             bancoDadosVar.write(nome)
        bancoDadosVar.close()
        bancoDadosCopy.close()

