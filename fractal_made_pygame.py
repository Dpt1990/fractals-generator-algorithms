import pygame, sys
import math

from pygame.locals import *

# Inizializzazione di Pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, height = 800, 600
screen = pygame.display.set_mode((800, 600))
fps = 15
# Impostazioni della finestra


pygame.display.set_caption("Koch-Snowflake Effect")
clock = pygame.time.Clock()

# Colori



# Funzione per disegnare il frattale di Koch
def draw_koch_snowflake(start, end, iter):
    if iter == 0:
        pygame.draw.line(screen, BLACK, start, end)
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
        draw_koch_snowflake(start, p1, iter - 1)
        draw_koch_snowflake(p1, p3, iter - 1)
        draw_koch_snowflake(p3, p5, iter - 1)
        draw_koch_snowflake(p5, end, iter - 1)


# Funzione principale
def frattale_koch():
    running = True
    depth = 5

    while running:
        screen.fill(WHITE)

        # Definizione dei vertici del triangolo
        side_length = 400
        center_x, center_y = WIDTH // 2, height // 2
        p1 = (center_x - side_length // 2, center_y + (side_length * math.sqrt(3) / 2) // 2)
        p2 = (center_x + side_length // 2, center_y + (side_length * math.sqrt(3) / 2) // 2)
        p3 = (center_x, center_y - (side_length * math.sqrt(3) / 2) // 2)

        # Disegna il frattale di Koch su ogni lato del triangolo
        draw_koch_snowflake(p1, p2, depth)
        draw_koch_snowflake(p2, p3, depth)
        draw_koch_snowflake(p3, p1, depth)

        # Rende le modifiche effettive
        pygame.display.flip()

        # Eventi
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()

        # Limita il frame rate
        clock.tick(60)

    pygame.quit()

def frattale_hilbert():
    iter = 6
    num = int(pow(2, iter))
    t = num * num

    lineThickness = 2

    hilbert = [None for i in range(t)]

    for i in range(t):
        length = WIDTH/num
        hilbert[i] = get_point(i, length, iter, True)


    toggle_color = False

    # set timer to the t (timer = t) if you want
    # to draw the whole fractal without animation
    timer = 1
    increment_speed = 1

    run = True
    while run:
        screen.fill(WHITE)
        clock.tick(fps)
        frame_rate = int(clock.get_fps())
        pygame.display.set_caption("Hilbert Curve - FPS : {}".format(frame_rate))

        for i in range(timer-1):
          pygame.draw.line(screen, BLACK, hilbert[i], hilbert[i+1])

        pygame.display.flip()

        timer += increment_speed
        if timer > t:
            timer = t

    pygame.quit()

def get_point(index, length=1, level=1, offset=False):
  points = [
      [0, 0],
      [0, 1],
      [1, 1],
      [1, 0]
  ]
  i = index & 3
  point = points[i]

  for x in range(1, level):
      val = pow(2, x)

      index = index >> 2
      i = index & 3

      if i == 0:
          point[0], point[1] = point[1], point[0]

      elif i == 1:
          point[1] += val

      elif i == 2:
          point[0] += val
          point[1] += val

      elif i == 3:
          point[0], point[1] = val-1-point[1], val-1-point[0]
          point[0] += val

  point = [
      point[0] * length,
      point[1] * length
  ]

  if offset:
      point = [
          point[0] + length/2,
          point[1] + length/2
      ]

  return point
