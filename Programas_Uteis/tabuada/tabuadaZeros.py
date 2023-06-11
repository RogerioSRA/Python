def Tabuada_Zeros(valor):
        if (valor < 10):
            valor = "  "+str(valor)
        elif (valor >= 10 and valor <100):
            valor = " "+str(valor)
        elif (valor >= 100):
            valor = str(valor)
        return valor