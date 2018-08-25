from turtle import*
print '***JUEGO DEL AHORCADO***'


def dibujarRaya():
  forward(20)
def dibujarLetra(letra):
  write(letra)

def dibujarPalabra(palabra):
        hideturtle()
        for i in len(palabra):
            dibujarRaya()
            dibujarLetra(palabra)
    
    
a = raw_input('Escriba : ')
print dibujarPalabra(a)


