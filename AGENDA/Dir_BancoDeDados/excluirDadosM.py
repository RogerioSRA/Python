from datetime import date
from UtilsD.escolhaM import Validar_Escolha


def Excluir_Dados(caminho, titulo, tarefaExcluir):
        arquivo = Validar_Escolha(titulo, operacao=1)
        

        # Organiza a data de hoje
        data = f"({date.today().strftime('%d-%m-%Y')})"
        paraRetono = data

    
        arquivoLocal = f"{caminho}{arquivo}.txt"
        arquivoBackup = f"{caminho}{arquivo}__Backup.txt"
        bdadosB = open(arquivoBackup, "wt")
        bdadosB.write("")
        bdados = open(arquivoLocal, "rt")
        bdadosB = open(arquivoBackup, "at")


        # Copia lista de tarefas para lista de Backup e acrescenta última tarefano backup
        pos = 1
        bdados = open(arquivoLocal, "rt")
        for dado in bdados:
            dado = dado.split(";")
            if dado[0] == tarefaExcluir: continue
            dado = f"{pos};{dado[1]};{dado[2]}"
            bdadosB.write(dado)
            pos += 1
        # bdadosB.write(f"{pos};{novaTarefa};{data}\n")
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


