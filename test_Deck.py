import class_Deck
import pygame

pygame.init()
screen = pygame.display.set_mode((20, 80))

d = class_Deck.Deck(screen)
d.Shuffle()

for _ in range(24):
    print(d.getCard().value)