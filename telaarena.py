import pygame

pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("")
fundo = pygame.image.load("arenaluta.png").convert_alpha()
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
def plano():
    janela.blit(fundo,(0,0))
ini=True
while ini:
    plano()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini=False
    pygame.display.update()
pygame.quit()