from AcoesD.locaisM import Locais
from bancoDadosD.abrirCriarArquivoM import Abrir_Criar_Arquivo


def Excluir_BancoDados(local, arquivo, escolha):
    pos = 1
    bdados_backup = local+"-tarefas__backup.txt"
    arquivos = [bdados_backup]
    bdados_backup = Abrir_Criar_Arquivo(arquivos)[0]
    bdados_bkp = open(bdados_backup, "wt")
    bdados_bkp.write("")
    bdados_bkp = open(bdados_backup, "at")
    bdados = open(arquivo, "rt")
    for tarefa in bdados:
        posicao = tarefa.split(";")
        tarefa = str(tarefa).split(";")
        if posicao[0] == escolha:
            excluido = tarefa[2].split("\n")
            excluido = excluido[0]
            continue
        bdados_bkp.write(str(pos)+";"+tarefa[1]+";"+tarefa[2])
        pos += 1
    bdados_bkp.close()
    bdados.close()
    bdados_bkp = open(bdados_backup, "rt")
    bdados = open(arquivo, "wt")
    bdados.write("")
    bdados = open(arquivo, "at")
    for tarefa in bdados_bkp:
        bdados.write(tarefa)
    bdados.close()
    bdados_bkp.close()
    return excluido
    
        
        
