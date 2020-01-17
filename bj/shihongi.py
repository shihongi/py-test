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
    print('---get 1card--')
    return self.deck.pop()

  def dump(self):
    print('--- deck dump --')
    print(self.deck)


class Tehuda():
  def __init__(self):
    self.mycards=[]

  def setCard(self, card):
    self.mycards.append(card)

  def goukei(self):
    tmp=0
    for card in self.mycards:
      if card[1]>10:
        tmp+=10
      else:
        tmp+=card[1]
    return tmp

  def status(self):
    msg=''
    for card in self.mycards:
      msg+=card[0]+str(card[1])+' '
    msg+=' Point:'+str(self.goukei())
    return msg

  def dump(self):
    print('---tehuda dump ---')
    print(self.mycards)



# ============================================
print('<<<< wellcome BJ>>>>')
deck=Yamahuda()
deck.shuffle()

dealer=Tehuda()
you=Tehuda()

# ====You and Dealer draw 1 card ====
you.setCard(deck.get1card())
print("Your card is ",you.status())

dealer.setCard(deck.get1card())
print("Dealer's card is ",dealer.status())

# ====Your draw turn ====
print("Do you draw a card ?(y/n)")
while input()=='y':
  you.setCard(deck.get1card())
  print("your card is ",you.status())

# ====Dealer draw turn ====
# todo

# ==== judge win or lose ===
# todo

