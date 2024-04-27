def split(total_player, bety):
    global total
    if total_player>=bet:
        total+=bet
        total_player-=bet
        return total_player
    else:
        return False

def win(total_player, number_win):
    global total
    total_player+=int(total/number_win)
    return total_player
