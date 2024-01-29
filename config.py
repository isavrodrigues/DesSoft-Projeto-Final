from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
WIDTH = 900 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

COR1 = (249, 231, 159)
COR2 = (222, 49, 99)
COR3 = (64, 224, 208)
COR4= (204, 204, 255)
COR5 = (64, 224, 208)
COR6 = (204, 204, 255)
COR7 = (249, 231, 159)
COR8 = (222, 49, 99)


# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
