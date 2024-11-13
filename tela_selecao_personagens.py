import pygame
from teste import Lutador
import subprocess
import sys


pygame.init()
largura_tela = 1550
altura_tela = 835
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Seleção Personagens")




#Importar lutadores

personagem1 = pygame.image.load()

personagem2 = pygame.image.load()

personagem3 = pygame.image.load()

personagem4 = pygame.image.load()


personagens = [personagem1, personagem2 , personagem3, personagem4]

for personagem in personagens:
    pygame.transform.scale(personagem, ( , ))
    
i1 = 0
i2 = 0


def desenhar_personagem():
    jogador1_personagem = personagens[i1]
    janela.blit(jogador1_personagem, (x, y))

    jogador2_personagem = personagens[i2]
    janela.blit(jogador2_personagem, (x, y))
    pygame.display.flip()
ini=True
while ini:
    selecionado = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                i1 = i1 - 1
            elif event.key == pygame.K_d:
                i1 = i1 + 1
            
            elif event.key == pygame.K_LEFT:
                i2 = i2 - 1
            elif event.key == pygame.K_RIGHT:
                i2 = i2 + 1


    jogador1 = personagens[i1]
    jogador2 = personagens[i2]
    desenhar_personagem()

            

                



        
    