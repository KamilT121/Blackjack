import players

# Test players def split

p = players.Players(300, [], 0, 0)

p.split(100)
print(f'{p.total_player} = 200    {p.prices} = 100')

p.split(50)
print(f'{p.total_player} = 150    {p.prices} = 150')

p.split(150)
print(f'{p.total_player} = 0    {p.prices} = 300')

print(f'{p.split(100)} = False')
