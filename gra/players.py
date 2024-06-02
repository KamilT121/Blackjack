class Players:
    def __init__(self, total_player, cards, prices=0, sum_value=0):
        #nie ustawiać listy jako elemntu domyślnego, ponieważ każda gracza będzie używał tej samej listy, i nazwa klasy wielką literą powinna byc ;p
        self.total_player = total_player
        self.prices = prices
        self.cards = cards
        self.sum_value = sum_value

    def split(self, total):
        if self.total_player >= total:
            self.prices += total
            self.total_player -= total
            return True
        else:
            return False

    def get_card(self, card, value):
        self.sum_value += value
        self.cards.append(card)

    def win(self, total):
        self.total_player += int(total)
        self.prices = 0
        self.cards = []
        self.sum_value = 0

    def get_price(self):
        return self.prices

    def get_sum_value(self):
        return self.sum_value
