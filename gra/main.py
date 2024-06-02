import time
import class_Deck
import random
import players
import f_bot
import os

global sum_total


def logo():
    print(r"""  .------..------..------..------..------..------..------..------..------.
  |B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
  | :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
  | ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
  | '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
  `------'`------'`------'`------'`------'`------'`------'`------'`------'""")


def get_deck(n=0):
    tab_deck = []
    for i in range(n):
        p = class_Deck.Deck("screen")
        p.Shuffle()
        tab_deck.append(p)

    return tab_deck


def get_card(tab, n):
    while True:
        y = random.randint(0, n - 1)
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
        tab_players.append(players.Players(p_total, [], p))

    return tab_players


def split_f(tab_players, number_player, total):
    return tab_players[number_player].split(total)


def player_pass(tab_players, number_player):
    tab_players[number_player].win(-sum_total)


def win(tab_win):
    for i in tab_win:
        i.win(sum_total*2)


if __name__ == "__main__":
    try:
        #pygame.init()
        #screen = pygame.display.set_mode((1920, 1080))
        #screen = pygame.display.set_mode((20, 80))

        #tab_players[0] - krupier
        #tab_players[1] - bot
        #tab_players[2] - gracz

        #menu = pygame.image.load("images\\Menu_koncept.png")
        #screen.blit(menu,(0,0))

        logo()

        totalp = int(input("\n\nIlość pieniędzy jaka masz przy stole: "))
        totalw = int(input("Za ile wchodzisz do gry: "))

        if totalw > totalp:
            totalw = totalp

        tab_deck = get_deck(3)
        tab_players = get_players(3, totalw, totalp-totalw)

        sum_total = totalw

        os.system('cls')
        logo()

        print("\n W grze znajduje się: Krupier, 1 gracz i TY")
        input("\n Nacisniej dowolny przycisk jesli jestes gotowy")

        while True:
            n = 0
            bot_pass = 0

            while True:
                n += 1
                os.system('cls')
                logo()
                if tab_players[2].sum_value > 21:
                    print(f"\033[31mPrzegrałeś\033[0m")
                    break

                if tab_players[1].sum_value > 21:
                    bot_pass = 1

                if tab_players[0].sum_value > 21:
                        if tab_players[-1].sum_value <= 21:
                            print(f"\033[32mWygrałeś {sum_total*2}\033[0m")
                            win([tab_players[2]])
                        else:
                            print(f"\033[31mPrzegrałeś\033[0m")
                        break

                if n == 4:
                    if tab_players[-1].sum_value >= tab_players[0].sum_value:
                        print(f"\033[32mWygrałeś {sum_total*2}\033[0m")
                        win([tab_players[2]])
                    else:
                        print(f"\033[31mPrzegrałeś\033[0m")
                    break

                print(f"\nTwoja aktualna wartość dostepnych pieniedzy: \033[32m{tab_players[2].total_player}\033[0m\n\n")
                print(f"\nAktualna suma wartości kart Krupiera: \033[34m{tab_players[0].sum_value}\033[0m")
                print(f"Aktualna suma wartości kart Gracza 1: \033[34m{tab_players[1].sum_value}\033[0m i pieniędzy na stole: \033[34m{tab_players[1].get_price()}\033[0m")
                print(f"Aktualna Twoja suma wartości kart:    \033[34m{tab_players[2].sum_value}\033[0m i pieniędzy na stole: \033[34m{tab_players[2].get_price()}\033[0m")

                print("\n\nKrupier:")
                time.sleep(2)
                #Krupier:
                c = get_card(tab_deck, 3)
                tab_players[0].get_card(c, c.getValue())
                print(f"\n     Krupier wyciąga: {c.getSuit()} {c.getRank()}")
                time.sleep(2)

                os.system('cls')
                logo()
                print(f"\nTwoja aktualna wartość dostepnych pieniedzy: \033[32m{tab_players[2].total_player}\033[0m\n\n")
                print(f"\nAktualna suma wartości kart Krupiera: \033[34m{tab_players[0].sum_value}\033[0m")
                print(f"Aktualna suma wartości kart Gracza 1: \033[34m{tab_players[1].sum_value}\033[0m i pieniędzy na stole: \033[34m{tab_players[1].get_price()}\033[0m")
                print(f"Aktualna Twoja suma wartości kart:    \033[34m{tab_players[2].sum_value}\033[0m i pieniędzy na stole: \033[34m{tab_players[2].get_price()}\033[0m")

                if bot_pass == 0:
                    print("\n\nGracz 1:")
                    time.sleep(2)
                    #Bot:
                    if len(tab_players) == 3:
                        info = f_bot.strategis(tab_players[1].sum_value, c.getValue())
                        if info == 1:
                            c = get_card(tab_deck, 3)
                            tab_players[1].get_card(c, c.getValue())
                            print(f"\n     Gracz 1 wyciąga: {c.getSuit()} {c.getRank()}")
                        elif info == 2:
                            bot_pass = 1
                            print(f"\n     Gracz 1 pasuje")
                        else:
                            split_f(tab_players, 1, totalw)
                            print(f"\n     Gracz 1 podpija stawkę o: {totalw}")

                    time.sleep(2)

                os.system('cls')
                logo()

                print(f"\nTwoja aktualna wartość dostepnych pieniedzy: \033[32m{tab_players[2].total_player}\033[0m\n\n")
                print(f"\nAktualna suma wartości kart Krupiera: \033[34m{tab_players[0].sum_value}\033[0m")
                print(f"Aktualna suma wartości kart Gracza 1: \033[34m{tab_players[1].sum_value}\033[0m i pieniędzy na stole: \033[34m{tab_players[1].get_price()}\033[0m")
                print(f"Aktualna Twoja suma wartości kart:    \033[34m{tab_players[2].sum_value}\033[0m i pieniędzy na stole: \033[34m{tab_players[2].get_price()}\033[0m")

                print("\n\nTy:")
                time.sleep(2)
                if n == 3:
                    splitt = int(input(f"\nCzy chcesz podpić stawke o {totalw}, TAK - (1), NIE - (0): "))

                    #Gracz:
                    if splitt:
                        if split_f(tab_players, 2, 100):
                            print(f"\n     Podbijasz stawkę o: {totalw}")
                            sum_total += totalw
                        else:
                            print(f"\n     Nie masz pieniedzy")
                    else:
                        passs = int(input(f"\nCzy chcesz dobrac karte, TAK - (1), NIE - (0): "))
                        if passs:
                            c = get_card(tab_deck, 3)
                            tab_players[2].get_card(c, c.getValue())
                            print(f"\n     Wyciągasz: {c.getSuit()} {c.getRank()}")
                else:
                    c = get_card(tab_deck, 3)
                    tab_players[2].get_card(c, c.getValue())
                    print(f"\n     Wyciągasz: {c.getSuit()} {c.getRank()}")

                time.sleep(2)

            time.sleep(4)

            print(f"\nTwoja aktualna wartość dostepnych pieniedzy: \033[32m{tab_players[2].total_player}\033[0m\n\n")
            if not int(input("\n\nGrasz dalej Tak-(1), Nie-(0): ")):
                break
            else:
                if tab_players[2].total_player == 0:
                    print("\nNie masz pieniedzy")
                    time.sleep(4)
                    break
                totalw = int(input("Za ile wchodzisz do gry: "))
                if totalw > tab_players[2].total_player:
                    totalw = tab_players[2].total_player
                sum_total = totalw
                tab_deck = get_deck(3)
                tab_players = get_players(3, totalw, tab_players[2].total_player - totalw)
    except:
        print("Blad programu!")
        time.sleep(3)
