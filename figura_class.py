import pygame as pg

class Rectangulo:
    def __init__(self,pos_x,pos_y,color=(255,255,255),w=20,h=20,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy  

    def mover(self,x_max,y_max):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if self.pos_x == x_max or self.pos_x == 0:
            self.vx = self.vx*-1
        if self.pos_y == y_max or self.pos_y == 0:
            self.vy = self.vy*-1 

    def dibujar(self,pantalla):  
        pg.draw.rect(pantalla,self.color,(self.pos_x,self.pos_y,self.h,self.w))         


class Circulo:
    def __init__(self,pos_x, pos_y, color=(255,255,255), radio = 10,vx=1, vy=1 ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy  

    def mover(self,x_max,y_max):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if self.pos_x == x_max or self.pos_x == 0:
            self.vx = self.vx*-1
        if self.pos_y == y_max or self.pos_y == 0:
            self.vy = self.vy*-1 


    def dibujar(self, pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y), self.radio)