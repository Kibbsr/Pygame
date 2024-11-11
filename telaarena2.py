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

while ini:
    # Desenhando o fundo da tela
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
            ini = False

    # Atualizando a tela para refletir as mudanças feitas
    pygame.display.update()

    # Re-desenhando o fundo novamente (não é necessário, pois a função 'plano' já o desenha)
    # janela.blit(fundo, (0, 0))  # Esta linha é redundante e pode ser removida

# O segundo loop (inic) não é necessário, já que ele serve para apenas esperar e fechar o jogo,
# mas isso já é tratado no primeiro loop. Vamos comentá-lo também.

# A segunda parte do código parece ser redundante e não é necessária para o jogo funcionar.

# iniciando um segundo loop que não faz nada além de esperar que o evento de QUIT aconteça
clock = pygame.time.Clock()
FPS = 120

inic = True
while inic:
    clock.tick(FPS)
    plano()  # Desenhando o fundo

    # Verificando se a janela foi fechada
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inic = False

    # Atualizando a tela
    pygame.display.update()

# Finalizando o Pygame quando o jogo é fechado
pygame.quit()
