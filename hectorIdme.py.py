from turtle import*
from random import*

def dibujarLista(l):
    hideturtle()
    up()
    goto(-200,0)
    for a in range(0, len(l)):
        down()
        goto(-200 + a*30,l[a])
        up()
        goto(-200 + (a+1) * 30, 0)

def burbujaL(lista):
    for i in range(2, len(lista)):
        for j in range(0,len(lista)-1):
            if lista[j] > lista[j+1]:
                c = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = c
    return lista
def seleccion(lista):
  for i in range(0,len(lista)-1):
    mini=i
    for j in range(i+1,len(lista)):
      if lista[j]<lista[mini]:
        mini=j
    if mini!=i:
      c=lista[i]
      lista[i]=lista[mini]
      lista[mini]=c

  return lista

def insercion(lista):
  for i in range(1,len(lista)):
    x=lista[i]
    j=i
    while j>0 and lista[j-1]>x:
      lista[j]=lista[j-1]
      j-=1
    lista[j]=x
  return lista

def sort(lista):
    less = []
    equal = []
    greater = []

    if len(lista) > 1:
        pivot = lista[0]
        for x in lista:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return sort(less)+equal+sort(greater)
    else:
        return lista

def OrdenxMezcla(L):
  if len(L) < 2:
    return L

  mitad=len(L)//2
  left = OrdenxMezcla(L[:mitad])
  right = OrdenxMezcla(L[mitad:])

  res=mezcla(left,right)

  return res

def mezcla(l1,l2):
  l3 = []
  while len(l1)!=0 and len(l2)!=0:
    if l1[0]>l2[0]:
      l3.append(l2.pop(0))
    else:
      l3.append(l1.pop(0))

  return l3+ l1 + l2

def buscar(l,e):
  for i in range(0,len(l)):
    if l[i]==e:
      return True
  return False

def buscarOrd(l,e):
  for i in range(0,len(l)):
    if l[i]==e:
      return True
    elif l[i]>e:
      return False
  return False

def buscaBin(L,e):
  if(len(L)==0):
    return False
  return bBusca(L,e,0,len(L)-1)

def bBusca(L,e, inicio, fin):
  if inicio==fin:
    return L[inicio]==e
  i= (fin+inicio)//2
  if L[i] == e:
    return True
  elif L[i] > e:
    if inicio == i:
      return False
    else:
      return bBusca(L,e,inicio,i-1)
  else:
    return bBusca(L,e,i+1,fin)

# 1 Seleccion
l0=[]

for i in range(0,17):
    l0.append(randrange(0,100))
print "tu lista es ",l0
print
dibujarLista(l0)

print"tu lista ordenada mediante selecion es ",seleccion(l0)
print
clear()
dibujarLista(l0)
clear()

# 2 Insercion
l0=[]

for i in range(0,17):
    l0.append(randrange(0,100))
print "tu lista es ",l0
print
dibujarLista(l0)

print"tu lista ordenada mediante insercion es ",insercion(l0)
print
clear()
dibujarLista(l0)
clear()

#3 Quicksort
l0=[]

for i in range(0,17):
    l0.append(randrange(0,100))
print "tu lista es ",l0
print
dibujarLista(l0)

print"tu lista ordenada mediante quicksort es ",sort(l0)
print
clear()
dibujarLista(l0)
clear()

#4 Mezcla
l0=[]

for i in range(0,17):
    l0.append(randrange(0,100))
print "tu lista es ",l0
print
dibujarLista(l0)

print"tu lista ordenada mediante mezcla es ",OrdenxMezcla(l0)
print
clear()
dibujarLista(l0)
clear()

#5 Burbuja
l0=[]

for i in range(0,17):
    l0.append(randrange(0,100))
print "tu lista es ",l0
print
dibujarLista(l0)

print"tu lista ordenada mediante burbuja es ",burbujaL(l0)
print
clear()
dibujarLista(l0)
clear()

#6 Busqueda binaria
l0=[]

for i in range(0,17):
    l0.append(randrange(0,100))
print "tu lista es ",l0
print
dibujarLista(l0)

print"el elemento a buscar mediante busqueda binaria es ",buscaBin(l0,randrange(0,20))
print
clear()
dibujarLista(l0)
clear()
