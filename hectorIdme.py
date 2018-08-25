#FUNCIONES

#Problema 1
print 'SUMANDO ELEMENTOS EN UNA LISTA'
l=[1,2,5,7,5,8,58,45,100]
print l
def suma_lista(lista):
    res = 0
    for i in lista:
        res += i
    print 'El resultado de la suma de los elementos de la lista es: ',res
print suma_lista(l)
print #Este print es para dejar un espacio en la consola

#Problema 2
print 'CALCULANDO VALORES DE FUNCIONES'
a = int(raw_input('Ingrese un valor para \'x \' en la funcion f(x)= 2x**2+4x+3 : '))
def f(x):
    return (2*(x**2)) +(4*x)+3
print 'El resultado de la funcion es: ',f(a)
print #Este print es para dejar un espacio en la consola

#Problema 3
print 'CALCULANDO VALORES DE FUNCIONES (2)'
print 'Ahora vamos a imprimir los resultados de la funcion anterior en dominios.'
from turtle import *
from math import*
a = raw_input('Escriba \'opcion 1\' para ingresar los valores al dominio(sin grafico), \nO escriba \'opcion 2\' para dar los resultados con el dominio [-3,3], (con grafico): ')
def f2(mini,maxi):
    for x in range(mini,maxi):
        print (2*(x**2)) +(4*x)+3
if a == 'opcion 1':
    valor_minimo=int(raw_input('Escriba el valor minimo de su dominio: '))
    valor_maximo=int(raw_input('Escriba el valor maximo de su dominio: '))
    print 'Estos son sus valores: '
    print f2(valor_minimo,valor_maximo)
elif a == 'opcion 2' :
    print 'Estos son sus valores: '
    print f2(-3,4)
    speed(50)
    escala=20
    #dibujar los ejes
    color("blue")
    penup()
    goto(-20*escala,-40)
    pendown()
    goto(20*escala,-40)
    color("red")
    penup()
    goto(0,-20*escala)
    pendown()
    goto(0,20*escala)

    penup()
    from time import sleep
    from turtle import *

    def parabolaY(x, a=0.5, b=7, c=0):
        return a*x**2 + b*x + c
    tracer(True)
    color('green')
    width(3)
    goto(0,0)
    down()
    for x in range(5,40):
        goto(x, parabolaY(x))
    up()
    goto(-15,500)
    down()
    for x in range(-40,5):
        goto(x, parabolaY(x))
    up()
    goto(-100,-100)




else:
    print'Escriba correctamente'
    a = raw_input('Escriba su opcion para empezar: ')

print #Este print es para dejar un espacio en la consola

#Problema 4
print 'SUMA DE VECTORES'
def suma_vector(a,b):
    for i in range(len(a)):
        result.append(a[i]+b[i])
    return result
vector =raw_input("Escriba \'start\' para empezar a ingresar valores para los vectores (1) y (2): ")
vector1=[]
vector2=[]
result=[]
c=0
if vector == 'start':
    while c < 2:
        v1 =int(raw_input('Ingrese los valores para el vector 1: '))
        vector1.append(v1)
        c += 1
    c = 0
    while c < 2:
        v2 =int(raw_input('Ingrese los valores para el vector 2: '))
        vector2.append(v2)
        c += 1
    print 'Este es tu vector 1 ',vector1
    print 'Este es tu vector 2 ',vector2
    print 'La suma de los dos vectores es: ',suma_vector(vector1,vector2)
else:
    print 'Error, intentelo nuevamente.'
    vector =raw_input("Escriba \'start\' para empezar a ingresar valores para los vectores (1) y (2): ")
    if vector == 'start':
        while c < 2:
            v1 =int(raw_input('Ingrese los valores para el vector 1: '))
            vector1.append(v1)
            c += 1
        c = 0
        while c < 2:
            v2 =int(raw_input('Ingrese los valores para el vector 2: '))
            vector2.append(v2)
            c += 1
        print 'Este es tu vector 1 ',vector1
        print 'Este es tu vector 2 ',vector2
        print 'La suma de los dos vectores es: ',suma_vector(vector1,vector2)
print #Este print es para dejar un espacio en la consola

#Problema 5
print 'LISTAS AL REVES'
i=0
lista=[]
while i < 10:
    a =int(raw_input('Escribe 10 datos para una lista: '))
    i +=1
    lista.append(a)
print 'Esta es tu lista ',lista

def voltearlista(lista):
    print lista[::-1]
print 'Aqui esta la lista al reves ',voltearlista(lista)
print #Este print es para dejar un espacio en la consola

#Problema 6
print 'COLISION ENTRE DOS ESFERAS?'

t=raw_input("Escriba \'start\' para empezar a ingresar las posicionees tridimensionales de las esferas (1) y (2),\nLos datos se presentaran en una lista[radio,posicion x, posicion y,posicon z]: ")
esfera1=[]
esfera2=[]
result=[]
c=0
def colision(a,b):
    for i in range(len(esfera1)):
        if a[i] == b[i]:
            print True, 'Si hay colision'
        else:
            print False,'No hay colision'
if t == 'start':
    while c < 4:
        e1 =int(raw_input('Ingrese los valores para la esfera 1: '))
        esfera1.append(e1)
        c += 1
    c = 0
    while c < 4:
        e2 =int(raw_input('Ingrese los valores para la esfera 2: '))
        esfera2.append(e2)
        c += 1
    print 'Los valores de tu esfera 1 es: ',esfera1
    print 'Los valores de tu esfera 2 es: ',esfera2
    print colision(esfera1,esfera2)
else:
    'Error , intentalo nuevamente'
print #Este print es para dejar un espacio en la consola

#Problema 7
#No pude resolverlo,problemas con la animacion y parametros de la funcion
