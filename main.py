import class_Deck
import total_f
import random
import players

import pygame


global sum_total
def get_deck(n=0):
    tab_deck = []
    for i in range(n):
        p = class_Deck.Deck("Tutaj ma być window")
        p.Shuffle()
        tab_deck.append(p)

    return tab_deck

def get_card(tab, n):
    while True:
        y = random.randint(0, n-1)
        card = class_Deck.Deck.getCard(tab[y])
        if not card:
            del tab[y]
            n -= 1
        else:
            break

    return card

def get_players(i, p, p_total):
    tab_players = []
    for n in range(i):
        tab_players.append(players.players(p_total, p))

    return

def split(tab_players, number_player, total):
    tab_players[number_player].split(total)

def player_pass(tab_players, number_player):
    tab_players[number_player].win(-(tab_players[number_player].get_price()))
    del tab_players[number_player]


def win(tab_win):
    for i in tab_win:
        i.win(sum_total/len(tab_win))


if __name__ == "__main__":
    n = 1 #Ilość talii
    p = 1000 #Wkład do pierwszej rundy
    p_total = 3000 #Całość pieniędzy
    i = 2 #Ilość osób
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))


    tab_deck = get_deck(n)
    tab_players = get_players(i)

    print(get_card(tab, n).getName())