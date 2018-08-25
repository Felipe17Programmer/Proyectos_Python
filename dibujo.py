

from turtle import *

        
def draw(c1):#falta c2
    #inicializar dibujo
    hideturtle()#esconde la flecha de turtle
    tracer(0, 0)#dibuja instant
    clear()#borra la pantalla

    screen = list(screensize())
    
    #dibujar
    penup()#levantamos en lapiz
    goto(c1[1],c1[2])#nos ubicamos en la posicion del centro
    
    pendown()#bajamos en lapiz
    circle(c1[0])#dibujamos el circulo c1

    if(c1[1]>screen[0] or c1[1]<-screen[0]):
        c1[3]=-c1[3]
    if(c1[2]>screen[0] or c1[2]<-screen[0]):
        c1[4]=-c1[4]
    #mover el circulo en x de 0.1
    c1[1]+=c1[3]
    #mover el circulo en y de 0.05
    c1[2]+=c1[4]

    #avisar que terminamos de dibujar
    update()#actualiza la pantalla
  
#creamos el circulo n°1 | falta n°2    
circulo1 = [45,50,-100,0.1,50.05]#radio,x,y
while True:#bucle infinito
    draw(circulo1)#dibujamos
done()
