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


#Importar lutadores

personagem1 = pygame.image.load('Attack_1.1_frames/frame_0.png')

personagem2 = pygame.image.load('Attack_1.1_frames/frame_1.png')

personagem3 = pygame.image.load('Attack_1.1_frames/frame_2.png')

personagem4 = pygame.image.load('Attack_1.1_frames/frame_3.png')


personagens = [personagem1, personagem2 , personagem3, personagem4]



for i in range(len(personagens)):
    personagens[i] = pygame.transform.scale(personagens[i], (100, 150))

i1 = 0
i2 = 0

confirmado1 = False
confirmado2 = False


def desenhar_personagem():
    janela.fill((0, 0, 0))
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
    global confirmado1, confirmado2
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
        # Trocar personagem jogador 1 (se não confirmado)
            if not confirmado1:
                if event.key == pygame.K_a:
                    i1 = (i1 - 1) % len(personagens)
                elif event.key == pygame.K_d:
                    i1 = (i1 + 1) % len(personagens)

            # Trocar personagem jogador 2 (se não confirmado)
            if not confirmado2:
                if event.key == pygame.K_LEFT:
                    i2 = (i2 - 1) % len(personagens)
                elif event.key == pygame.K_RIGHT:
                    i2 = (i2 + 1) % len(personagens)

            # Confirmar escolha
            if event.key == pygame.K_RETURN and not confirmado1:
                confirmar_escolha(1)

            if event.key == pygame.K_KP_ENTER and not confirmado2:
                confirmar_escolha(2)

            # Resetar confirmações com ESC
            if event.key == pygame.K_ESCAPE:
                confirmado1 = False
                confirmado2 = False
    desenhar_personagem()
    janela.blit(confirmar, (15, 25))
    pygame.display.flip()

    if confirmado1 and confirmado2:
        pygame.quit()
        subprocess.run(["python", "selecaotela.py"])
        sys.exit()


