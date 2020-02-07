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
    ts=[]
    for card in self.mycards:
      if card[1]==1:
        ts.append(0) # A
      else:
        ts.append(card[1]) # 2345..JQK

    while 1:
      tmp=0
      for number in ts:
        if number==0: # A
          tmp+=11
        elif number>10:
          tmp+=10
        else:
          tmp+=number

      if tmp<=21:
        return tmp

      if not 0 in ts:
        return tmp

      for i in range(0,len(ts)):
        if ts[i]==0:
          ts[i]=1
          break
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
you.setCard(['S',1]) # 11
print("your card is ",you.status()) # 11
you.setCard(['D',1]) # 11+11=22 , 11 + 1 = 12
print("your card is ",you.status()) # 12
you.setCard(['S',8]) # 11+1+8 =20
print("your card is ",you.status()) # 20
you.setCard(['D',2]) # 11+1+8+2 =22 , 1+1+8+2=12
print("your card is ",you.status()) # 12
you.setCard(['S',1]) # 13
print("Your card is ",you.status()) # 13
