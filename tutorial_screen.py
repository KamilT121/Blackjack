import pygame
import sys
def main(screen):
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        #kod samouczka
        print("samouczek")



    return 3