
# Programa con errores para probarlo en flake8
def suma(a,b,c):
    listasuma =    [a,b,c]

    aa= str(a)

    bb=   str(b)

    cc= str(c)
    
    if aa.isdigit() == False or bb.isdigit() == False or cc.isdigit() == False:
          return " Alguno de los argumentos no es un número, vuelva a intentar"

    return sum(listasuma)
  
