import pygame
import math
import main

# Inizializzazione di Pygame
pygame.init()

# Impostazioni della finestra
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Koch-Snowflake Effect")
clock = pygame.time.Clock()

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Funzione per disegnare il frattale di Koch
def draw_koch_snowflake(start, end, depth):
    if depth == 0:
        pygame.draw.line(screen, WHITE, start, end)
    else:
        # Calcola la lunghezza del segmento
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx ** 2 + dy ** 2)

        # Calcola i punti intermedi
        p1 = (start[0] + dx / 3, start[1] + dy / 3)
        p5 = (start[0] + 2 * dx / 3, start[1] + 2 * dy / 3)
        p3 = ((start[0] + end[0]) / 2 + math.cos(math.pi / 3) * (start[1] - end[1]) / 3,
              (start[1] + end[1]) / 2 + math.cos(math.pi / 3) * (end[0] - start[0]) / 3)

        # Chiamata ricorsiva per disegnare i segmenti più piccoli
        draw_koch_snowflake(start, p1, depth - 1)
        draw_koch_snowflake(p1, p3, depth - 1)
        draw_koch_snowflake(p3, p5, depth - 1)
        draw_koch_snowflake(p5, end, depth - 1)

# Funzione principale
def frattale_koch():
    running = True
    depth = 5

    while running:
        screen.fill(BLACK)

        # Definizione dei vertici del triangolo
        side_length = 400
        center_x, center_y = width // 2, height // 2
        p1 = (center_x - side_length // 2, center_y + (side_length * math.sqrt(3) / 2) // 2)
        p2 = (center_x + side_length // 2, center_y + (side_length * math.sqrt(3) / 2) // 2)
        p3 = (center_x, center_y - (side_length * math.sqrt(3) / 2) // 2)

        # Disegna il frattale di Koch su ogni lato del triangolo
        draw_koch_snowflake(p1, p2, depth)
        draw_koch_snowflake(p2, p3, depth)
        draw_koch_snowflake(p3, p1, depth)

        # Aggiorna la finestra
        pygame.display.flip()
        

        # Eventi
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False

        # Limita il frame rate
        clock.tick(30)

    pygame.quit()


