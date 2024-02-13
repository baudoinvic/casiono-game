class Cell:
   def __init__(self, name, rate, color):
      self.name = name
      self.rate = rate
      self.color = color

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

def show_players():
   print('Debug: play()')
   for cell in table:
       print(f"|{cell.name}(x{cell.rate})|")

create_table()
show_players()