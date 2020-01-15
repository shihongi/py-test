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
print('$B%7%c%C%U%kA0$N;3;%$+$i(B1$BKg0z$/(B')
print(card)
print('1$BKg0z$$$?8e$N;3;%(B')
print(deck)

deck=makeDeck()

def deckShuffle(deck):
    import random
    random.shuffle(deck)
    return deck

barabara=deckShuffle(deck)
print('$B%7%c%C%U%k8e$N;3;%(B')
print(barabara)

card=get1card(deck)
print('$B%7%c%C%U%k8e$N;3;%$+$i0lKg0z$/(B')
print(card)
print('1$BKg0z$$$?8e$N;3;%(B')
print(deck)
