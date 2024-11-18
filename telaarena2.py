import pygame
from teste import Lutador  # Importando a classe Lutador de outro arquivo (teste.py)
import subprocess
import sys
def verificar_colisao(lutador1, lutador2):
    """Verifica se o golpe de lutador1 atingiu lutador2, só causando dano se o golpe estiver ativo."""

    # Verificar se lutador1 está atacando (golpe normal ou especial)
    if lutador1.ataque_ativo:
        if lutador1.soco().colliderect(lutador2.rect):  # Colisão com o soco
            lutador2.aplicar_dano(lutador1.dano_soco)  # Aplica 2 de dano
            lutador1.ataque_ativo = False  # Desativa o ataque após causar dano

    if lutador1.golpe_ativo:
        if lutador1.chute().colliderect(lutador2.rect):  # Colisão com o golpe especial
            lutador2.aplicar_dano(lutador1.dano_chute)  # Aplica 5 de dano
            lutador1.golpe_ativo = False  # Desativa o golpe especial após causar dano

    # Verificar se lutador2 está atacando (golpe normal ou especial)
    if lutador2.ataque_ativo:
        if lutador2.soco().colliderect(lutador1.rect):  # Colisão com o soco de lutador2
            lutador1.aplicar_dano(lutador2.dano_soco)  # Aplica 2 de dano
            lutador2.ataque_ativo = False  # Desativa o ataque após causar dano

    if lutador2.golpe_ativo:
        if lutador2.chute().colliderect(lutador1.rect):  # Colisão com o golpe especial de lutador2
            lutador1.aplicar_dano(lutador2.dano_chute)  # Aplica 5 de dano
            lutador2.golpe_ativo = False  # Desativa o golpe especial após causar dano
# Inicializando o pygame
pygame.init()

# Definindo as dimensões da tela
largura_tela = 1540
altura_tela = 805

# Criando a janela do jogo
janela = pygame.display.set_mode((largura_tela, altura_tela))

# Definindo o título da janela do jogo
pygame.display.set_caption("Jogo de Luta")

# Carregando e redimensionando o fundo
fundo = pygame.image.load("arenaluta2.png").convert_alpha()
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

tela_vitoria = pygame.image.load("ARENA.png").convert_alpha()
tela_vitoria = pygame.transform.scale(tela_vitoria, (largura_tela, altura_tela))
# Função que desenha o fundo na tela
def plano():
    janela.blit(fundo, (0, 0))

# Função para limitar a posição de um lutador dentro dos limites da tela
def limitar_posicao(lutador):
    if lutador.rect.left < 0:
        lutador.rect.left = 0
    if lutador.rect.right > largura_tela:
        lutador.rect.right = largura_tela
    if lutador.rect.top < 0:
        lutador.rect.top = 0
    if lutador.rect.bottom > altura_tela:
        lutador.rect.bottom = altura_tela

# Criando dois objetos Lutador, um na posição (1000, 600) e outro em (100, 600)
lutador1 = Lutador(1300, 600)
lutador2 = Lutador(100, 600)
pygame.mixer.init()
pygame.mixer.music.stop
pygame.mixer.music.load("416632__sirkoto51__castle-music-loop-1.ogg")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

# Loop principal do jogo, responsável por controlar a execução do jogo
ini = True
clock = pygame.time.Clock()
FPS = 120
while ini:
    clock.tick(FPS)
    plano()  # Desenha o fundo

    lutador1.atualizar_animacao()
    lutador2.atualizar_animacao()
    lutador1.movimentacao()  # Movimenta o lutador1
    lutador2.movimentacao2()  # Movimenta o lutador2

    # Limita a posição dos lutadores dentro da tela
    limitar_posicao(lutador1)
    limitar_posicao(lutador2)

    lutador1.box(janela)  # Desenha o lutador1
    lutador2.box(janela) 
    # Verificar colisões entre os dois lutadores
    verificar_colisao(lutador1, lutador2)
    # Desenho da barra de vida para o lutador1
    barra_largura = 250
    barra_altura = 50
    barra_x = 15
    barra_y = 20
    vida_restante1 = (lutador1.hp / 700) * barra_largura
    pygame.draw.rect(janela, (255, 0, 0), pygame.Rect([barra_x, barra_y], [barra_largura, barra_altura]))
    pygame.draw.rect(janela, (55, 125, 34), pygame.Rect(barra_x, barra_y, vida_restante1, barra_altura))
    # Desenho da barra de vida para o lutador2
    barra_x2 = 1280
    barra_y2 = 20
    vida_restante2 = (lutador2.hp / 700) * barra_largura
    pygame.draw.rect(janela, (255, 0, 0), pygame.Rect([barra_x2, barra_y2], [barra_largura, barra_altura]))
    pygame.draw.rect(janela, (55, 125, 34), pygame.Rect(barra_x2, barra_y2, vida_restante2, barra_altura))

    if vida_restante2 == 0:
        jogador2st = "morto"
        lutador2 = False
    else:
        jogador2st = "vivo"

    if vida_restante1 == 0:
        jogador1st = "morto"
        lutador1 = False
    else:
        jogador1st = "vivo"

    if jogador2st == "morto":
        vencedor = "Jogador 1"
        pygame.quit()
        subprocess.run(["python", "tela_final.py"])
        sys.exit()
    elif jogador1st == "morto":
        vencedor = "Jogador 2"
        pygame.quit()
        subprocess.run(["python", "tela_final2.py"])
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini = False

    pygame.display.update()  # Atualiza a tela
    pygame.display.flip()

pygame.quit()  # Finaliza o Pygame