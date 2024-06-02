import random
import class_Card
class Deck:
    color=("karo", "pik", "karo", "trefl")
    BLACKJACKDictionary= {"as1":1, "dwójka":2, "trójka":3, "czwórka":4, "piątka":5, "szóstka":6, "siódemka":7, "ósemka":8, "dziewiątka":9, "walet":10, "dama":10, "król":10}

    def __init__(self, window, ValueDictionary=BLACKJACKDictionary):
        self.startDeck=[]
        self.playingDeck=[]
        for color in Deck.color:
            for figure, value in ValueDictionary.items():
                self.startDeck.append(class_Card.Card(figure, color, value, window))

    def Shuffle(self):
        self.playingDeck=self.startDeck.copy()
        #for card in self.playingDeck:
        #    card.conceal()
        random.shuffle(self.playingDeck)

    def getCard(self):
        if len(self.playingDeck) == 0:
            return False
        card = self.playingDeck.pop()
        return card

    def returnCard(self, card):
        self.playingDeck.insert(0, card)













