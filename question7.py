class Human:
    def __init__(self, coins):
        self.coins = coins

    def bet(self):
        while True:
            bet_coin = input("How many coins do you bet?: (1-99) ")
            if bet_coin.isdigit():  
                bet_coin = int(bet_coin)
                if 1 <= bet_coin <= 99:
                    print(bet_coin)
                    break
                else:
                    print("Invalid bet amount. Please enter a number between 1 and 99.")
            else:
                print("Invalid input. Please enter a valid integer.")

# Debugging the play() function
def play():
    print("MY:", 500)
    human_player = Human(500)
    human_player.bet()

play()
