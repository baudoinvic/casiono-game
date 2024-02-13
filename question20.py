import random

class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

class Computer(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)
        self.bet_coin = 0
        self.bet_cell = ''

    def bet(self):
        self.bet_coin = random.randint(1, 99)
        self.bet_cell = str(random.randint(1, 8))
        print(f"{self.name} bet {self.bet_coin} coin(s) on {self.bet_cell}.")

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

computer_player = Computer('C1', 500)
computer_player.bet()
