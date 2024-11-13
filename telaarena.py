# import pygame
# from teste import Lutador


# pygame.init()
# largura_tela = 1550
# altura_tela = 835
# janela = pygame.display.set_mode((largura_tela, altura_tela))
# pygame.display.set_caption("")
# fundo = pygame.image.load("arenaluta1.png").convert_alpha()
# fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))










# pygame.mixer.init()
# pygame.mixer.music.load("721472__victor_natas__boss-fight.ogg")
# fim_jogo = pygame.mixer.Sound("527650__fupicat__winsquare.ogg")
# pygame.mixer.music.set_volume(0.4)
# pygame.mixer.music.play(loops=-1)




# def plano():
#     janela.blit(fundo,(0,0))
# lutador1=Lutador(100, 600)
# lutador2=Lutador(1000, 600)
# ini=True

# clock = pygame.time.Clock()
# FPS = 120

# while ini:
#     clock.tick(FPS)
#     plano()
#     lutador1.movimentacao()
#     lutador2.movimentacao2()
#     lutador1.box(janela)
#     lutador2.box(janela)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             ini=False
#     pygame.display.update()

#     barra_largura = 100
#     barra_altura = 10
#     barra_x = 50 
#     barra_y = 20 
#     jogador = Lutador(100,150)
#     vida_restante = (jogador.hp / 100) * barra_largura
#     pygame.draw.rect(janela, (169, 169, 169), pygame.Rect([barra_x, barra_y], [barra_largura, barra_altura]))
#     pygame.draw.rect(janela, (0, 255, 0), pygame.Rect(barra_x, barra_y, vida_restante, barra_altura))


# fim_jogo.play()
# pygame.quit()
import pygame
from teste import Lutador  # Certifique-se de que a classe Lutador está definida corretamente

pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Luta")
fundo = pygame.image.load("arenaluta1.png").convert_alpha()
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

pygame.mixer.init()
pygame.mixer.music.load("721472__victor_natas__boss-fight.ogg")
fim_jogo = pygame.mixer.Sound("527650__fupicat__winsquare.ogg")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

def plano():
    janela.blit(fundo, (0, 0))

# Instanciando os lutadores
lutador1 = Lutador(100, 600)
lutador2 = Lutador(1000, 600)
ini = True

clock = pygame.time.Clock()
FPS = 120

while ini:
    clock.tick(FPS)
    plano()  # Desenha o fundo
    lutador1.movimentacao()  # Movimenta o lutador1
    lutador2.movimentacao2()  # Movimenta o lutador2
    lutador1.box(janela)  # Desenha o lutador1
    lutador2.box(janela)  # Desenha o lutador2

    # Desenho da barra de vida para o lutador1
    barra_largura = 250
    barra_altura = 50
    barra_x = 15
    barra_y = 20
    vida_restante1 = (lutador1.hp / 100) * barra_largura
    pygame.draw.rect(janela, (169, 169, 169), pygame.Rect([barra_x, barra_y], [barra_largura, barra_altura]))
    pygame.draw.rect(janela, (0, 255, 0), pygame.Rect(barra_x, barra_y, vida_restante1, barra_altura))

    # Desenho da barra de vida para o lutador2
    barra_x2 = 1280
    barra_y2 = 20
    vida_restante2 = (lutador2.hp / 100) * barra_largura
    pygame.draw.rect(janela, (169, 169, 169), pygame.Rect([barra_x2, barra_y2], [barra_largura, barra_altura]))
    pygame.draw.rect(janela, (0, 255, 0), pygame.Rect(barra_x2, barra_y2, vida_restante2, barra_altura))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini = False

    pygame.display.update()  # Atualiza a tela

fim_jogo.play()  # Som de fim de jogo (caso aplicável)
pygame.quit()  # Finaliza o Pygame
