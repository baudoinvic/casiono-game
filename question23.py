# Define the Player and Human classes as provided in your previous context
class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin


class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)
        self.bets = {}

    def enable_bet_cell(self, cell):
        return cell.upper() in ['R', 'B'] or cell in ['1', '2', '3', '4', '5', '6', '7', '8']

    def bet(self):
        while True:
            try:
                self.bet_coin = int(input("How many coins do you bet?: (1-99) "))
                if 1 <= self.bet_coin <= 99:
                    break
                else:
                    print("Invalid bet amount. Please enter a number between 1 and 99.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            self.bet_cell = input("On what do you bet?: (R, B, 1-8) ").upper()
            if self.enable_bet_cell(self.bet_cell):
                break
            else:
                print("Invalid input. Please enter R, B, or a number between 1 and 8.")

        self.bets[self.bet_cell] = self.bet_coin

        print(f"{self.name} bet {self.bet_coin} coin(s) to {self.bet_cell}.")


# Define the bet_players function
def bet_players(players):
    for player in players:
        player.bet()


# Debug: play()
print("Debug: play()")
print("|_____|MY|C1|C2|C3|")
print("|R(×2)|00|00|00|00|")
print("|B(×2)|00|00|00|00|")
print("|1(x8)|00|00|00|00|")
print("|2(x8)|00|00|00|00|")
print("|3(x8)|00|00|00|00|")
print("|4(x8)|00|00|00|00|")
print("|5(x8)|00|00|00|00|")
print("|6(x8)|00|00|00|00|")
print("|7(x8)|00|00|00|00|")
print("|8(x8)|00|00|00|00|")

# Example usage:
players = [Human('MY', 500), Human('C1', 500), Human('C2', 500), Human('C3', 500)]
bet_players(players)

# Print the bets
for player in players:
    for key, value in player.bets.items():
        print(f"{player.name} bet {value} coin(s) to {key}.")

# Simulating the winning number
winning_number = 'R'
print(f"Winning number is {winning_number}.")

# Determine winners
winners = [player.name for player in players if winning_number in player.bets.keys()]
if winners:
    print(f"{', '.join(winners)} won.")
else:
    print("No winners.")
