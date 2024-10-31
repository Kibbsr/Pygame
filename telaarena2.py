import pygame

pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("")
fundo = pygame.image.load("arenaluta2.png").convert_alpha()
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
def plano():
    janela.blit(fundo,(0,0))
inic=True
while inic:
    plano()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inic=False
    pygame.display.update()
pygame.quit()