class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

    def bet(self):
        return 0  # Placeholder method for human player

class Human(Player):
    def bet(self):
        while True:
            bet_amount = int(input("How many coins do you bet?: (1-99) "))
            if 1 <= bet_amount <= 99:
                print(f"{self.name} bets {bet_amount} coin(s).")
                return bet_amount
            else:
                print("Invalid bet amount. Please enter a number between 1 and 99.")

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

    # Each player places a bet
    for player in players:
        bet_amount = player.bet()
        player.coin -= bet_amount

    # Print updated coin amounts after bets
    for player in players:
        print(f"{player.name}: {player.coin}")

create_players()
play()
