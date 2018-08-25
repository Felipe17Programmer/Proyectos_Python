print '***JUEGO DEL AHORCADO***'
from random import*
from turtle import*
setup(640,480,640,0)
title('EL JUEGO DEL AHORCADO')

def dibujar_ahorcado(errores):
  pensize(4)
  if errores==1:
    goto(100,0)
  elif errores==2:
    penup()
    goto(50,0)
    pendown()
    goto(50,150)
  elif errores==3:
    goto(120,150)
  elif errores==4:
    penup()
    goto(100,150)
    pendown()
    goto(100,110)
  elif errores==5:
    penup()
    goto(100,90)
    pendown()
    circle(10)
  elif errores==6:
    goto(100,50)
  elif errores==7:
    goto(90,20)
  elif errores==8:
    penup()
    goto(100,50)
    pendown()
    goto(110,20)
  elif errores==9:
    penup()
    goto(80,75)
    pendown()
    goto(120,75)
    penup()
    goto(50,-120)
    write('Perdiste!!!!!',False,'right',('arial',20,'bold italic'))

lista_palabras = ['universidad' ,'Python','oso','gaviota','iracundo','salsa','Peru','Paris','Deadpool','Avengers','meme','cultura','naturaleza','etopeya']
errores = 0
intentos = 9
palabra = choice(lista_palabras)
espacio = ['_']*(len(palabra))
print ' '.join(espacio)
while intentos > 0:
    letra = raw_input('=>')
    acierto = False
    for i,l in enumerate(palabra):
        if l == letra:
            espacio[i] = l
            acierto = 1
    if acierto:
        print
        print 'Muy Bien!'
    else:
        print
        print 'Muy Mal! Sigue intentando'
        intentos -= 1
        errores += 1
        dibujar_ahorcado(errores)
        print 'Te quedan ',intentos,' intentos ahora.'



    print ' '.join(espacio)

    if '_' not in espacio:
        print 'Lo lograste!!'
        penup()
        goto(50,-120)
        write('Ganaste!!!!!',False,'right',('arial',20,'bold italic'))
        break
if intentos == 0:
    print
    print 'Lo sentimos se le acabaron los intentos'
    print 'La palabra era ' + palabra
