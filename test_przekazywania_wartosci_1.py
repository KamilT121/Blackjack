import players

# Test players def get_sum_value

p = players.Players(300, ["Card", "Card_2", "Card_3"], 200, 9)
print(f'{p.get_sum_value()} = 9')

p2 = players.Players(300, ["Card", "Card_2", "Card_3"], 900, 19)
print(f'{p2.get_sum_value()} = 19')
