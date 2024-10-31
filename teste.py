import pygame

pygame.init()

#lutador_img = pygame.image.load("").convert_alpha()
#lutador_img = pygame.transform.scale(lutador_img,)#dimensões,))

class Lutador():
    def __init__(self,x,y):
       
       # pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((x,y,50,150))
        #self.rect.x  = 
        #self.rect.bottom = 
        #self.speedx = 0
    def box(self,surface):
        pygame.draw.rect (surface, (0,0,255), self.rect)
