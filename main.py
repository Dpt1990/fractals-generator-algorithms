import fractal
import pygame

def menu_principale():
  scelta = 0
  while (scelta != "2"):
    scelta = input("Digita 1 per stampare 'il frattale di Koch' o 2 per stampare 'il frattale': ")
    if scelta == "1":
        fractal.frattale_koch()
    elif scelta == "2":
        pygame.quit()
    else:
      print("Scelta non valida")

if __name__ == "__main__":
    menu_principale()