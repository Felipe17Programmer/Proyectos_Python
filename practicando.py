print 'dibujando con turtle'
print'tienes pciones como dibujar cuadrado ,circulo,rombo,hexagono,triangulo'
x=raw_input('eleccion: ')
from turtle import*
def poligono(n):
    i=0
    while i<n:
        forward(100)
        right(360/n)
        i+=1

if x=='cuadrado':
    print poligono(4)
if x=='circulo':
    print circle(70)
