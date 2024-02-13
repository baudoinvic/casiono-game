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
    players.append(Computer('C1', 500))
    players.append(Computer('C2', 500))
    players.append(Computer('C3', 500))

def play():
    print('Debug: play()')
    for player in players:
        print(f"{player.name}: {player.coin}")

create_players()
play()
