print '***JUEGO DEL AHORCADO***'
from random import*


lista_palabras = {'Universidad' : 'Lugar donde estas ahora','Python' : 'Lenguaje en el cual fue hecho el juego','oso' : 'Animal salvaje','gaviota' : 'animal volador','iracundo' : 'grupo de musica','salsa' : 'genero de musica peruana'}

intentos = 9
palabra = choice(lista_palabras.keys())
espacio = ['_']*(len(palabra))
print '  '.join(espacio)
while intentos > 0:
    letra = raw_input('=>')
    acierto = False
    for j,l in enumerate(palabra):
        if l == letra:
            espacio[j] = l
            acierto = 1
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
