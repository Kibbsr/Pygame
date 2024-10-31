import pygame

pygame.init()

lutador_img = pygame.image.load("").convert_alpha()
lutador_img = pygame.transform.scale(lutador_img, (#dimensões,))

class Lutador(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img  
        self.rect = self.image.get_rect()
        self.rect.x  = ##
        self.rect.bottom = ##
        self.speedx = 0

    def update(self):
