import pygame
from teste import Lutador
import subprocess
import sys

estado = "Seleção Personagem"

pygame.init()
largura_tela = 1540
altura_tela = 805
janela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Seleção Personagens")

fonte = pygame.font.Font('Play-Regular.ttf', 44)
confirmar = fonte.render("Pressione ENTER para selecionar", True, (0,0,0))
janela.blit = (confirmar, (15,25))

#Importar lutadores

personagem1 = pygame.image.load('')

personagem2 = pygame.image.load('')

personagem3 = pygame.image.load('')

personagem4 = pygame.image.load('')


personagens = [personagem1, personagem2 , personagem3, personagem4]



for personagem in personagens:
    pygame.transform.scale(personagem, ( 100, 150))
    
i1 = 0
i2 = 0

confirmado1 = False
confirmado2 = False


def desenhar_personagem():
    jogador1_personagem = personagens[i1]
    janela.blit(jogador1_personagem, (1300, 600))

    jogador2_personagem = personagens[i2]
    janela.blit(jogador2_personagem, (100, 600))

    if confirmado1:
        pronto = fonte.render("Pronto!", True, (255, 255, 255))
        janela.blit(pronto, (1300, 600) )

    if confirmado2:
        pronto = fonte.render("Pronto!", True, (255, 255, 255))
        janela.blit(pronto, (100, 600) )

    pygame.display.flip()


def confirmar_escolha(numero):
    if numero == 1:
        confirmado1 = True
        print(f"jogador1 escolheu o personagem {i1+1}")

    if numero == 2:
        confirmado2 = True
        print(f"jogador2 escolheu o personagem {i2+1}")
    #continuar para a próxima fase


ini=True
while ini:
    selecionado = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ini = False
            sys.exit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                i1 = i1 - 1
            elif event.key == pygame.K_d:
                i1 = i1 + 1
            
            elif event.key == pygame.K_LEFT:
                i2 = i2 - 1
            elif event.key == pygame.K_RIGHT:
                i2 = i2 + 1


            if event.key == pygame.K_RETURN:
                confirmar_escolha(1)

            if event.key == pygame.K_KP_ENTER:
                confirmar_escolha(2)
        desenhar_personagem()
    jogador1 = personagens[i1]
    jogador2 = personagens[i2]

    if confirmado1 and confirmado2:
        subprocess.run(["python", "telaarena.py"])
        pygame.quit()
        sys.exit()


        #mandar para a tela de jogo

