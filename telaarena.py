import pygame
from teste import Lutador


pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("")
fundo = pygame.image.load("arenaluta.png").convert_alpha()
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))


<<<<<<< HEAD





pulando = False
=======
pygame.mixer.init()
pygame.mixer.music.load("musica1.ogg")
pygame.mixer.music.set_volume(0.4)


pygame.mixer.music.play(loops=-1)
>>>>>>> e08a13e6d62895fe886957e902021b04517d35a3
def plano():
    janela.blit(fundo,(0,0))
lutador1=Lutador(100, 600)
lutador2=Lutador(1000, 600)
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
pygame.quit()