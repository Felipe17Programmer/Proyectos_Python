print 'SUMA DE PARES'

a= int(raw_input('Escribe un numero A :  '))
b= int(raw_input('Escribe un numero B :  '))
c= int(raw_input('Escribe un numero C :  '))

d= a % 2 == 0
e= b % 2 == 0
f= c % 2 == 0

def suma(x,y,z):
    print 'la suma de los pares es:', x + y + z

if ( d and e and f ) == True:
    print 'Hay tres numeros pares'
    print suma(a,b,c)
elif (d and e == True ) and (f == False):
    print 'Hay dos numero pares'
    print  suma(a,b,0)
elif (e and f == True ) and (d == False):
    print 'Hay dos numero pares'
    print suma(b,c,0)
elif (f and d == True ) and (e == False):
    print 'Hay dos numero pares'
    print suma(a,c,0)
elif (f and e == False ) or (d == True):
    print 'Hay un numero par',
elif (d and f == False ) or (e == True):
    print 'Hay un numero par'
elif (e and d == False ) or (f == True):
    print 'Hay un numero par'
else :
    print 'No hay ningun numero par'
