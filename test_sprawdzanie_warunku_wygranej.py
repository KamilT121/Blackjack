import players

# Test players def win

p = players.Players(300, ["Card", "Card_2", "Card_3"], 200, 9)

p.win(100)

print(f'{p.total_player} = 400')
print(f'{p.prices} = 0')
print(f'{p.cards} = []')
print(f'{p.sum_value} = 0')
