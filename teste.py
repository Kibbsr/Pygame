import pygame
import time  # Para controlar o cooldown
largura_tela = 1550
altura_tela=835
class Lutador:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 150)
        self.hp = 100  # HP inicial do lutador
        self.dano_soco = 0.2  # Dano do soco
        self.dano_golpe_especial = 0.10  # Dano do golpe especial
        self.velocidade_y = 0  # Velocidade no eixo Y
        self.no_chao = True  # Indica se o lutador está no chão ou no ar
        self.gravidade = 0.3  # Intensidade da gravidade
        self.impulso = -11  # Impulso inicial do pulo
        self.ataque_ativo = False  # Flag para controle de ataque
        self.golpe_ativo = False  # Flag para controle de golpe especial

        # Variáveis de cooldown
        self.ultimo_golpe_especial = 0  # Armazena o último tempo em que o golpe especial foi usado
        self.cooldown_golpe_especial = 3  # Tempo de cooldown (3 segundos)
    
    def aplicar_dano(self, dano):
        """Método para reduzir a vida (HP) do lutador."""
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0  # Impede que a vida seja negativa

    def soco(self):
        """Método para realizar o soco e causar dano ao oponente."""
        soco_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, 30, 50)  # Soco à frente do lutador
        return soco_area

    def socoespecial(self):
        """Método para realizar o soco especial e causar dano ao oponente."""
        socoespecial_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, 30, 50)  # Golpe especial à frente do lutador
        return socoespecial_area

    def movimentacao(self):
        """Controla os movimentos do lutador 1 (com as teclas A, D, W)"""
        if self.rect.x > largura_tela:
            self.rect.x = largura_tela
        if self.rect.x < 0:
            self.rect.x = 0

        mov_velocidade = 3.5
        dimensao_x = 0
        dimensao_y = 0

        mov = pygame.key.get_pressed()

        if mov[pygame.K_a]:
            dimensao_x = -mov_velocidade
        elif mov[pygame.K_d]:
            dimensao_x = mov_velocidade

        if mov[pygame.K_w] and self.no_chao:
            self.velocidade_y = self.impulso
            self.no_chao = False

        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y
            if self.rect.y >= 600:  # Simulando colisão com o solo
                self.rect.y = 600
                self.no_chao = True
                self.velocidade_y = 0

        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

        # Golpe especial com 'J', com cooldown de 3 segundos
        if mov[pygame.K_j] and not self.golpe_ativo and (time.time() - self.ultimo_golpe_especial >= self.cooldown_golpe_especial):
            self.golpe_ativo = True
            self.ultimo_golpe_especial = time.time()  # Atualiza o tempo do último golpe especial
            self.socoespecial()

        # Golpe normal com 'K'
        elif mov[pygame.K_k] and not self.ataque_ativo:
            self.ataque_ativo = True
            self.soco()

        else:
            self.ataque_ativo = False
            self.golpe_ativo = False


    def movimentacao2(self):
        """Função para movimentação do segundo lutador usando as teclas de seta"""
        if self.rect.x > largura_tela:
            self.rect.x = largura_tela
        if self.rect.x < 0:
            self.rect.x = 0

        mov_velocidade = 3.5
        dimensao_x = 0
        dimensao_y = 0

        mov = pygame.key.get_pressed()

        if mov[pygame.K_LEFT]:
            dimensao_x = -mov_velocidade
        elif mov[pygame.K_RIGHT]:
            dimensao_x = mov_velocidade

        if mov[pygame.K_UP] and self.no_chao:
            self.velocidade_y = self.impulso
            self.no_chao = False

        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y
            if self.rect.y >= 600:  # Simulando colisão com o solo
                self.rect.y = 600
                self.no_chao = True
                self.velocidade_y = 0

        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

    # Golpe especial com '1', com cooldown de 3 segundos
        if mov[pygame.K_1] and not self.golpe_ativo and (time.time() - self.ultimo_golpe_especial >= self.cooldown_golpe_especial):
            self.golpe_ativo = True
            self.ultimo_golpe_especial = time.time()  # Atualiza o tempo do último golpe especial
            self.socoespecial()

    # Golpe normal com '2'
        elif mov[pygame.K_2] and not self.ataque_ativo:
            self.ataque_ativo = True
            self.soco()

        else:
            self.ataque_ativo = False
            self.golpe_ativo = False


    def box(self, surface):
        """Desenha o lutador na tela."""
        pygame.draw.rect(surface, (0, 0, 255), self.rect)  # Desenha o lutador
        pygame.draw.rect(surface, (255, 0, 0), self.soco(), 2)  # Desenha a área do soco (hitbox)

    def desenhar_barra_vida(self, surface):
        """Desenha a barra de vida fixada no topo da tela."""
        barra_largura = 100
        barra_altura = 10
        barra_x = 50 
        if self.rect.x < largura_tela / 2:
            pass
        else: 
            largura_tela - 150  # Ajusta a posição X com base no lado
        barra_y = 20  # Definindo a posição fixa no topo da tela (20 pixels abaixo da borda superior)

        # Desenhando o fundo da barra de vida (cinza)
        pygame.draw.rect(surface, (169, 169, 169), (barra_x, barra_y, barra_largura, barra_altura))

        # Calculando a vida restante
        vida_restante = (self.hp / 100) * barra_largura

        # Desenhando a barra de vida (verde)
        pygame.draw.rect(surface, (0, 255, 0), (barra_x, barra_y, vida_restante, barra_altura))



