import pygame

pygame.init()
class Lutador():
    def _init_(self,x,y):

        self.rect = pygame.Rect((x,y,50,150))
    def movimentação(self):
        mov_velocidade=3
        dimensao_x=0
        dimensao_y=0
        mov=pygame.key.get_pressed()
        if mov[pygame.K_a]:
            dimensao_x=-mov_velocidade
        elif mov[pygame.K_d]:
            dimensao_x=mov_velocidade
        self.rect.x +=dimensao_x
        self.rect.y +=dimensao_y
    def movimentação2(self):
        mov_velocidade=3
        dimensao_x=0
        dimensao_y=0
        mov=pygame.key.get_pressed()
        if mov[pygame.K_LEFT]:
            dimensao_x=mov_velocidade
        elif mov[pygame.K_RIGHT]:
            dimensao_x=-mov_velocidade
        self.rect.x +=dimensao_x
        self.rect.y +=dimensao_y
    def box(self,surface):
        pygame.draw.rect (surface, (0,0,255),self.rect)