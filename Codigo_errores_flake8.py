
# Programa con errores para probarlo en flake8


def suma(a,b,c):
    listasuma = [a, b, c]
    aa = str(a)
    bb = str(b)
    cc = str(c) 
    if aa.isdigit() is False or bb.isdigit() is False or cc.isdigit() is False:
        return " Alguno de los argumentos no es un número, vuelva a intentar"

    return sum(listasuma)
