import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, RED, BLUE, GREEN, YELLOW
from assets import carrega_arquivos
import math
import random

def colisao_entre_circulos(x1, y1, raio1, x2, y2, raio2):
    # Calcula a distância entre os centros das circunferências
    distancia_centros = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Verifica se a distância é menor ou igual à soma dos raios das circunferências
    if distancia_centros <= raio1 + raio2:
        return True
    else:
        return False

def verifica_colisoes(circle, lista_circles):
    for circle2 in lista_circles:
        if colisao_entre_circulos(circle['x'], circle['y'], circle['r'], circle2['x'], circle2['y'], circle2['r']) == True:
            return True
    return False

def criar_numeros(intervalo):
    lista_circles = []
    lista_cores = [RED, BLUE, YELLOW, GREEN]
    for num in range(intervalo):
        num_in_circle = num
        raio = random.randint(50, 80)
        x_circle = random.randint(raio, WIDTH - raio)
        y_circle = random.randint(raio, HEIGHT - raio)
        cor_cicle = random.choice(lista_cores)
        # cor_cicle = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        fonte = pygame.font.SysFont(None, raio)
        circle = {'x': x_circle, 'y': y_circle, 'r': raio, 'cor': cor_cicle, 'texto': fonte, 'num_circle': num_in_circle}
        if lista_circles == []:
            lista_circles.append(circle)
        else:
            while verifica_colisoes(circle,lista_circles) == True:
                raio = random.randint(50, 80)
                x_circle = random.randint(raio, WIDTH - raio)
                y_circle = random.randint(raio, HEIGHT - raio)
                circle = {'x': x_circle, 'y': y_circle, 'r': raio, 'cor': cor_cicle, 'texto': fonte, 'num_circle': num_in_circle}
            lista_circles.append(circle)

    return lista_circles



def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    counter, conta = 40, '40'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)    
    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    # guardando lista de circulos
    circles = criar_numeros(8)
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type==pygame.USEREVENT:
                counter-=1
                conta=str(counter).rjust(3) if counter>-1 else state==DONE
       
       
        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        for circulo in circles:
            pygame.draw.circle(window, circulo['cor'], (circulo['x'], circulo['y']), circulo['r'])
        pygame.display.update()  # Mostra o novo frame para o jogador
        window.blit(font.render(conta, True, (255,255,255)), (32, 48))
        pygame.display.flip()
        clock.tick(60)
        
        

    return state
   