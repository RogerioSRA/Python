import os
os.system("clear")


def Ordenar_Por_Keys(conjunto):
    provisorio = []
    novo_conjunto = {}
    for key in conjunto.keys():
        provisorio.append(key)
    provisorio.sort()
    for key in provisorio:
        novo_conjunto[key] = None
    for keyNovo in novo_conjunto:
        for keyCon in conjunto:
            if (keyCon == keyNovo):
                novo_conjunto[keyNovo] = conjunto.keys().mapping.get(keyNovo)
    print(novo_conjunto)


def Ordenar_Por_Values(conjunto):
    provisorio = []
    for value in conjunto.values():
        provisorio.append(value)
    provisorio.sort()

    novo_conjunto = {}
    for value in provisorio:
        for key in conjunto.keys():
            comp = conjunto.values().mapping.get(key)
            if (value == comp):
                novo_conjunto[key] = value
    print(novo_conjunto)


conjunto = {'c':'cc', 'b':'bb', 'a':'aa'}
conjunto = {'nome00':'zeca', 'nome03':'carlos', 'nome02':'pedro', 'nome01':'anderson'}
Ordenar_Por_Keys(conjunto)
Ordenar_Por_Values(conjunto)

