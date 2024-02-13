class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

class Human(Player):
    pass

class Computer(Player):
    pass

players = []

def create_players():
    global players
    players.append(Human('MY', 500))
    players.append(Human('C1', 500))
    players.append(Human('C2', 500))
    players.append(Human('C2', 500))

def play():
    print('Debug: play()')

create_players()
print('Debug: play()')