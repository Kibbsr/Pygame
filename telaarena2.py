import pygame
from teste import Lutador

pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("")
fundo = pygame.image.load("arenaluta2.png").convert_alpha()
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
def plano():
    janela.blit(fundo,(0,0))
lutador1=Lutador(1000, 600)
lutador2=Lutador(100, 600)
ini=True
while ini:
    plano()
    lutador1.movimentação()
    lutador2.movimentação2()
    lutador1.box(janela)
    lutador2.box(janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini=False
    pygame.display.update()
    janela.blit(fundo,(0,0))
inic=True
while inic:
    plano()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inic=False
    pygame.display.update()
pygame.quit()