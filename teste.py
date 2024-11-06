import pygame

class Lutador():
    def __init__(self, x, y):
        # A posição inicial do lutador é dada pelos parâmetros (x, y)
        self.rect = pygame.Rect(x, y, 50, 150)
        self.hp = 100  # HP do lutador (vida do lutador)
        self.dano = 10  # Dano do soco

    def movimentação(self):
        # Define a velocidade de movimento (3 pixels por atualização)
        mov_velocidade = 3
        dimensao_x = 0
        dimensao_y = 0

        # Obtém o estado das teclas pressionadas (True ou False)
        mov = pygame.key.get_pressed()

        if mov[pygame.K_w]:
            dimensao_y = mov_velocidade
        elif mov[pygame.K_s]:
            dimensao_y = -mov_velocidade
        # Verifica se a tecla 'A' foi pressionada (movimento para a esquerda)
        if mov[pygame.K_a]:
            dimensao_x = -mov_velocidade
        # Verifica se a tecla 'D' foi pressionada (movimento para a direita)
        elif mov[pygame.K_d]:
            dimensao_x = mov_velocidade

        # Atualiza a posição do lutador
        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

        # Verifica se a tecla 'J' foi pressionada para dar o soco
        if mov[pygame.K_j]:
            self.soco()

    def movimentação2(self):
        mov_velocidade = 3
        dimensao_x = 0
        dimensao_y = 0
        mov = pygame.key.get_pressed()
        if mov[pygame.K_UP]:
            dimensao_y = mov_velocidade
        if mov[pygame.K_DOWN]:
            dimensao_y = -mov_velocidade
        if mov[pygame.K_LEFT]:
            dimensao_x = +mov_velocidade
        elif mov[pygame.K_RIGHT]:
            dimensao_x = -mov_velocidade

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
        pygame.draw.rect(surface, (255, 0, 0), self.soco(), 2)  # Desenha a área do soco (hitbox)

# Função para detectar colisão entre dois lutadores
def verificar_colisao(lutador1, lutador2):
    """Verifica se o soco de lutador1 atingiu lutador2."""
    if lutador1.soco().colliderect(lutador2.rect):  # Se o soco de lutador1 colidir com lutador2
        lutador2.aplicar_dano(lutador1.dano)  # Aplica o dano

