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

# Definindo o relógio para controlar a taxa de atualização (FPS)
clock = pygame.time.Clock()
FPS = 120  # Frames por segundo

# Loop principal do jogo
running = True
while running:
    # Controle de FPS
    clock.tick(FPS)

    # Limpar a tela (desenhando o fundo)
    plano()

    # Atualizando a posição dos lutadores
    lutador1.movimentacao()  # Lutador 1 se move com as teclas A e D
    lutador2.movimentacao2()  # Lutador 2 se move com as teclas de seta

    # Desenhando a hitbox do lutador 1 (em azul)
    pygame.draw.rect(janela, (0, 0, 255), lutador1.rect, 2)  # Desenhando a hitbox azul do lutador 1

    # Desenhando o soco do lutador 1, se ativo (em vermelho)
    if lutador1.ataque_ativo:
        pygame.draw.rect(janela, (255, 0, 0), lutador1.rect, 2)  # Desenhando a hitbox do soco em vermelho

    # Desenhando a hitbox do lutador 2 (em verde)
    pygame.draw.rect(janela, (0, 255, 0), lutador2.rect, 2)  # Desenhando a hitbox verde do lutador 2

    # Desenhando o soco do lutador 2, se ativo (em laranja)
    if lutador2.ataque_ativo:
        pygame.draw.rect(janela, (255, 165, 0), lutador2.rect, 2)  # Desenhando a hitbox do soco em laranja

    # Verificando eventos
    for event in pygame.event.get():
        # Se o evento for o de fechar a janela, termina o loop
        if event.type == pygame.QUIT:
            running = False

    # Atualizando a tela para refletir as mudanças feitas
    
    pygame.display.update()

# Finalizando o Pygame quando o jogo é fechado
pygame.quit()

