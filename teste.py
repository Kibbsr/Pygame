import pygame

largura_tela = 1550
altura_tela = 835

class Lutador():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 150)  # Rect representa o tamanho e posição do lutador
        self.hp = 100  # HP do lutador
        self.dano_soco = 10  # Dano do soco normal
        self.dano_golpe_especial = 5  # Dano do golpe especial (tecla J)

        self.velocidade_y = 0  # Velocidade no eixo Y
        self.no_chao = True  # Indica se o lutador está no chão ou no ar
        self.gravidade = 0.3  # Intensidade da gravidade
        self.impulso = -11  # Impulso inicial do pulo

        # Flag para controlar se os golpes estão sendo usados
        self.ataque_ativo = False
        self.golpe_ativo = False

        # Áreas de golpe
        self.soco_area = pygame.Rect(0, 0, 0, 0)
        self.golpe_area = pygame.Rect(0, 0, 0, 0)

    def movimentacao(self):
        """Controla os movimentos do lutador 1 (com as teclas A, D, W)"""
        if self.rect.x > largura_tela:
            self.rect.x = largura_tela
        if self.rect.x < 0:
            self.rect.x = 0

        mov_velocidade = 3.5
        dimensao_x = 0
        dimensao_y = 0

        # Obtém o estado das teclas pressionadas (True ou False)
        mov = pygame.key.get_pressed()

        # Movimentos horizontais
        if mov[pygame.K_a]:
            dimensao_x = -mov_velocidade
        elif mov[pygame.K_d]:
            dimensao_x = mov_velocidade

        # Movimento de pulo
        if mov[pygame.K_w] and self.no_chao:
            self.velocidade_y = self.impulso
            self.no_chao = False

        # Aplica a gravidade
        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y

            if self.rect.y >= 600:  # Simulando colisão com o solo
                self.rect.y = 600
                self.no_chao = True
                self.velocidade_y = 0

        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

        # Detecta a tecla para o golpe
        if mov[pygame.K_j]:  # Golpe especial (dano 5)
            self.golpe_especial()

        elif mov[pygame.K_k]:  # Golpe normal (dano 10)
            self.soco()

    def movimentacao2(self):
        """Função para movimentação do segundo lutador usando as teclas de seta"""
        if self.rect.x > largura_tela:
            self.rect.x = largura_tela
        if self.rect.x < 0:
            self.rect.x = 0

        mov_velocidade = 3.5
        dimensao_x = 0
        dimensao_y = 0

        # Obtém o estado das teclas pressionadas (True ou False) para as setas
        mov = pygame.key.get_pressed()

        # Movimentos horizontais (setas)
        if mov[pygame.K_LEFT]:
            dimensao_x = -mov_velocidade
        elif mov[pygame.K_RIGHT]:
            dimensao_x = mov_velocidade

        # Movimento de pulo (seta para cima)
        if mov[pygame.K_UP] and self.no_chao:
            self.velocidade_y = self.impulso
            self.no_chao = False

        # Aplica a gravidade
        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y

            if self.rect.y >= 600:  # Simulando colisão com o solo
                self.rect.y = 600
                self.no_chao = True
                self.velocidade_y = 0

        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

        # Detecta a tecla para o golpe (mesmo controle de ataque)
        if mov[pygame.K_k]:  # Golpe especial (dano 5)
            self.golpe_especial()

        elif mov[pygame.K_j]:  # Golpe normal (dano 10)
            self.soco()

    def soco(self):
        """Método para realizar o soco normal (dano 10)."""
        if not self.ataque_ativo:
            # Definindo a área de alcance do soco (hitbox)
            self.soco_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, 30, 50)
            self.ataque_ativo = True
            self.golpe_ativo = False

    def golpe_especial(self):
        """Método para realizar o golpe especial (dano 5)."""
        if not self.golpe_ativo:
            # Definindo a área de alcance do golpe especial
            self.golpe_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, 40, 60)
            self.golpe_ativo = True
            self.ataque_ativo = False

    def aplicar_dano(self, dano):
        """Método para reduzir a vida (HP) do lutador."""
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0  # Impede que a vida seja negativa

    def box(self, surface):
        """Desenha a área de ataque do lutador (soco ou golpe especial)."""
        if self.ataque_ativo:
            pygame.draw.rect(surface, (255, 0, 0), self.soco_area, 2)  # Desenha a área do soco
        elif self.golpe_ativo:
            pygame.draw.rect(surface, (255, 255, 0), self.golpe_area, 2)  # Desenha a área do golpe especial

    def desenhar_barra_vida(self, surface):
        """Desenha a barra de vida fixada no topo da tela."""
        barra_largura = 100
        barra_altura = 10
        barra_x = 50 if self.rect.x < largura_tela / 2 else largura_tela - 150  # Ajusta a posição X com base no lado
        barra_y = 20  # Definindo a posição fixa no topo da tela (20 pixels abaixo da borda superior)

        # Desenhando o fundo da barra de vida (cinza)
        pygame.draw.rect(surface, (169, 169, 169), (barra_x, barra_y, barra_largura, barra_altura))

        # Calculando a vida restante
        vida_restante = (self.hp / 100) * barra_largura

        # Desenhando a barra de vida (verde)
        pygame.draw.rect(surface, (0, 255, 0), (barra_x, barra_y, vida_restante, barra_altura))


# Função para detectar colisão entre dois lutadores
def verificar_colisao(lutador1, lutador2):
    """Verifica se o soco de lutador1 ou o golpe especial colidiu com lutador2."""
    if lutador1.ataque_ativo and lutador1.soco_area.colliderect(lutador2.rect):
        lutador2.aplicar_dano(lutador1.dano_soco)  # Aplica o dano do soco normal
    elif lutador1.golpe_ativo and lutador1.golpe_area.colliderect(lutador2.rect):
        lutador2.aplicar_dano(lutador1.dano_golpe_especial)  # Aplica o dano do golpe especial




