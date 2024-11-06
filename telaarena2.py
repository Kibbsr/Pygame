# Importando o módulo pygame, que é usado para criar jogos e aplicações multimídia
import pygame
# Importando a classe Lutador do arquivo 'teste.py'. Ela define o comportamento dos lutadores no jogo
from teste import Lutador

# Inicializando o pygame, necessário para utilizar os recursos gráficos e de som do Pygame
pygame.init()

# Definindo as dimensões da tela (janela do jogo)
largura_tela = 1550  # Largura da tela em pixels
altura_tela = 835    # Altura da tela em pixels

# Criando a janela do jogo com as dimensões especificadas
janela = pygame.display.set_mode((largura_tela, altura_tela))

# Definindo o título da janela do jogo (não está sendo usado aqui, está vazio)
pygame.display.set_caption("")

# Carregando a imagem do fundo do jogo (provavelmente uma arena de luta)
fundo = pygame.image.load("arenaluta2.png").convert_alpha()

# Redimensionando a imagem do fundo para que ela tenha as dimensões da janela
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

# Função que desenha o fundo na tela
def plano():

    # Blitando (desenhando) a imagem do fundo na posição (0,0) da janela
    janela.blit(fundo, (0, 0))

# Criando dois objetos Lutador, um na posição (1000, 600) e outro em (100, 600)
lutador1 = Lutador(1000, 600)
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

    # Atualizando a posição dos lutadores, conforme o controle do jogador
    lutador1.movimentação()  # Lutador 1 se move usando as teclas A e D
    lutador2.movimentação2() # Lutador 2 se move usando as teclas de seta

    # Desenhando os lutadores na tela, de acordo com suas posições
    lutador1.box(janela)
    lutador2.box(janela)

    # Loop para verificar os eventos (interações) na janela
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
