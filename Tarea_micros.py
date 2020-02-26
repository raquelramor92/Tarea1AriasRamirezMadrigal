
#Error 1 para tipo de dato recibido incorrecto
def Error1():
    return "Error 1"
#Error 2 para función 1, dato ya se encuentra en mayúscula
def Error2():
    return "Error 2"
#Error 3 para función 3, no natural
def Error3():
    return "Error 3"


def PrimeraFuncion (x):
    for i in x:
        if i.isupper() == True:
            return Error2()
            break
        if i.isdigit() == True:
            return Error1()
            break
    x = x.upper()
    return x
    

def SegundaFuncion(x):
    y = "False"
    for i in x:
        if i.isdigit() == True:
            return Error1()
            break
        
        if i == "w":
            y = "True"
    return y
            
def TerceraFuncion(x,y):
    xc = str(x)
    yc = str(y)
    if xc == x or yc == y:
        return Error1()
    if x < 0 or y < 0:
        return Error3()
   
    Resta = x - y
    if Resta < 0:
        return Error3()
    return Resta

    

