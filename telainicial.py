import pygame
import subprocess
import sys
def inicializa():
    pygame.init()
    largura_tela = 1550
    altura_tela = 835
    janela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("")
    fundo = pygame.image.load("ARENA.png")
    fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
    titulo_img = pygame.image.load("titulo.png")
    titulo_img = pygame.transform.scale(titulo_img, (450, 350)) #coordenadas da imagem do titulo
    pygame.font.init()
    fonte_subtitulo = pygame.font.Font(None, 45) #tamanho e fonte da letra  
    texto = fonte_subtitulo.render('START', True, (1, 255, 250)) # mensagem e definiçao da cor 
    titulo_pos = (1550 // 2 - 450 // 2, 100)  
    
    pygame.mixer.music.load("721292__victor_natas__are-you-game.ogg")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)


    estado = {
        'fundo': fundo,
        'fonte_subtitulo': fonte_subtitulo,
        'tela_atual': 0,
        'texto': texto,
        'titulo_pos': titulo_pos,
        'titulo_img': titulo_img
    }
    return estado, janela

def atualiza_estado(estado):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
    pygame.display.update()
    return True 

def desenha(janela, estado):
    if estado['tela_atual'] == 0:
        janela.blit(estado['fundo'], (0,0))
        janela.blit(estado['texto'], (735, 490)) #coordenadas do texto
        janela.blit(estado['titulo_img'],estado['titulo_pos'])


estado, janela = inicializa()
game = True
while game:
    desenha(janela, estado)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                subprocess.run(["python", "selecaotela.py"])
            
    game = atualiza_estado(estado)
pygame.quit