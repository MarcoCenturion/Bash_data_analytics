#importar las librerías
import pygame, sys

# Definir colores con escala RGB (0 = NADA / 255 = TODO)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED   = (266,0,0)
BLUE  = (0,0,255)

# Inicializar el juego
pygame.init()

# Definir tamaño de pantalla TUPLA
size = (800,500)

# crear ventana
screen = pygame.display.set_mode(size)

# Iniciar bucle infinito del juego
while True:
    for event in pygame.event.get(): # capturamos los eventos para poder cerrar la ventana
        if event.type == pygame.QUIT():
            sys.exit()

    screen.fill(WHITE) # llena la pantalla de blanco
    pygame.display.flip() # actualiza la pantalla
