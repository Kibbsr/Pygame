import pygame
from teste import Lutador

pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("")
fundo = pygame.image.load("ARENA.png").convert()
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
tela = pygame.image.load("arenaluta.png").convert()
def plano():
    janela.blit(fundo,(0,0))

lutador1=Lutador(100, 600)
lutador2=Lutador(1000, 600)
ini=True
while ini:
    for event in pygame.event.get():
        plano()
        if event.type == pygame.KEYUP:
            tela.blit(fundo,(500,200))
        if event.type == pygame.QUIT:
            ini=False
    pygame.display.update()
