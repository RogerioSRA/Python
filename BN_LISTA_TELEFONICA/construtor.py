import os, sys, platform

# BLOCO DE NOTAS
sistema = platform.system()
if (sistema == 'Linux'):
    barra = '/'
    desktop = 'Área de Trabalho'
    documentos = 'Documentos'
    clear = 'clear'

else:
    barra = '\\'
    desktop = 'Desktop'
    documentos = 'Documents'
    try:
        os.system('clr')
        clear = 'clr'
    except:
        clear = 'cls'
path_ = os.path.expanduser(f"~{barra}{documentos}{barra}PYTHON{barra}BN_LISTA_TELEFONICA{barra}")
path_backup = os.path.expanduser(f"~{barra}{documentos}{barra}PYTHON{barra}BN_LISTA_TELEFONICA_BACKUP{barra}")
path_perm = os.path.expanduser(f"~{barra}{desktop}{barra}PYTHON{barra}BN_LISTA_TELEFONICA_PERM{barra}")
menu_inicial_bn = "menu_inicial"

# CRIA DIRETÓRIO NORMAL
try:
    os.makedirs(path_)
except FileExistsError: pass
except: input("Um erro ocorreu criando diretorio..."); sys.exit()
try:
    with open(path_+menu_inicial_bn, "r") as arq: pass
except FileNotFoundError:
    with open(path_+menu_inicial_bn, "x") as arq: pass
except: input("Um erro ocorreu criando arquivo..."); sys.exit()

# CRIA DIRETÓRIO BACKUP
try:
    os.makedirs(path_backup)
except FileExistsError: pass
except: input("Um erro ocorreu criando diretorio backup..."); sys.exit()

try:
    with open(path_backup+menu_inicial_bn, "r") as arq: pass
except FileNotFoundError:
    with open(path_backup+menu_inicial_bn, "x") as arq: pass
except: input("Um erro ocorreu criando arquivo backup..."); sys.exit()

# CRIA DIRETÓRIO PERMANENTE
try:
    os.makedirs(path_perm)
except FileExistsError: pass
except: input("Um erro ocorreu criando diretorio perm..."); sys.exit()
try:
    with open(path_perm+menu_inicial_bn, "r") as arq: pass
except FileNotFoundError:
    with open(path_perm+menu_inicial_bn, "x") as arq: pass
except: input("Um erro ocorreu criando arquivo perm..."); sys.exit()

