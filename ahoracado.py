intentos = 9
palabra = 'mono'
espacio = ['_']*(len(palabra))
print ' '.join(espacio)
while intentos > 0:
    letra = raw_input('=>')
    acierto = False
    for j,l in enumerate(palabra):

        if l == letra:
            espacio[j] = l
            acierto = 1
            print j

    if acierto:
        print
        print 'Muy Bien!'
    else:
        print
        print 'Muy Mal! Sigue intentando'
        intentos -= 1
        print 'Te quedan ',intentos,' intentos ahora.'

    print ' '.join(espacio)

    if '_' not in espacio:
        print 'Lo lograste!!'
        break
if intentos == 0:
    print
    print 'Lo sentimos se le acabaron los intentos'
    print 'La palabra era ' + palabra
