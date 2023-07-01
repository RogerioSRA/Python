from datetime import date

def Criar_Banco_Dados(banco_de_dados_para_BancoDeDados = "Banco_De_Dados_Geral",
                      arquivo_OpcoesDoMenu = "Menu_Opcoes",
                      opcoesDoMenu = "",
                      novoLocal = "",
                      novaTarefa = ""):
    caminho = "Dir_BancoDeDados/BancoDeDados/"
    paraRetono = caminho


    # Distribui dados recebidos em pacote e cria Banco de Dados
    pacote = [banco_de_dados_para_BancoDeDados, arquivo_OpcoesDoMenu, ]    


    for dado in pacote:
        if dado != "":
            dado = f"{caminho}{dado}"
            try:
                bdados = open(dado+".txt", "rt")
                bdados.close()
            except:
                bdados = open(dado+".txt", "xt")
                bdados.close()
            try:
                bdadosBackup = open(dado+"__Backup.txt", "rt")
                bdadosBackup.close()
            except:
                bdadosBackup = open(dado+"__Backup.txt", "xt")
                bdadosBackup.close()


    # Salva opções do menu no Banco de Dados
    qtd = 0
    arquivoLocal = f"{caminho}{arquivo_OpcoesDoMenu}.txt"
    bdadosConferencia = open(arquivoLocal, "rt")
    for local in bdadosConferencia:
        qtd += 1
    if qtd == 0:
        print("Criando Banco de Dados ...")
        opcoesDoMenu_Itens = opcoesDoMenu
        bdados = open(arquivoLocal, "wt")
        for opcao in opcoesDoMenu_Itens:
            opcao += "\n"
            bdados.write(opcao)
        bdados.close()


    if novoLocal != "": paraRetono = Acrescenta_Novo_Local(caminho, arquivo_OpcoesDoMenu, novoLocal)
    if novaTarefa != "": paraRetono = Acrescenta_Nova_Tarefa(caminho, arquivo_OpcoesDoMenu, novaTarefa)
    Banco_De_Dados_Geral(caminho, banco_de_dados_para_BancoDeDados, arquivo_OpcoesDoMenu = "Menu_Opcoes")
    return paraRetono


def Acrescenta_Novo_Local(caminho, arquivo_OpcoesDoMenu, novoLocal):
        # print(f"Novo Local\ncaminho= {caminho}\nopções do menu= {arquivo_OpcoesDoMenu}.txt\nNovo Local= {novoLocal}")
        pos = 0
        arquivoLocal = f"{caminho}{arquivo_OpcoesDoMenu}.txt"
        arquivoBackup = f"{caminho}{arquivo_OpcoesDoMenu}__Backup.txt"
        bdadosB = open(arquivoBackup, "wt")
        bdadosB.write("")
        bdados = open(arquivoLocal, "rt")
        bdadosB = open(arquivoBackup, "at")


        # Confere posição do último ítem da lista
        qtd = 0
        for dado in bdados:
            qtd += 1

        # Organiza a data de hoje
        data = f"({date.today().strftime('%d-%m-%Y')})"
        paraRetono = data


        # Adiciona local na lista de Backup
        bdados = open(arquivoLocal, "rt")
        for dado in bdados:
            if pos == qtd - 1:
                pontos = 44 - (len(data) + len(novoLocal))
                traco = pontos * "."
                bdadosB.write(f"{novoLocal}{traco}{data}\n")
                pos += 1
            bdadosB.write(dado)
            pos += 1
        bdadosB.close()


        # Refaz lista principal com novo ítem incluído
        bdados = open(arquivoLocal, "wt")
        bdados.write("")
        bdados = open(arquivoLocal, "at")
        bdadosB = open(arquivoBackup, "rt")
        for dado in bdadosB:
            bdados.write(dado)
        bdados.close()
        bdadosB.close()
        return paraRetono


def Acrescenta_Nova_Tarefa(caminho, arquivo_OpcoesDoMenu, novaTarefa):
        

        # Organiza a data de hoje
        data = f"({date.today().strftime('%d-%m-%Y')})"
        paraRetono = data

    
        arquivoLocal = f"{caminho}{arquivo_OpcoesDoMenu}.txt"
        arquivoBackup = f"{caminho}{arquivo_OpcoesDoMenu}__Backup.txt"
        bdadosB = open(arquivoBackup, "wt")
        bdadosB.write("")
        bdados = open(arquivoLocal, "rt")
        bdadosB = open(arquivoBackup, "at")


        # Copia lista de tarefas para lista de Backup e acrescenta última tarefano backup
        pos = 1
        bdados = open(arquivoLocal, "rt")
        for dado in bdados:
            bdadosB.write(dado)
            pos += 1
        bdadosB.write(f"{pos};{novaTarefa};{data}\n")
        bdadosB.close()


        # Refaz lista principal com novo ítem incluído
        bdados = open(arquivoLocal, "wt")
        bdados.write("")
        bdados = open(arquivoLocal, "at")
        bdadosB = open(arquivoBackup, "rt")
        for dado in bdadosB:
            bdados.write(dado)
        bdados.close()
        bdadosB.close()
        return paraRetono


def Banco_De_Dados_Geral(caminho, banco_de_dados_para_BancoDeDados, arquivo_OpcoesDoMenu):
    # print(f"Banco de Dados Geral\ncaminho= {caminho}\nBanco de dados Geral= {banco_de_dados_para_BancoDeDados}\nOpcoes Menu= {arquivo_OpcoesDoMenu}")
    qtd = 0
    arquivoGeral = f"{caminho}{banco_de_dados_para_BancoDeDados}.txt"
    bdadosConferencia = open(arquivoGeral, "rt")
    for local in bdadosConferencia:
        qtd += 1
    if qtd < 2:
        arquivoLocal = arquivo_OpcoesDoMenu
        bdadosConferencia = open(arquivoGeral, "wt")
        bdadosConferencia.write("")
        bdadosConferencia = open(arquivoGeral, "at")
        bdadosConferencia.write(f"{caminho}{arquivoLocal}.txt\n")
        bdadosConferencia.write(f"{caminho}{arquivoLocal}__Backup.txt")
        bdadosConferencia.close()

        



