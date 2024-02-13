import random

class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

class Human:
    def __init__(self, coins):
        self.coins = coins

    def bet(self):
        self.bet_coin = int(input("How many coins do you bet?: (1-99) "))

# Debugging the play() function
def play():
    print("MY:", 500)
    human_player = Human(500)
    human_player.bet()
    print(human_player.bet_coin)

play()
