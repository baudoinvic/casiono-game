class Human:
    def __init__(self, coins):
        self.coins = coins

    def bet(self):
        bet_coin = int(input("How many coins do you bet?: (1-99) "))
        if 1 <= bet_coin <= 99:
            print(bet_coin)
            self.coins -= bet_coin
            print("MY:", self.coins)
        else:
            print("Invalid bet amount. Please enter a number between 1 and 99.")

# Debugging the play() function
# def play():
#     human_player = Human(500)
#     human_player.bet()

play()
