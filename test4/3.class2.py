#!/usr/bin/env python
import random



class Yamahuda():
  SUITS=('S','H','D','C')
  NUMBER=range(1,14)

  def __init__(self):
    self.deck=[]
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
      

class Tehuda():
  mycards=[]

  def __init__(self):
    pass

  def setCard(self, card):
    self.mycards.append(card)

  def dump(self):
    print('---card in hand----')
    print(self.mycards)


deck=Yamahuda()
deck.shuffle()
deck.dump()

myhand=Tehuda()
card=deck.get1card2()

myhand.setCard(card)
deck.dump()
myhand.dump()



