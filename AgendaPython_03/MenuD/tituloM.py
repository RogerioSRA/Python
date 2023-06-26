def Titulo(titulo = " Sem Título", comprimentoTraco = 30):
    comprimentoTraco = int(comprimentoTraco/2) - int(len(titulo) / 2)
    print(comprimentoTraco * " "+titulo)