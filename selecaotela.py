import pygame
from teste import Lutador
import subprocess
import sys

pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("")


fundo_menu = pygame.image.load("ARENA.png").convert()
fundo_menu = pygame.transform.scale(fundo_menu, (largura_tela, altura_tela))

fundoarena1 = pygame.image.load("arenaluta1.png").convert()
fundoarena1 = pygame.transform.scale(fundoarena1,(largura_tela,altura_tela))

fundoarena2 = pygame.image.load("arenaluta2.png").convert()
fundoarena2 = pygame.transform.scale(fundoarena2,(largura_tela,altura_tela))

fundoarena3 = pygame.image.load("arenaluta3.png").convert()
fundoarena3 = pygame.transform.scale(fundoarena3,(largura_tela,altura_tela))

miniatura_fase1 = pygame.transform.scale(fundoarena1, (400, 225))  
miniatura_fase2 = pygame.transform.scale(fundoarena2, (400, 225))

def tela_menu():
    janela.blit(fundo_menu, (0, 0))
    
    # Adicione aqui o texto ou opções de menu
    fonte = pygame.font.Font("PressStart2P-Regular.ttf", 44)
    texto = fonte.render("Pressione A ou D para ver as fases", True, (255, 255, 255))
    janela.blit(texto, (15, 500))
    texto = fonte.render("e ENTER para selecionar!", True, (255, 255, 255))
    janela.blit(texto, (15, 550))
    
    janela.blit(miniatura_fase2, (200, 200)) 
    janela.blit(miniatura_fase1, (950, 200)) 

def fase1():
    janela.blit(fundoarena1, (0, 0))
    # Adicione aqui o texto ou opções de menu
    fonte = pygame.font.Font('PressStart2P-Regular.ttf', 44)
    texto = fonte.render("Floresta Encantada", True, (150, 255, 150))
    janela.blit(texto, (15,10))
    texto = fonte.render("ESC para voltar", True, (255, 255, 255))
    janela.blit(texto, (500, 700))
    
def fase2():
    janela.blit(fundoarena2, (0, 0))
    fonte = pygame.font.Font('PressStart2P-Regular.ttf', 44)
    texto = fonte.render("Coliseu Congelado", True, (200, 200, 255))
    janela.blit(texto, (0, 0))
    texto = fonte.render("ESC para voltar", True, (255, 255, 255))
    janela.blit(texto, (500, 700))

def fase3():
    janela.blit(fundoarena3,(0,0))
    fonte = pygame.font.Font('PressStart2P-Regular.ttf', 44)
    texto = fonte.render("Praia Empoerada", True, (0, 200, 200))
    janela.blit(texto, (0, 0))
    texto = fonte.render("ESC para voltar", True, (255, 255, 255))
    janela.blit(texto, (500, 700))


tela_atual = 'menu'
ini=True
while ini:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini = False
        elif event.type == pygame.KEYDOWN:
            if tela_atual =='menu':
                if event.key == pygame.K_d:
                    tela_atual = 'Floresta'
                elif event.key == pygame.K_a:
                    tela_atual = 'Gelo'
                elif event.key == pygame.K_w:
                    tela_atual = 'Praia'
            elif event.key == pygame.K_ESCAPE:
                tela_atual = 'menu'
                    
        if tela_atual == 'menu':
            tela_menu()
        elif tela_atual == 'Gelo':
            fase2()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    subprocess.run(["python", "telaarena2.py"])
                    pygame.quit()
                    sys.exit()
                    
        elif tela_atual == 'Floresta':
            fase1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    subprocess.run(["python", "telaarena.py"])
                    pygame.quit()
                    sys.exit()
        elif tela_atual == 'Praia':
            fase3()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    subprocess.run(["python", "telaarena3.py"])
                    pygame.quit()
                    sys.exit()
                    
                   
                    
        pygame.display.update()
pygame.quit()
        


    
