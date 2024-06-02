import players

# Test players def get_price

p = players.Players(300, ["Card", "Card_2", "Card_3"], 200, 9)
print(f'{p.get_price()} = 200')

p2 = players.Players(300, ["Card", "Card_2", "Card_3"], 900, 9)
print(f'{p2.get_price()} = 900')
