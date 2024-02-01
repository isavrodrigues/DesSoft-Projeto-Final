import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, RED, BLUE, GREEN, YELLOW, COR1, COR2, COR3, COR4, COR5, COR6, COR7, COR8
from assets import carrega_arquivos
import math
import random
def salvar_pontuacao(pontuacao):
    arquivo = open('ranking.txt', 'a')
    arquivo.write(f"{pontuacao}\n")
    arquivo.close()

def obter_ranking():
    try:
        arquivo = open('ranking.txt', 'r')
    except FileNotFoundError:
        return []

    pontuacoes = arquivo.readlines()
    arquivo.close()
    
    pontuacoes = [int(p.strip()) for p in pontuacoes]
    pontuacoes.sort(reverse=True)
    return pontuacoes[:10] 
def telafinal_screen(window, pontuacao):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    salvar_pontuacao(pontuacao)  # Salva a pontuação atual
    ranking = obter_ranking()    # Obtém o ranking atualizado

    DONE = 0
    PLAYING = 1
    state = PLAYING

    while state != DONE:
        clock.tick(FPS)
        #Trata eventos
        for event in pygame.event.get():
            #Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
        # Renderização
        window.fill(BLACK)  # Cor de fundo e caixa de pontuação

        
        pygame.draw.rect(window, BLACK, (WIDTH-725, HEIGHT-550, 550, 75))
        font = pygame.font.SysFont('Consolas', 30)

        
        window.blit(font.render(f'Sua pontuação foi de {pontuacao} pontos', True, COR4), (WIDTH-700, HEIGHT-525))

       
        y = HEIGHT - 400
        for posicao, score in enumerate(ranking):
            window.blit(font.render(f"{posicao + 1}. {score} pontos", True, COR4), (WIDTH-700, y))
            y += 30 

        pygame.display.update()

    return state

