def Header(header, compTraco = 30):
    compTexto = int(compTraco/2 - len(header)/2)
    print(compTexto*" " + header)