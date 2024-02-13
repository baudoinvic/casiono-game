import random

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin


class Human(Player):
  def __init__(self, name, coin):
    self.name = name
    super()._init_(name,coin)

def play():
  print('Debug:play()')


play()