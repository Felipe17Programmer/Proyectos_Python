print 'COMPARACION DE VARIABLES NUMERICAS'

a = float(raw_input('Escriba un numero  A :  '))
b = float(raw_input('Escriba un numero B :  '))
c = float(raw_input('Escriba un numero C :  '))

if a > b and a > c:
    print a, ' es el numero mayor'
    if a % 2 ==0:
        print a, ' es un numero par'
    else:
        print a, ' es un numero impar'

elif b > a and b > c:
    print b, ' es el numero mayor'

    if b % 2 ==0:
        print b, ' es un numero par'
    else:
        print b, ' es un numero impar'

else:
    print c, ' es el numero mayor'

    if c % 2 ==0:
        print c, ' es un numero par'
    else:
        print c, ' es un numero impar'
