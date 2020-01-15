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

# mission
#card=get1card(deck)
#print(card)
#print(deck)



