import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, RED, BLUE, GREEN, YELLOW, COR1, COR2, COR3, COR4, COR5, COR6, COR7, COR8
from assets import carrega_arquivos
import math
import random

def telafinal_screen(window, pontuacao):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # Renderização
        window.fill(COR4)
        pygame.draw.rect(window,BLACK,(WIDTH-725,HEIGHT-350,550,75))
        font = pygame.font.SysFont('Consolas', 30)
        window.blit(font.render(f'sua pontuação foi de {pontuacao} pontos', True, (255,255,255)), (WIDTH-700,HEIGHT-325))


        
        pygame.display.update()

    return state
