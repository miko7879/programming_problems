from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f'{self.name} {self.score}'
        
    def comparator(a, b):
        if a.score > b.score:
            return -1
        if a.score < b.score:
            return 1
        return -1 if a.name < b.name else 1 if a.name > b.name else 0

players = [('amy', 100), ('david', 100), ('heraldo', 50), ('aakansha', 75), ('aleksa', 150)]
data = []
for p in players:
    name, score = p
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)