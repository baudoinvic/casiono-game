class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin
        self.bet = {'R': 0, 'B': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}

class Cell:
    def __init__(self, name, rate, color):
        self.name = name
        self.rate = rate
        self.cell_color = color

    def display_color(self):
        if self.cell_color == 'red':
            return f"\033[91m{self.name}(x{self.rate})\033[0m"  
        else:
            return f"{self.name}(x{self.rate})"

def create_table():
    global table
    table = [
        Cell('R', 2, 'red'),
        Cell('B', 2, 'black'),
        Cell('1', 8, 'red'),
        Cell('2', 8, 'black'),
        Cell('3', 8, 'red'),
        Cell('4', 8, 'black'),
        Cell('5', 8, 'red'),
        Cell('6', 8, 'black'),
        Cell('7', 8, 'red'),
        Cell('8', 8, 'black')
    ]

def green_bar():
    return "\033[92m|\033[0m"  

def show_players():
    print('Debug: play()')
    for cell in table:
        print(f"{green_bar()}{cell.display_color()}{green_bar()}")

create_table()
show_players()
