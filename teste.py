# Importando o módulo Pygame, que fornece funcionalidades para criar jogos
import pygame

# Definição da classe Lutador, que representa um lutador no jogo.
class Lutador():
    # O método __init__ é o construtor da classe, inicializa as variáveis e a posição do lutador.
    def __init__(self, x, y):
        # Cria um retângulo (pygame.Rect) representando o lutador, com a posição inicial (x, y)
        # O retângulo tem tamanho fixo de 50x150 pixels
        self.rect = pygame.Rect((x, y, 50, 150))

    # Método de movimentação do lutador, utilizando as teclas A e D
    def movimentação(self):
        # Define a velocidade de movimento (3 pixels por atualização)
        mov_velocidade = 3
        # Inicializa as variáveis que irão controlar os movimentos no eixo X e Y
        dimensao_x = 0
        dimensao_y = 0

        # Obtém o estado das teclas pressionadas (True ou False)
        mov = pygame.key.get_pressed()

        # Verifica se a tecla 'A' foi pressionada (movimento para a esquerda)
        if mov[pygame.K_a]:
            dimensao_x = -mov_velocidade
        # Verifica se a tecla 'D' foi pressionada (movimento para a direita)
        elif mov[pygame.K_d]:
            dimensao_x = mov_velocidade

        # Atualiza a posição do lutador no eixo X, adicionando o valor de dimensao_x
        # No eixo Y, não há movimento, portanto, dimensao_y permanece 0
        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

    # Método de movimentação alternativo, utilizando as teclas de seta (esquerda e direita)
    def movimentação2(self):
        # Define a velocidade de movimento (3 pixels por atualização)
        mov_velocidade = 3
        # Inicializa as variáveis que irão controlar os movimentos no eixo X e Y
        dimensao_x = 0
        dimensao_y = 0

        # Obtém o estado das teclas pressionadas (True ou False)
        mov = pygame.key.get_pressed()

        # Verifica se a tecla de seta para a esquerda foi pressionada
        if mov[pygame.K_LEFT]:
            dimensao_x = mov_velocidade
        # Verifica se a tecla de seta para a direita foi pressionada
        elif mov[pygame.K_RIGHT]:
            dimensao_x = -mov_velocidade

        # Atualiza a posição do lutador no eixo X, adicionando o valor de dimensao_x
        # No eixo Y, não há movimento, portanto, dimensao_y permanece 0
        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

    # Método que desenha o lutador na tela
    def box(self, surface):
        # Desenha um retângulo azul (0, 0, 255) na superfície 'surface' usando a posição e tamanho de 'self.rect'
        pygame.draw.rect(surface, (0, 0, 255), self.rect)
