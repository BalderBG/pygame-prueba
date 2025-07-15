import pygame as pg
from newfigura_class import Figura

#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc.
pg.init()
x_display=800
y_display=600

#crear pantalla o sourface
pantalla = pg.display.set_mode( (x_display,y_display) )#definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame" )#agregar un titulo a mi ventana

game_over=True

rectangulo1 = Figura(0,300,(223, 40, 220))
rectangulo2 = Figura(0,350,vx=2,vy=2)
rectangulo3 = Figura(0,400,(52,185,36),vx=2,vy=2)

circulo1 = Figura(0,300,radio=30)
circulo2 = Figura(0,360, (223, 40, 84),radio=15,vx=2,vy=2 )
circulo3 = Figura(0,400,(40, 223, 46),radio=20,vx=1,vy=2)

while game_over:
    for eventos in pg.event.get():  #captura  todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False


    
    pantalla.fill( (50, 189, 172) )#asignar un color a la pantalla
    #agregamos objeto a la pantalla

    circulo1.mover(x_display,y_display)
    circulo1.dibujarCirculo(pantalla)

    circulo2.mover(x_display,y_display)
    circulo2.dibujarCirculo(pantalla)

    circulo3.mover(x_display,y_display)
    circulo3.dibujarCirculo(pantalla)
    

    rectangulo1.mover(x_display,y_display)
    rectangulo2.mover(x_display,y_display)
    rectangulo3.mover(x_display,y_display)
    
    #draw.rect(sourceface,color en (rgb),posiciones(posicionX,posicionY,tamañoX,tamañoY))
    
    rectangulo1.dibujarRectangulo(pantalla)
    rectangulo2.dibujarRectangulo(pantalla)
    rectangulo3.dibujarRectangulo(pantalla)
    
    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()