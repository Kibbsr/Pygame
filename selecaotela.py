import pygame
from teste import Lutador

pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("")


fundo_menu = pygame.image.load("ARENA.png").convert()
fundo_menu = pygame.transform.scale(fundo_menu, (largura_tela, altura_tela))

fundoarena1 = pygame.image.load("arenaluta.png").convert()
fundoarena1 = pygame.transform.scale(fundoarena1,(largura_tela,altura_tela))

fundoarena2 = pygame.image.load("arenaluta2.png").convert()
fundoarena2 = pygame.transform.scale(fundoarena2,(largura_tela,altura_tela))

def tela_menu():
    janela.blit(fundo_menu, (0, 0))
    # Adicione aqui o texto ou opções de menu
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render("Pressione ENTER para começar", True, (255, 255, 255))
    janela.blit(texto, (300, 400))

def fase1():
    janela.blit(fundoarena1, (0, 0))
    # Adicione aqui o texto ou opções de menu
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render("Floresta Encantada", True, (255, 255, 255))
    janela.blit(texto, (300, 400))
    
def fase2():
    janela.blit(fundoarena2, (0, 0))
    # Adicione aqui o texto ou opções de menu
    fonte = pygame.font.Font(None, 74)
    texto = fonte.render("Coliseu Congelado", True, (255, 255, 255))
    janela.blit(texto, (300, 400))
tela_atual = 'menu'
ini=True
while ini:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini = False
        elif tela_atual == 'menu':
            tela_menu()
            if event.type == pygame.KEYDOWN:
                if tela_atual =='menu':
                    if event.key == pygame.K_d or event.type == pygame.K_RIGHT:
                        tela_atual = 'Floresta'
                    elif event.type == pygame.K_a or event.type == pygame.K_LEFT:
                        tela_atual = 'Gelo'
    if tela_atual == 'Floresta':
        fase1()
    elif tela_atual == 'Gelo':
        fase2()

    pygame.display.update()
pygame.quit()
        


    
