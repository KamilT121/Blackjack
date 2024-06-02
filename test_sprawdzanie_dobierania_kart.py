import players

# Test players def get_card

p = players.Players(300, [], 0, 0)

p.get_card("Card", 3)
print(f'{p.sum_value} = 3    {p.cards} = ["Card"]')

p.get_card("Card_2", 6)
print(f'{p.sum_value} = 9    {p.cards} = ["Card", "Card_2]')

p.get_card("Card_3", 1)
print(f'{p.sum_value} = 10    {p.cards} = ["Card", "Card_2", "Card_3"]')
