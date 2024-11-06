import pygame

Gravidade = 2
altura_tela = 835
largura_tela = 1550
velocidade_pulo = 100
class Lutador():
    def __init__(self,x,y):


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
        if self.rect.right > largura_tela:
            self.rect.right = largura_tela
        if self.rect.left < 0:
            self.rect.left = 0


        
    def movimentação2(self):
        mov_velocidade=3
        dimensao_x=0
        dimensao_y=0
        mov=pygame.key.get_pressed()
        if mov[pygame.K_RIGHT]:
            dimensao_x=mov_velocidade
        elif mov[pygame.K_LEFT]:
            dimensao_x=-mov_velocidade
        self.rect.x +=dimensao_x
        self.rect.y +=dimensao_y
        if self.rect.right > largura_tela:
            self.rect.right = largura_tela
        if self.rect.left < 0:
            self.rect.left = 0

    def box(self,surface):
        pygame.draw.rect (surface, (0,0,255),self.rect)

    def jump(self):
        for event in pygame.event.get():
            if event.key == pygame.K_UP or event.key() == pygame.K_SPACE:
                testando = 0
                
            
                





    
    #def golpe(self, surface):
        #if mov[pygame.K_ ]
        


    #all_sprites.update()
  

    #hits = pygame.sprite.spritecollide(lutador1, lutador2, True) 
        #if hits: 