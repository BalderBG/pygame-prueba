import pygame as pg
from figura_class import Rectangulo

#inicializar todos los modulos de pygame, pantallas, objetos, eventos, sonidos, etc.
pg.init()
x_display=1280
y_display=720

#crear pantalla o sourface
pantalla = pg.display.set_mode( (x_display,y_display) )#definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame" )#agregar un titulo a mi ventana

game_over=True

rectangulo1 = Rectangulo(0,300,(223, 40, 220))
rectangulo2 = Rectangulo(0,350,vx=2,vy=2)
rectangulo3 = Rectangulo(0,400,(52,185,36),vx=2,vy=2)


while game_over:
    for eventos in pg.event.get():#capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill( (50, 189, 172) )#asignar un color a la pantalla
    #agregamos objeto a la pantalla
  
    rectangulo1.mover(x_display,y_display)
    rectangulo2.mover(x_display,y_display)
    rectangulo3.mover(x_display,y_display)
    
    #draw.rect(sourceface,color en (rgb),posiciones(posicionX,posicionY,tamañoX,tamañoY))
    rectangulo1.dibujar(pantalla)
    rectangulo2.dibujar(pantalla)
    rectangulo3.dibujar(pantalla)
    """
    pg.draw.rect(pantalla,rectangulo1.color,(rectangulo1.pos_x,rectangulo1.pos_y,rectangulo1.h,rectangulo1.w))
    pg.draw.rect(pantalla,rectangulo2.color,(rectangulo2.pos_x,rectangulo2.pos_y,rectangulo2.h,rectangulo2.w))
    pg.draw.rect(pantalla,rectangulo3.color,(rectangulo3.pos_x,rectangulo3.pos_y,rectangulo3.h,rectangulo3.w))
    """
    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()