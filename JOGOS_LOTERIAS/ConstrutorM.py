import platform, os


sistema = platform.system()
if sistema == 'Linux':
    cor_padrao = "\033[m"
    cor_amarelo = "\033[1;33m"
    cor_bg_verde = "\033[1;42m"
    cor_verde = "\033[1;32;40m"
    clear = 'clear'
    barra = '/'
    desktop = 'Área de Trabalho'
    documentos = 'Documentos'
else:
    cor_padrao = cor_amarelo = cor_bg_verde = cor_verde = ''
    barra = '\\'
    desktop = 'Desktop'
    documentos = 'Documents'
    try:
        os.system('clr')
        clear = 'clr'
    except:
        clear = 'cls'
os.path.expanduser
path_ = os.path.expanduser(f'~{barra+documentos+barra}PYTHON{barra}BN_JOGOS_LOTERIAS{barra}')
path_perm = os.path.expanduser(f'~{barra+desktop+barra}PYTHON{barra}BN_JOGOS_LOTERIAS{barra}')
try:
    os.makedirs(path_)
except FileExistsError: pass
try:
    os.makedirs(path_perm)
except FileExistsError: pass


