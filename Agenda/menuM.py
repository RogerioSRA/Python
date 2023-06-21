import os
from datetime import date


def Menu():
    os.system("clear")
    opcoesMenu = ["", Boa_Vista, Lagoa_Santa, Tarefas_para_Amanha, exit]
    header = " AGENDA "
    frase = "Qual a sua escolha? "
    Traco("=")
    Header(header)
    Traco("=")
    Print_Menu(opcoesMenu)
    escolha = Escolha(frase, 0, len(opcoesMenu) - 2)
    opcoesMenu[escolha]()


def Boa_Vista():
    os.system("clear")
    opcoesMenu = ["", Nova_Tarefa, Apagar_Tarefa, Tarefas_Concluidas, Listar_Tarefas, Voltar_ao_Menu, exit]
    header = " Tarefas para o Boa Vista"
    frase = "Qual a sua escolha? "
    arquivo = "TarefasBoaVista.txt"
    pacoteBairro = [opcoesMenu, header, frase, arquivo]
    Distribui_Tarefas(pacoteBairro)


def Lagoa_Santa():
    os.system("clear")
    opcoesMenu = ["", Nova_Tarefa, Apagar_Tarefa, Tarefas_Concluidas, Listar_Tarefas, Voltar_ao_Menu, exit]
    header = " Tarefas para o Lagoa Santa"
    frase = "Qual a sua escolha? "
    arquivo = "TarefasLagoaSanta.txt"
    pacoteBairro = [opcoesMenu, header, frase, arquivo]
    Distribui_Tarefas(pacoteBairro)


def Distribui_Tarefas(pacoteBairro):
    opcoesMenu = pacoteBairro[0]
    header = pacoteBairro[1]
    frase = pacoteBairro[2]
    arquivo = pacoteBairro[3]
    Traco("=")
    Header(header)
    Traco("=")
    Print_Menu(opcoesMenu)
    Abrir_Arquivo(arquivo)
    escolha = Escolha(frase, 0, len(opcoesMenu) - 2)
    pacote = [arquivo, header]
    if escolha == len(opcoesMenu) -1 : pacote = []
    else: opcoesMenu[escolha](pacote)


def Nova_Tarefa(pacote):
    os.system("clear")
    Traco("=")
    Header(pacote[1])
    Traco("=")
    header = " Adicionando Tarefas "
    Header(header)
    Traco("=")    
    tarefa = input("Qual o nome da tarefa ? : \n",)
    tarefa = tarefa.capitalize()
    frase = "Está correto este nome ? 1-Sim  2-Não : "
    escolha = Escolha(frase, 1, 2)
    if escolha == 1:
        RegistraBancoDados(pacote, tarefa)
        print(f"\nTarefa registrada na data de {date.today().day}-{date.today().month}-{date.today().year}")
        frase = "Gostaria de um novo registro ? : 1-Sim  2-Não : "
        escolha = Escolha(frase, 1, 2)
        if escolha == 1: return Nova_Tarefa(pacote)
        else: return Boa_Vista()
    if escolha == 2: return Nova_Tarefa(pacote)


def Apagar_Tarefa(pacote):    
    os.system("clear")
    Traco("=")
    Header(pacote[1])
    Traco("=")
    header = " Apagando Tarefas "
    Header(header)
    Traco("=")
    tarefa = input("Qual a posição da tarefa a ser apagada ? : \n",)
    # tarefa = tarefa.capitalize()
    # frase = "Está correto este nome ? 1-Sim  2-Não : "
    # escolha = Escolha(frase, 1, 2)
    # if escolha == 1:
    #     RegistraBancoDados(pacote, tarefa)
    #     print(f"\nTarefa registrada na data de {date.today().day}-{date.today().month}-{date.today().year}")
    #     frase = "Gostaria de um novo registro ? : 1-Sim  2-Não : "
    #     escolha = Escolha(frase, 1, 2)
    #     if escolha == 1: return Nova_Tarefa(pacote)
    #     else: return Boa_Vista()
    # if escolha == 2: return Nova_Tarefa(pacote)


def Tarefas_Concluidas(pacote):
    pass


def Listar_Tarefas(pacote):
    os.system("clear")
    compTraco = 80
    Traco("=", compTraco)
    Header(pacote[1], compTraco)
    Traco("=", compTraco)
    header = " Listando Tarefas "
    Header(header, compTraco)
    Traco("=", compTraco)
    print()
    print(f"{'Data':<13}{'Tarefa':<50}{'Dias de atraso'}")
    print()
    cores = "0"
    bancoDados = open(pacote[0], "rt")
    for acao in bancoDados:
        data = acao.split(";")
        acao = acao.split(";")
        acao = acao[1].split("\n")
        dataDeAtraso = str(data[0]).split("-")
        diasDeAtraso = date.today() - date(int(dataDeAtraso[2]), int(dataDeAtraso[1]), int(dataDeAtraso[0]))
        diasDeAtraso = str(diasDeAtraso).split(",")
        diasDeAtraso = str(diasDeAtraso[0]).split(" ")
        if diasDeAtraso[0] == "0:00:00": diasDeAtraso[0] = "Hoje"
        elif int(diasDeAtraso[0]) > 1 : dias = "  dias"
        else: dias = "  dia "
        if cores == "\033[4;32m": cores = "\033[4;34m"
        else: cores = "\033[4;32m"
        print(f"{cores}{data[0]:<13}{acao[0][:50]:<50}{diasDeAtraso[0]:>5}{dias}\033[m")
        print()
    print()


def Voltar_ao_Menu(pacote):
    Menu()


def Abrir_Arquivo(pacote):
    try:
        bancoDados = open(pacote[0], "rt")
        bancoDados.close()
    except:
        bancoDados = open(pacote[0], "x")
        bancoDados.close()


def RegistraBancoDados(pacote, tarefa):
    data = str(Zeros(date.today().day)) + "-" + str(Zeros(date.today().month)) + "-" + str(date.today().year)
    bancoDados = open(pacote[0], 'at')
    bancoDados.write(data + ";" + tarefa + "\n")
    bancoDados.close()


def Zeros(num):
    if int(num) <10:
        num = "0"+str(num)
    else:
        num = str(num)    
    return num


def Tarefas_para_Amanha():
    print("Tarefas para Amanhã")


def Header(header, compTraco = 30):
    compTexto = int(compTraco/2 - len(header)/2)
    print(compTexto*" " + header)


def Traco(traco = "=", compTraco = 30):
    print(compTraco*traco)


def Print_Menu(opcoesMenu):
    print()
    enum = 1
    for funcao in opcoesMenu:
        if funcao == "": continue
        funcaoSplit = str(funcao).split()[1]
        if funcaoSplit == "exit()":
            funcaoSplit = "Sair"
            print()
            enum = 0
        print(f"{enum} - {funcaoSplit}")
        enum += 1


def Escolha(frase = "null", min = 0, max = 1):
    print()
    escolha = input(frase + f"( {min} - {max} ) : ")
    if escolha.isnumeric():
        escolha = int(escolha)
        if escolha >= min and escolha <= max:
            if escolha == 0: escolha = max + 1
            return escolha
        else:
            return Escolha(frase, min, max)
    else:
        return Escolha(frase, min, max)
    

Menu()


