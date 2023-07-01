import os
import unidecode
os.system("clear")





def Imprime():
    array = [1, 2, 3, 4, 5, 6, 7]
    for num in array:
        if num % 2 == 0:
            Print2()
        print(num)

def Print():
    array_b = [10, 11, 12, 13, 14, 15, 16, 17]
    print(type(array_c))
    for num in array_b:
        print(num)


def Print2():
    array_b = list['10', '11', '12', '13', '14', '15', '16', '17']
    print(type(array_c))
    for num in array_b:
        print(num)


# Imprime()


def Print2():
    array_b = "10,17"
    # array_b = list('10')
    # array_b = [10, 11, 12, 13, 14, 15, 16, 17]
    print("b= ",type(array_b))
    pos = 0
    # dado = open(array_b)
    for num in array_b:
        print(num)
        if pos % 2 == 0:
            Print3()
        pos += 1


def Print3():
    array_c = "['a', 'b', 'c']"
    print("c= ",type(array_c))
    for item in array_c:
        print(item)



Print2()



