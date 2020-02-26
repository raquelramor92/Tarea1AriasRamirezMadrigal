def min_may(string): #Cambia minuscula por mayuscula
  palabra=""
  if not isinstance(string,str):
     return print("No ingreso un caracter")
  for x in string:
    if ord(x)<65:
     return print("error, letras")
    elif ord(x)<91:
      return print("error,",x,"no era una letra minuscula")
    elif ord(x)<97:
     return print("error, ingrese letras")
    elif ord(x)>122:
      return print("error, ingrese letras") 
    else:
      num=ord(x)-32
      letra=chr(num)
      palabra=palabra+letra
  return print(palabra)

def busca_w(string): #encuentra "w" en un string
  c=0;
  if isinstance(string,str):
    for i in string:
      if string[c]=="w":
        return print("Se encontró w")
      else: 
        c=c+1
    return print("no habia w")
  else: return print("no era un string")

def compara(int1,int2):#devuelve resta de dos numeros naturales
  if isinstance(int1,int) and isinstance(int2,int):
    if int1<1 or int2<1:
      return print("no ingreso dos numeros naturales")
    else:
      return print(abs(int1-int2))
  else: return print("no ingreso dos numeros naturales")

compara(1,3)
compara("A",3)
compara(5,0)
busca_w(1)
busca_w("ooo")
busca_w("ooow")
min_may("pene")
min_may("pEne")
min_may("}")
min_may(2)