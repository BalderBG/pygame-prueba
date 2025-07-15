import pygame as pg

#inicializamos los modulos de pygame, pantallas, objetos, eventos, sonidos.. etc
pg.init()



pantalla = pg.display.set_mode( (1280, 720) )
pg.display.set_caption( "Intro pygame ")

game_over = True
x = 0
vx = 1
y = 0
vy = 1


while game_over:
    for eventos in pg.event.get(): #capturar todos los eventos mientras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill((60, 140, 100) ) #esto es la gama de colores de la pantalla
    #agregamos objeto a la pantalla
    x += vx
    y += vy

    if x == 1280 or x == 0:
        vx = vx* -1

    if y == 720 or y == 0:
        vy = vy* -1

    #draw.rect(sourceface, color en (rgb) y posiciones(posicion en X y posicion en Y, y el tamaño del objeto, lo mismo, X e Y) ) 

    pg.draw.rect(pantalla, (222, 58, 31),(x, y, 10,10))
    pg.draw.rect(pantalla, (222, 58, 31),(x+10, y+20, 10,10))


    pg.display.flip() #funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()