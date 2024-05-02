# Klasa Card

import pygwidgets
import pygame

class Card():
    BACK_OF_CARD_IMAGE = pygame.image.load('images/BackOfCard.png')

    def __init__(self, suit, rank, value, window):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        if value == 10:
            self.cardName = f"{rank}_{suit[0]}"
        else:
            self.cardName = f"{rank}_{value}"
        fileName = f'images\\card\\{self.cardName}.png'
        self.images = pygwidgets.ImageCollection(window, (0, 0),
                        {'front': fileName,
                         'back': Card.BACK_OF_CARD_IMAGE}, 'back')
    def conceal(self):
        self.images.replace('back')

    def reveal(self):
        self.images.replace('front')

    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def setLoc(self, loc):
        self.images.setLoc(loc)
        return loc

    def getLoc(self):
        loc = self.images.getLoc()
        return loc

    def draw(self):
        self.images.draw()