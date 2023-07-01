import os
import unidecode


carro = 100

def item():
    global moto
    moto = 110
    print(moto)
    item2()

def item2():
    # global moto    
    print(moto)
    print(carro)

item()