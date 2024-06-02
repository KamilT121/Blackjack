
def strategis(sum, card):
    """
    return 1 - Hit
    return 2 - Stand
    return 3 - Double down
    """
    if sum <= 8:
        return 1
    elif sum == 9:
        if 3 <= card <= 6:
            return 3
        else:
            return 1
    elif sum == 10:
        if card <= 9:
            return 3
        else:
            return 1
    elif sum == 11:
        if card <= 10:
            return 3
        else:
            return 1
    elif sum == 12:
        if 4 <= card <= 6:
            return 2
        else:
            return 1
    elif 13 <= sum <= 16:
        if card <= 6:
            return 2
        else:
            return 1
    else:
        return 2
