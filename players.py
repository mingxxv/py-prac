players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4]) #omitting the first index starts the slice at the beginning of the list
print(players[2:]) #and the end of the list
print(players[-3:]) #negative values

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())