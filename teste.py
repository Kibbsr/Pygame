import pygame

# Definições de tela
largura_tela = 1550
altura_tela = 835

class Lutador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 100, 150)
        self.hp = 700  # HP inicial do lutador
        self.dano_soco = 1  # Dano do soco
        self.dano_chute = 4  # Dano do golpe especial
        self.velocidade_y = 0  # Velocidade no eixo Y
        self.no_chao = True  # Indica se o lutador está no chão ou no ar
        self.gravidade = 0.3  # Intensidade da gravidade
        self.impulso = -11  # Impulso inicial do pulo
        self.ataque_ativo = False  # Flag para controle de ataque
        self.golpe_ativo = False  # Flag para controle de golpe especial
        self.sprite_atual = 0
        self.soco_animado = False
        self.pulo_animado = False
        self.morte_animado = False
        self.corrida_animado = False
        self.chute_animado = False


        self.image = pygame.Surface((100,150))
        self.image.fill((0,0,255))
        #Sprites
    
        self.sprites_soco = [pygame.image.load(f"Attack_1.1_frames/frame_{i}.png")for i in range(5)]
        self.sprites_pulo = [pygame.image.load(f"Jump1/frame_{i}.png")for i in range(3)]
        self.sprites_corrida = [pygame.image.load(f"Run1/frame_{i}.png")for i in range(4)]
        self.sprites_chute = [pygame.image.load(f"Attack_1.2_frames/frame_{i}.png")for i in range(4)]
        self.sprites_morte = [pygame.image.load(f"Dead1/frame_{i}.png")for i in range(4)]
        
        self.sprite_transicoes = 100
        self.sprite_i = 0
        self.sprite_t = 0
        self.sprite_delay = 50
        
    def animacao(self):
        if self.soco_animado:
            if pygame.time.get.ticks() - self.sprite_t > self.sprite_delay:
                self.sprite_t = pygame.time.get.ticks()
                self.sprite_i +=1
                if self.sprite_i >= len(self.sprites_soco):
                    self.sprite_i = 0
                    self.soco_animado = False
                self.image = self.sprites_soco[self.sprite_i]
            else:
                self.image = self.sprites_soco[self.sprite_i]
        elif self.pulo_animado:
            if pygame.time.get.ticks() - self.sprite_t > self.sprite_delay:
                self.sprite_t = pygame.time.get.ticks()
                self.sprite_i +=1
                if self.sprite_i >= len(self.sprites_pulo):
                    self.sprite_i = 0
                    self.pulo_animado = False
                self.image = self.sprites_pulo[self.sprite_i]
            else:
                self.image = self.sprites_pulo[self.sprite_i]
        elif self.morte_animado:
            if pygame.time.get.ticks() - self.sprite_t > self.sprite_delay:
                self.sprite_t = pygame.time.get.ticks()
                self.sprite_i +=1
                if self.sprite_i >= len(self.sprites_morte):
                    self.sprite_i = 0
                    self.morte_animado = False
                self.image = self.sprites_morte[self.sprite_i]
            else:
                self.image = self.sprites_morte[self.sprite_i]
        elif self.corrida_animado:
            if pygame.time.get.ticks() - self.sprite_t > self.sprite_delay:
                self.sprite_t = pygame.time.get.ticks()
                self.sprite_i +=1
                if self.sprite_i >= len(self.sprites_corrida):
                    self.sprite_i = 0
                    self.pulo_animado = False
                self.image = self.sprites_corrida[self.sprite_i]
            else:
                self.image = self.sprites_corrida[self.sprite_i]
        elif self.chute_animado:
            if pygame.time.get.ticks() - self.sprite_t > self.sprite_delay:
                self.sprite_t = pygame.time.get.ticks()
                self.sprite_i +=1
                if self.sprite_i >= len(self.sprites_chute):
                    self.sprite_i = 0
                    self.pulo_animado = False
                self.image = self.sprites_chute[self.sprite_i]
            else:
                self.image = self.sprites_chute[self.sprite_i]

    def aplicar_dano(self, dano):
        """Método para reduzir a vida (HP) do lutador."""
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0  # Impede que a vida seja negativa
            self.morte_animada = True

    def soco(self):
        """Método para realizar o soco e causar dano ao oponente, com a hitbox no sentido contrário do movimento."""
        self.soco_animado = True
        self.sprite_i = 0
        soco_largura = 30  # Largura da hitbox do soco
        soco_altura = 50  # Altura da hitbox do soco
    
        # Se o personagem está indo para a direita, a hitbox será deslocada para a esquerda
        if self.dimensao_x > 0:
            soco_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, soco_largura, soco_altura)  # Golpe para a esquerda
        # Se o personagem está indo para a esquerda, a hitbox será deslocada para a direita
        elif self.dimensao_x < 0:
            soco_area = pygame.Rect(self.rect.x - 50, self.rect.y + 40, soco_largura, soco_altura)  # Golpe para a direita
        else:
            soco_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, soco_largura, soco_altura)  # Golpe neutro (sem movimento)

        return soco_area

    def chute(self):
        """Método para realizar o soco especial e causar dano ao oponente, com a hitbox no sentido contrário do movimento."""
        self.sprite_i = 0
        soco_largura = 30  # Largura da hitbox do golpe especial
        soco_altura = 50  # Altura da hitbox do golpe especial

        # Se o personagem está indo para a direita, a hitbox será deslocada para a esquerda
        if self.dimensao_x > 0:
            soco_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, soco_largura, soco_altura)  # Golpe para a esquerda
        # Se o personagem está indo para a esquerda, a hitbox será deslocada para a direita
        elif self.dimensao_x < 0:
            soco_area = pygame.Rect(self.rect.x - 50, self.rect.y + 40, soco_largura, soco_altura)  # Golpe para a direita
        else:
            soco_area = pygame.Rect(self.rect.x + 50, self.rect.y + 40, soco_largura, soco_altura)  # Golpe neutro (sem movimento)

        return soco_area

    def movimentacao(self):
        """Controla os movimentos do Lutador 1 (com as teclas A, D, W)"""


        mov_velocidade = 3.5
        dimensao_x = 0
        dimensao_y = 0

        mov = pygame.key.get_pressed()

        # Movimentos horizontais
        if mov[pygame.K_a]:  # Movimento para a esquerda
            dimensao_x = -mov_velocidade
            self.corrida_animado = True
        elif mov[pygame.K_d]:  # Movimento para a direita
            dimensao_x = mov_velocidade
            self.corrida_animado = True
        else:
            self.corrida_animado = False
        # Movimento de pulo
        if mov[pygame.K_w] and self.no_chao:
            self.velocidade_y = self.impulso
            self.no_chao = False
            self. pulo_animado = True

        # Aplica a gravidade
        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y

            if self.rect.y >= 600:  # Simulando colisão com o solo
                self.rect.y = 600
                self.no_chao = True
                self.velocidade_y = 0
                self.pulo_animado = False

        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

        self.dimensao_x = dimensao_x  # Atualiza a direção de movimento

        if mov[pygame.K_k] and not self.golpe_ativo:
            self.golpe_ativo = True
            self.chute()

        elif mov[pygame.K_j] and not self.ataque_ativo:
            self.ataque_ativo = True
            self.soco()
        else:
            self.ataque_ativo = False
            self.golpe_ativo = False


    def movimentacao2(self):
        """Controla os movimentos do Lutador 2 (com as teclas de seta)"""
        if self.rect.x > largura_tela:
            self.rect.x = largura_tela
        if self.rect.x < 0:
            self.rect.x = 0

        mov_velocidade = 3.5
        dimensao_x = 0
        dimensao_y = 0

        mov = pygame.key.get_pressed()

        # Movimentos horizontais (setas)
        if mov[pygame.K_LEFT]:  # Movimento para a esquerda
            dimensao_x = -mov_velocidade
            self.corrida_animado = True
        elif mov[pygame.K_RIGHT]:  # Movimento para a direita
            dimensao_x = mov_velocidade
            self.corrida_animado = True
        else:
            self.corrida_animado = False

        # Movimento de pulo (seta para cima)
        if mov[pygame.K_UP] and self.no_chao:
            self.velocidade_y = self.impulso
            self.no_chao = False
            self.pulo_animado = True

        # Aplica a gravidade
        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y

            if self.rect.y >= 600:  # Simulando colisão com o solo
                self.rect.y = 600
                self.no_chao = True
                self.velocidade_y = 0
                self.pulo_animado = False

        self.rect.x += dimensao_x
        self.rect.y += dimensao_y

        self.dimensao_x = dimensao_x  # Atualiza a direção de movimento do lutador 2

        # Golpe especial com '2'
        if mov[pygame.K_m] and not self.golpe_ativo:
            self.golpe_ativo = True
            self.chute()

        # Golpe normal com '1'
        elif mov[pygame.K_n] and not self.ataque_ativo:
            self.ataque_ativo = True
            self.soco()

        else:
            self.ataque_ativo = False
            self.golpe_ativo = False


    def box(self, surface):
        """Desenha o lutador na tela."""
        #colocar self.image
        surface.blit(self.image, self.rect)  # Desenha o lutador
        if self.soco_animado:
            pygame.draw.rect(surface, (255, 0, 0), self.soco(), 2)  # Desenha a área do soco (hitbox)



    def atualizar_animacao(self):
        self.animacao()
