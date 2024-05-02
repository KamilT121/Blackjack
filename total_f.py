def sum_total(total_player, bet):
    global total
    if total_player >= bet:
        total += bet
        total_player -= bet
        return total_player
    return False

def win(total_player, number_win):
    global total
    total_player+=int(total/number_win)
    return total_player
