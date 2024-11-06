# Importando o módulo Pygame, que fornece funcionalidades para criar jogos
import pygame


class Lutador():
    def __init__(self,x,y):

        self.rect = pygame.Rect((x,y,50,150))
    def movimentação(self):
        # Define a velocidade de movimento (3 pixels por atualização)
        mov_velocidade = 3
        # Inicializa as variáveis que irão controlar os movimentos no eixo X e Y
        dimensao_x = 0
        dimensao_y = 0

        # Obtém o estado das teclas pressionadas (True ou False)
        mov = pygame.key.get_pressed()

        # Verifica se a tecla 'A' foi pressionada (movimento para a esquerda)
        if mov[pygame.K_a]:
            dimensao_x = -mov_velocidade
        # Verifica se a tecla 'D' foi pressionada (movimento para a direita)
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