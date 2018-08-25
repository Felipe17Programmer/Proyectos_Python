a = int(raw_input('Por favor ingrese un numero para a'))
b = int(raw_input('Por favor ingrese un numero para b'))

producto = 0

while b != 0:
    producto = producto + a
    b = b - 1

print 'El producto entre los dos numeros es: ', producto

c = int(raw_input('Por favor ingrese un numero para c'))
d = int(raw_input('Por favor ingrese un numero para d'))

s = 0
r = 0

while s < d:
    r = r + c
    s = s + 1

print r
