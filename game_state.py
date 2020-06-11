import pygame
from constants import *
from objects import *

class Game:
     
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)
         
    
    def start(self):
        self.init()
    
    def init(self):
        self.running=True
        self.color= COLOR
        self.drawing=False
        self.size=5
        
        self.pallete=Pallete()
        
        self.sprites=pygame.sprite.Group()
        self.sprites.add(self.pallete)
        
        self.surface.fill( SCREEN_COLOR )
        self.run()
    
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos=pygame.mouse.get_pos()
                    if self.pallete.click_here(mouse_pos):
                        color=self.pallete.check_colors(mouse_pos)
                        if color != None:
                            self.color=color
                            
                            
                    if self.size + self.pallete.check_size(mouse_pos)>1:
                        self.size+= self.pallete.check_size(mouse_pos)
                        
                        
                
        mouse_pressed= pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            self.drawing=True
        else:
            self.drawing=False
            
        
    
    def draw(self):
        if self.drawing:
            surf= pygame.Surface( (self.size, self.size) )
            rect=surf.get_rect()
            rect.center= pygame.mouse.get_pos()
            surf.fill( self.color )
            
            self.surface.blit( surf, rect )
        
        font = pygame.font.Font("freesansbold.ttf", 20)
        text=font.render(f"Size: {self.size}", True, (0,0,0))
        text_rect= text.get_rect()
        text_rect.center= ( WIDTH//2, HEIGHT-30 ) 
        
        surf_text=pygame.Surface( (text_rect.width, text_rect.height) )
        surf_text.fill( (255,255,255) )
        rect_surf= surf_text.get_rect()
        rect_surf.center= ( WIDTH//2, HEIGHT-30 ) 
            
        self.sprites.draw(self.surface)
        self.surface.blit(surf_text, rect_surf)
        self.surface.blit(text, text_rect)
    
    def run(self):
        while self.running:
            self.event()
            self.draw()
            self.update()
    
    def update(self):
        pygame.display.flip()