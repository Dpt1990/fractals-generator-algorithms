import pygame, sys
import fractal_made_pygame
import fractal_made_turtle

"""
Setting up an environment to initialize pygame
"""
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Frattali')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, 600), 0, 32)

# setting font settings
font = pygame.font.SysFont(None, 24)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# A variable to check for the status later



# Main container function that holds the buttons and game functions
def main_menu():
    click = False
    while True:

        screen.fill((WHITE))
        draw_text('Menù', font, BLACK, screen, 380, 40)

        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(300, 100, 200, 50)
        button_2 = pygame.Rect(300, 170, 200, 50)
        button_3 = pygame.Rect(300, 240, 200, 50)
        button_4 = pygame.Rect(300, 330, 200, 50)


        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                fractal_made_pygame.frattale_koch()
        if button_2.collidepoint((mx, my)):
            if click:
                title = "Tiles"
                axiom = "F+F+F+F"
                rules = {"F": "FF+F-F+F+FF"}
                iterations = 3  # TOP: 4
                angle = 90
                fractal_made_turtle.disegna(iterations, axiom, rules, angle, aspect_ratio=1, width=WIDTH, flip_v=True)
        if button_3.collidepoint((mx, my)):
            if click:
                axiom = "F"
                rules = {"F": "+F--F+F--F"}
                iterations = 4  # TOP: 16
                angle = 45
                fractal_made_turtle.disegna(iterations, axiom, rules, angle, aspect_ratio=1, width=WIDTH, flip_v=True)
        if button_4.collidepoint((mx, my)):
            if click:
                fractal_made_pygame.frattale_hilbert()

        pygame.draw.rect(screen, (156, 156, 156), button_1)
        pygame.draw.rect(screen, (156, 156, 156), button_2)
        pygame.draw.rect(screen, (156, 156, 156), button_3)
        pygame.draw.rect(screen, (156, 156, 156), button_4)

        # writing text on top of button
        draw_text('Frattale di Koch', font, (BLACK), screen, 315, 115)
        draw_text('Turtle', font, (BLACK), screen, 350, 185)
        draw_text('Levy-C-Curve Chiuso', font, (BLACK), screen, 315, 255)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)



if __name__ == "__main__":
    main_menu()