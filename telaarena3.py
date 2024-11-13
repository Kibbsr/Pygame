import pygame
# Importando a classe Lutador do arquivo 'teste.py'. Ela define o comportamento dos lutadores no jogo
from teste import Lutador



# Função para detectar colisão entre dois lutadores
def verificar_colisao(lutador1, lutador2):
    """Verifica se o golpe de lutador1 atingiu lutador2, só causando dano se o golpe estiver ativo."""
    
    # Verificar se lutador1 está atacando
    if lutador1.ataque_ativo:
        if lutador1.soco().colliderect(lutador2.rect):  # Colisão com o soco
            lutador2.aplicar_dano(lutador1.dano_soco)
        if lutador1.socoespecial().colliderect(lutador2.rect):  # Colisão com o golpe especial
            lutador2.aplicar_dano(lutador1.dano_golpe_especial)
    
    # Verificar se lutador2 está atacando
    if lutador2.ataque_ativo:
        if lutador2.soco().colliderect(lutador1.rect):  # Colisão com o soco de lutador2
            lutador1.aplicar_dano(lutador2.dano_soco)
        if lutador2.socoespecial().colliderect(lutador1.rect):  # Colisão com o golpe especial de lutador2
            lutador1.aplicar_dano(lutador2.dano_golpe_especial)

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
fundo = pygame.image.load("arenaluta3.png").convert_alpha()

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

