import os
from cadastro import editar
from utils.tracos import Tracos
from cadastro import cadastroMenu
from cadastro.uteis.entraNome import Nome
from cadastro.uteis.entraIdade import Idade
from cadastro.uteis.confirmacao import Correto
from cadastro.Armazenamento.bancoDadosSet import BancoDadosSet
from cadastro.Armazenamento.bancoDadosCriar import CriarBancoDados


def Cadastrar():
    os.system('clear')    
    print(Tracos(' Cadastro de Clientes '),'\n')
    print(Tracos(' Cadastrando '),'\n')
    Registro('Nome do cliente: ', 'Idade do cliente: ', 'Cadastrar')
    

def Registro(nomeFrase, idadeFrase, modulo):
    inputNome = Nome(nomeFrase)
    inputIdade = Idade(idadeFrase)

    
    print(f"\nNovo cliente cadastrado:\nNome: {inputNome}  =>  Idade: {inputIdade}")
    bancoDeDadosVar = 'BancoDeDados'
    CriarBancoDados(bancoDeDadosVar) # DADOS
    if(inputIdade != None and inputNome != "" and inputIdade > 0):
            dados = (inputNome+';'+str(inputIdade)+'\n') # DADOS
            BancoDadosSet(bancoDeDadosVar, dados)
    if modulo == 'Cadastrar':
        resp = Correto(f"\nDeseja {modulo} um novo cliente? 1-Sim 2-Não ")
        if resp == True:
            Cadastrar()
    if modulo == 'Editar':
        resp = Correto(f"\nDeseja {modulo} um novo cliente? 1-Sim 2-Não ")
        if resp == True:
            editar.Editar()
    else:
        cadastroMenu.Cadastro()
        exit()

