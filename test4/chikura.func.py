#!/usr/bin/env python

def makeDeck():
  # spade, hearts, diamond, clovers 
  SUITS=('S','H','D','C')
  # 1..13
  NUMBER=range(1,14)
  deck=[]
  for s in SUITS:
    for n in NUMBER:
      card=[s,n]
      deck.append(card)
  return deck

# print deck
deck=makeDeck()
print(deck)

#mission
def get1card(deck):
    card=deck[0]
    deck.remove(card)
    return card

card=get1card(deck)
print('シャッフル前の山札から1枚引く')
print(card)
print('1枚引いた後の山札')
print(deck)

deck=makeDeck()

def deckShuffle(deck):
    import random
    random.shuffle(deck)
    return deck

barabara=deckShuffle(deck)
print('シャッフル後の山札')
print(barabara)

card=get1card(deck)
print('シャッフル後の山札から一枚引く')
print(card)
print('1枚引いた後の山札')
print(deck)
