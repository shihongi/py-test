#!/usr/bin/env python
import random



class Yamahuda():
  # class hensu-
  SUITS=('S','H','D','C')
  NUMBER=range(1,14)

  def __init__(self):
    # instance hensu-
    self.deck=[]
    for s in SUITS:
      for n in NUMBER:
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
      


deck1=Yamahuda()
deck2=Yamahuda()

deck2.shuffle()

deck1.dump()
deck2.dump()

card=deck1.get1card()
deck1.dump()
print('hiita card=',card)



