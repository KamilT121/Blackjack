import pygame
import sys
def main(screen):
    for event in pygame.event.get():
        # przechwyć zamknięcie okna
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.locals.MOUSEBUTTONDOWN and event.button == 1:
            if 705 < event.pos[0] < 1214 and 341 < event.pos[1] < 1033:
                return 1
            elif 1394 < event.pos[0] < 1814 and 500 < event.pos[1] < 1033:
                return 2
            elif 103 < event.pos[0] < 519 and 500 < event.pos[1] < 1033:
                return 3
    return 0