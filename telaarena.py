import pygame

pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("")
fundo = pygame.image.load("arenaluta.png")
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
ini=True
while ini:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini==False