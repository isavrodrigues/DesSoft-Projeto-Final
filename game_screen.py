import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
import math

def colisao_entre_circulos(x1, y1, raio1, x2, y2, raio2):
    # Calcula a distância entre os centros das circunferências
    distancia_centros = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Verifica se a distância é menor ou igual à soma dos raios das circunferências
    if distancia_centros <= raio1 + raio2:
        return True
    else:
        return False
    
    
    

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        pygame.draw.circle(window, (255,0,0), (WIDTH//2, HEIGHT//2), 50)
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state
