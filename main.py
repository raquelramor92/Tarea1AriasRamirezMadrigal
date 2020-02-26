def min_may(string): #Cambia minuscula por mayuscula
  palabra=""
  if not isinstance(string,str):
     return "error 1"
  for x in string:
    if ord(x)<65:
     return "error 2"
    elif ord(x)<91:
      return "error 2"
    elif ord(x)<97:
     return "error 2"
    elif ord(x)>122:
      return "error 2"
    else:
      num=ord(x)-32
      letra=chr(num)
      palabra=palabra+letra
  return palabra

def busca_w(string): #encuentra "w" en un string
  c=0;
  if isinstance(string,str):
    for i in string:
      if string[c]=="w":
        return "Se encontró w"
      else: 
        c=c+1
    return "no habia w"
  else: return "error 1"

def compara(int1,int2):#devuelve resta de dos numeros naturales
  if isinstance(int1,int) and isinstance(int2,int):
    if int1<1 or int2<1:
      return "error 2"
    else:
      return abs(int1-int2)
  else: return "error 1"

print("error 1: tipo incorrecto. error 2: dato incorrecto")
print(compara(1,3))
print(compara("A",3))
print(compara(5,0))
print(busca_w(1))
print(busca_w("ooo"))
print(busca_w("ooow"))
print(min_may("hola"))
print(min_may("holA"))
print(min_may("}"))
print(min_may(2))
