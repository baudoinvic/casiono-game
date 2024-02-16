class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin


class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)
        self.bet_coin = 0
        self.bet_cell = ''

    def enable_bet_cell(self, cell):
        if cell == 'R' or cell == 'B' or cell in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return True
        else:
            return False

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

# Debug: play()
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

human_player = Human('MY', 500)
human_player.bet()
print(f"{human_player.name} bet {human_player.bet_coin} coin(s) on {human_player.bet_cell}.")
