import pygame
largura_tela = 1550
class Lutador():
    def __init__(self, x, y):
        # A posição inicials do lutador é dada pelos parâmetros (x, y)
        self.rect = pygame.Rect(x, y, 50, 150)
        self.hp = 100  # HP do lutador (vida do lutador)
        self.dano = 10  # Dano do soco

        self.ataque = False

        self.velocidade_y = 0  # Velocidade no eixo Y
        self.no_chao = True  # Indica se o lutador está no chão ou no ar 
        self.gravidade = 0.3  # Intensidade da gravidade
        self.impulso = -11  # Impulso inicial do pulo


    def movimentação(self):
        if self.rect.x > largura_tela:
            self.rect.x = largura_tela
        if self.rect.x < 0:
            self.rect.x = 0

        # Define a velocidade de movimento (3 pixels por atualização)
        mov_velocidade = 6.0
        dimensao_x = 0
        dimensao_y = 0


        # Obtém o estado das teclas pressionadas (True ou False)
        mov = pygame.key.get_pressed()
        
        if mov[pygame.K_w] and self.no_chao:
            self.velocidade_y = self.impulso
            self.no_chao = False
        # Verifica se a tecla 'A' foi pressionada (movimento para a esquerda)
        if mov[pygame.K_a]:
            dimensao_x = -mov_velocidade
        # Verifica se a tecla 'D' foi pressionada (movimento para a direita)
        elif mov[pygame.K_d]:
            dimensao_x = mov_velocidade
        
        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y
        
        if self.rect.y >= 600:  # Supondo que a altura do chão é y = 600
                self.rect.y = 600  # Coloca o lutador no chão
                self.no_chao = True
                self.velocidade_y = 0  # Zera a velocidade vertical

        # Atualiza a posição do lutador
        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

        # Verifica se a tecla 'J' foi pressionada para dar o soco
        if mov[pygame.K_j]:
            self.soco()
        
    


    def movimentação2(self):
        if self.rect.x > largura_tela:
            self.rect.x = largura_tela
        if self.rect.x < 0:
            self.rect.x = 0

        mov_velocidade = 3
        dimensao_x = 0
        dimensao_y = 0
        mov = pygame.key.get_pressed()
        if mov[pygame.K_LEFT]:
            dimensao_x = -mov_velocidade
        elif mov[pygame.K_RIGHT]:
            dimensao_x = +mov_velocidade
        if mov[pygame.K_UP] and self.no_chao:
            self.velocidade_y = self.impulso
            self.no_chao = False

        # Aplica a gravidade
        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y

            # Verifica se o lutador atingiu o chão (simulando colisão com o solo)
            if self.rect.y >= 600:  # Supondo que a altura do chão é y = 600
                self.rect.y = 600  # Coloca o lutador no chão
                self.no_chao = True
                self.velocidade_y = 0  # Zera a velocidade vertical


        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

    


    def soco(self):
        """Método para realizar o soco e causar dano ao oponente."""
        # Definindo a área de alcance do soco (hitbox)
        # O soco atinge 50 pixels à frente do lutador no eixo X
        

        soco_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, 30, 50)  # Soco à frente do lutador
        
        return soco_area

    def aplicar_dano(self, dano):
        """Método para reduzir a vida (HP) do lutador."""
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0  # Impede que a vida seja negativa

    def box(self, surface):
        """Desenha o lutador na tela."""
        pygame.draw.rect(surface, (0, 0, 255), self.rect)  # Desenha o lutador
        

    def desenhar_barra_vida(self, surface):
        """Desenha a barra de vida do lutador na tela."""
        # Definindo as dimensões da barra de vida
        barra_largura = 100
        barra_altura = 10
        barra_x = self.rect.x  # A barra de vida será desenhada no topo do lutador
        barra_y = self.rect.y - 20

        # Desenhando o fundo da barra de vida (cinza)
        pygame.draw.rect(surface, (169, 169, 169), (barra_x, barra_y, barra_largura, barra_altura))

        # Calculando o comprimento da barra de vida de acordo com a vida restante
        vida_restante = (self.hp / 100) * barra_largura  # Vida proporcional à largura da barra

        # Desenhando a barra de vida (verde)
        pygame.draw.rect(surface, (0, 255, 0), (barra_x, barra_y, vida_restante, barra_altura))

# Função para detectar colisão entre dois lutadores
def verificar_colisao(lutador1, lutador2):
    """Verifica se o soco de lutador1 atingiu lutador2."""
    if lutador1.soco().colliderect(lutador2.rect):  # Se o soco de lutador1 colidir com lutador2
        lutador2.aplicar_dano(lutador1.dano)  # Aplica o dano
