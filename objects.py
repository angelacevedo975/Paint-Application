import pygame
from constants import *

class Color(pygame.sprite.Sprite):
    colores={
        "red":(255,0,0),
        "blue":(0,0,255),
        "green":(0,255,0),
        "aqua":(0,128,128),
        "purple":(128,0,128),
        "black":(0,0,0),
        "pink":(255,0,128),
        "yellow":(255,255,0),
        "white":(255,255,255)
        }
    
    
    def __init__(self, pos_x, pos_y, color):
        super().__init__()
        self.image= pygame.Surface( (30,30) )
        self.image.fill( self.colores[color] )
        self.rect= self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.color=self.colores[color]
        
    def validate(self, pos):
        return pos[0]>self.pos_x+WIDTH-120 and pos[0]<self.pos_x+30+WIDTH-120 and pos[1]>self.pos_y and pos[1]<self.pos_y+30


class Pallete(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image= pygame.Surface( (120, HEIGHT) )
        self.image.fill( PALLETE )
        
        self.rect=self.image.get_rect()
        self.rect.x=WIDTH-self.rect.width
        self.rect.y=0
        
        self.colors= pygame.sprite.Group()
        self.other=pygame.sprite.Group()
        
        self.add_colors()
        self.add_other()
        
    def add_other(self):
        self.smaller= Color(20,HEIGHT-50,"black")
        self.bigger=Color(70, HEIGHT-50, "black")
        
        
        self.other.add(self.smaller)
        self.other.add(self.bigger)
        
        
        self.other.draw(self.image)
        
    def check_size(self, pos):
        if self.smaller.validate(pos):
            return -1
        if self.bigger.validate(pos):
            return 1
        return 0
        
    def add_colors(self):
        red=Color(20,20,"red")
        blue=Color(70,20,"blue")
        green=Color(20,70,"green")
        aqua=Color(70,70,"aqua")
        purple=Color(20, 120,"purple")
        black=Color(70,120,"black")
        pink=Color(20, 170,"pink")
        yellow=Color(70,170,"yellow")
        white= Color(30, HEIGHT-100,"white")
        
        self.colors.add(red)
        self.colors.add(blue)
        self.colors.add(green)
        self.colors.add(aqua)
        self.colors.add(purple)
        self.colors.add(black)
        self.colors.add(pink)
        self.colors.add(yellow)
        self.colors.add(white)
        
        self.colors.draw(self.image)
        
    def check_colors(self, pos):
        print(pos)
        for col in self.colors:
            if col.validate(pos):
                return col.color
            
        return None
    
    def click_here(self, mouse_pos):
        return mouse_pos[0]>self.rect.x and mouse_pos[0]<WIDTH and mouse_pos[1]>0 and mouse_pos[1]<HEIGHT
            
        
        
