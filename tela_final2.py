import pygame
from teste import Lutador
import subprocess
import sys

pygame.init()
largura_tela = 1540
altura_tela = 805
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("FIM")


fundo_menu = pygame.image.load("ARENA.png").convert()
fundo_menu = pygame.transform.scale(fundo_menu, (largura_tela, altura_tela))
tela_vencedor = pygame.image.load("ARENA.png").convert()


def tela_final():
    janela.blit(fundo_menu, (0, 0))
    
    # Adicione aqui o texto ou opções de menu
    fonte = pygame.font.Font("PressStart2P-Regular.ttf", 32)
    texto = fonte.render("Pressione ENTER para voltar à tela de seleção ", True, (0, 0, 0))
    janela.blit(texto, (15,25))
    texto2 = fonte.render("ou ESC para sair!", True, (0, 0, 0))
    janela.blit(texto2, (15,75))
    
    texto = fonte.render("O vencedor foi o Jogador 2!", True, (0, 0, 0))
    janela.blit(texto, (15,250))

ini=True
while ini:
    tela_final()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                subprocess.run(["python", "selecaotela.py"])
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                                                   
        pygame.display.update()
pygame.quit()
        


    
