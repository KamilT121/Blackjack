import random
class Deck():
    color=("karo", "pik", "karo", "trefl")
    BLACKJACKDictionary= {"as1":1, "dwójka":2, "trójka":3, "czwórka":4, "piątka":5, "szóstka":6, "siódemka":7, "ósemka":8, "dziewiątka":9, "walet":10, "dama":10, "król":10, "as2":11}

    def __init__(self, window, ValueDictionary=BLACKJACKDictionary):
        self.startDeck=[]
        self.playingDeck=[]
        for color in Deck.color:
            for figure, value in ValueDictionary.items():
                Karta=Card(figure, color, value, window)
                self.startDeck.append(Karta)

    def Shuffle(self):
        self.playingDeck=self.startDeck.copy()
        for card in self.playingDeck:
            card.conceal()
        random.shuffle(self.playingDeck)

    def getCard(self):
        if len(self.playingDeck)==0:
            raise IndexError('Nie ma już kart w tali')
        card=self.playingDeck.pop()
        return card

    def returnCard(self, card):
        self.playingDeck.insert(0, card)













