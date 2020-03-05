#!/usr/bin/env python
import random


class Yamahuda():
    SUITS=('S','H','D','C')
    NUMBER=range(1,14)

    def __init__(self):
        #instant
        self.deck=[]
        for s in self.SUITS:
            for n in self.NUMBER:
                card=[s,n]
                self.deck.append(card)

    def shuffle(self):
        print('---shuffle---')
        random.shuffle(self.deck)

    def get1card(self):
        print('---get 1card---')
        return self.deck.pop()

    def dump(self):
        print('---dump---')
        print(self.deck)

class Tehuda():

    def __init__(self):
        self.mycards=[]

    def setCard(self, card):
        self.mycards.append(card)

    def goukei(self):
        ts=[] #引いたカードを計算用に格納するリストtsを作成
        for card in self.mycards:
            if card[1]==1:
                ts.append(0) #引いたカードがA
            else:
                ts.append(card[1]) #A以外を引く

        while 1:
            tmp=0
            for number in ts:
                if number==0: #Aを引く
                    tmp+=11
                elif number>10: #10,J,Q,K
                    tmp+=10
                else:
                    tmp+=number
            
            if tmp<=21:
                return tmp

            if not 0 in ts:
                return tmp

            for i in range(0,len(ts)): #Aが手札にある場合、計算を終わらせるための処理を行う
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
        print('--tehuda dump--')
        print(self.mycards)

# ===================================
print('<<< welcome BJ>>>')
deck=Yamahuda()
deck.shuffle()
#deck.dump

dealer=Tehuda()
you=Tehuda()

# ===You and Dealer deraw 1 card===
you.setCard(deck.get1card())
print("Your card is ",you.status())

dealer.setCard(deck.get1card())
print("Dealer's card is ",dealer.status())

# ===Your draw turn===
print("Do you draw a card ?(y/n)")
YourPoint=you.goukei()
while input()=='y' and YourPoint<21:
    you.setCard(deck.get1card())
    print("your card is ",you.status())
    YourPoint=you.goukei()
    if YourPoint<21:
        print("Do you draw a card?(y/n)")

# ===Dealer's draw turn===
DealerPoint=dealer.goukei()
while DealerPoint<=16:
    print("Dealer doraw 1 card")
    dealer.setCard(deck.get1card())
    print("Dealer's card is ",dealer.status())
    DealerPoint=dealer.goukei()

# ===judge win or lose===
print("---judgement time---")
if YourPoint>=22:
    print("You lose...")
else:
    if DealerPoint>=22:
        print("You win !")
    else:
        if YourPoint>DealerPoint:
            print("You win !")
        elif YourPoint==DealerPoint:
                print("This is a drawn geme")
        else:
            print("You lose...")


