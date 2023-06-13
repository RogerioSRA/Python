import random, os

os.system("clear")

m = random.choice(['bobo', 'pateta', 'caçarola', 'patê', 'carroça', 'avião'])

print(m)





def Num(x):
    aleatorio = random.randint(1, x)
    print(f"O número escolhido está entre (1) e ({x})")
    num = 0
    while num != aleatorio:
        num = int(input("Dê seu palpite...: "))
        if num != aleatorio:
            print("Palpite errado, tente novamente.")
        else:
            break
    print("Você acertou !!! Parabéns !!")
    


x = input("Entre com um número: ")
if x.isnumeric():
    x = int(x)
    print("é numerico")
    Num(x)
else:
    print("Não é numérico")
