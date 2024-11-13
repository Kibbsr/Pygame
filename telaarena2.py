import pygame
from teste import Lutador  # Importando a classe Lutador de outro arquivo (teste.py)

# Inicializando o pygame
pygame.init()

# Definindo as dimensões da tela
largura_tela = 1550
altura_tela = 835

# Criando a janela do jogo
janela = pygame.display.set_mode((largura_tela, altura_tela))

# Definindo o título da janela do jogo
pygame.display.set_caption("Jogo de Luta")

# Carregando e redimensionando o fundo
fundo = pygame.image.load("arenaluta2.png").convert_alpha()
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

# Função que desenha o fundo na tela
def plano():
    janela.blit(fundo, (0, 0))

# Criando os dois lutadores
lutador1 = Lutador(1300, 600)
lutador2 = Lutador(100, 600)

# Loop principal do jogo, responsável por controlar a execução do jogo
ini = True

janela.blit(fundo,(0,0))
lutador1=Lutador(1300, 600)
lutador2=Lutador(100, 600)
ini=True
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


pygame.quit()  # Finaliza o Pygame