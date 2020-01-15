#!/usr/bin/env python
import random



class Yamahuda():
  SUITS=('S','H','D','C')
  NUMBER=range(1,14)
  deck=[]

  def __init__(self):
    for s in self.SUITS:
      for n in self.NUMBER:
        card=[s,n]
        self.deck.append(card)

  def shuffle(self):
    print('---shuffle--')
    random.shuffle(self.deck)

  def get1card(self):
    card=self.deck[0]
    self.deck.remove(card)
    return card

  def get1card2(self):
    return self.deck.pop()

  def dump(self):
    print('------ dump -----------')
    print(self.deck)
      


deck=Yamahuda()

deck.dump()

deck.shuffle()
deck.dump()

card=deck.get1card()
deck.dump()
print('hiita card=',card)



