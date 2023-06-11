from cadastro.cadastrar import *
from cadastro.Armazenamento.bancoDadosGet import BancoDadosGet


def VerLista():
    os.system('clear')
    print(Tracos(' Clientes Cadastrados '),'\n')
    print(f'{"Nome:":<57}{"Idade:"}\n')
    nomeArquivo = 'BancoDeDados'
    dados = BancoDadosGet(nomeArquivo)
    dado = dados
    try:
        for linha in dado:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f"{dado[0]}".ljust(57,'-')[:57],f"{dado[1]}".rjust(3)[:3])
        dados.close()
    except:
        print("Não existem clientes cadastrados....")
    input("\nQualquer tecla para voltar")
    cadastroMenu.cadastroMenu.Cadastro()

    