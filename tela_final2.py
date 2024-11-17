import pygame  # Biblioteca para criar jogos e interfaces gráficas
from teste import Lutador  # Importa a classe Lutador do arquivo `teste.py`
import subprocess  # Para executar outros scripts Python
import sys  # Para gerenciar a saída do programa

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura_tela = 1540
altura_tela = 805

# Cria a janela principal do jogo
janela = pygame.display.set_mode((largura_tela, altura_tela))

# Define o título da janela
pygame.display.set_caption("FIM")

# Carrega e ajusta o fundo do menu
fundo_menu = pygame.image.load("ARENA.png").convert()
fundo_menu = pygame.transform.scale(fundo_menu, (largura_tela, altura_tela))

# Carrega uma imagem adicional (não está sendo usada diretamente aqui)
tela_vencedor = pygame.image.load("ARENA.png").convert()

# Função para exibir a tela final
def tela_final():
    # Desenha o fundo do menu na janela
    janela.blit(fundo_menu, (0, 0))
    
    # Configura a fonte para o texto
    fonte = pygame.font.Font("PressStart2P-Regular.ttf", 32)
    
    # Renderiza o texto na tela com as instruções para o jogador
    texto = fonte.render("Pressione ENTER para voltar à tela de seleção ", True, (0, 0, 0))
    janela.blit(texto, (15, 25))  # Exibe o texto na posição (15, 25)

    texto2 = fonte.render("ou ESC para sair!", True, (0, 0, 0))
    janela.blit(texto2, (15, 75))  # Exibe o texto na posição (15, 75)

    # Renderiza a mensagem do vencedor
    texto = fonte.render("O vencedor foi o Jogador 2!", True, (0, 0, 0))
    janela.blit(texto, (15, 250))  # Exibe o texto na posição (15, 250)

# Variável para controlar o loop principal
ini = True

# Loop principal do jogo
while ini:
    # Chama a função para desenhar a tela final
    tela_final()

    # Verifica eventos do Pygame
    for event in pygame.event.get():
        # Se o evento for fechar a janela, encerra o loop
        if event.type == pygame.QUIT:
            ini = False
        # Se uma tecla for pressionada
        elif event.type == pygame.KEYDOWN:
            # Se a tecla ENTER for pressionada
            if event.key == pygame.K_RETURN:
                # Executa o script `selecaotela.py` para voltar à seleção de personagens
                subprocess.run(["python", "selecaotela.py"])
                # Fecha a janela do Pygame
                pygame.quit()
                # Encerra o programa
                sys.exit()
            # Se a tecla ESC for pressionada
            if event.key == pygame.K_ESCAPE:
                # Fecha a janela do Pygame
                pygame.quit()
                # Encerra o programa
                sys.exit()

        # Atualiza a tela com o conteúdo desenhado
        pygame.display.update()

# Encerra o Pygame quando o loop principal termina
pygame.quit()
