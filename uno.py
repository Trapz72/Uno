import random
import time
import sys

master=["blue 0", "blue 1", "blue 2", "blue 3", "blue 4", "blue 5", "blue 6", "blue 7", "blue 8", "blue 9", "blue +2", "green 0", "green 1", "green 2",
        "green 3", "green 4", "green 5", "green 6", "green 7", "green 8", "green 9", "green +2", "red 0", "red 1", "red 2", "red 3", "red 4", "red 5",
        "red 6", "red 7", "red 8", "red 9", "red +2", "yellow 0", "yellow 1", "yellow 2", "yellow 3", "yellow 4", "yellow 5", "yellow 6", "yellow 7",
        "yellow 8", "yellow 9", "yellow+2"]

deck=master[random.randint(0,43)]
hand=[]
b1hand=[]
b2hand=[]
b3hand=[]
b1turn=False
b2turn=False
b3turn=False
b1fail=0
b2fail=0
b3fail=0
win=False

for x in range(0,7,1):
    hand.append(master[random.randint(0,39)])
    b1hand.append(master[random.randint(0,39)])
    b2hand.append(master[random.randint(0,39)])
    b3hand.append(master[random.randint(0,39)])

while win == False:
    
    time.sleep(1)
    print("")
    time.sleep(0.25)
    print("Your hand:",hand)
    time.sleep(0.25)
    print("the deck:",deck)
    time.sleep(0.25)
    action=input(str("Would you like to play or draw a card? "))
    
    if action == "play":
        card=input(str("Which card would you like to play? "))
        
        if card in hand:
            csplit=card.split()
            dsplit=deck.split()
        
            if csplit[0] == dsplit[0]:
                colour=True
            else:
                colour=False
            
            if csplit[1] == dsplit[1]:
                number=True
            else:
                number=False
            
            if colour or number == True:
                deck=card
                hand.remove(card)
                print("You played",card)
                
                if csplit[1] == "+2":
                    b1hand.append(master[random.randint(0,44)])
                    b1hand.append(master[random.randint(0,44)])
                    time.sleep(0.5)
                    print("Bot 1 drew 2 cards")
        
            else:
                print("That card cannot be played")
        else:
            print("That card is not in your hand")
            
    elif action == "draw":
        draw = master[random.randint(0,39)]
        hand.append(draw)
        print("You drew",draw)
        
    else: 
        print("Please try again")
        
    if len(hand) == 1:
        print("Uno!")
    elif len(hand) == 0:
        print("You win!")
        sys.exit()
    
    time.sleep(1)
    print("")
    time.sleep(0.5)
    print("It is bot 1's turn")
    time.sleep(0.5)
    print("Bot 1 has",len(b1hand),"cards")
    
    while b1turn == False:
        for x in range(0,len(b1hand),1):
        
            b1card=b1hand[x]
            b1split=b1card.split()
            dsplit=deck.split()
        
            if b1split[0] == dsplit[0]:
                colour=True
            else:
                colour=False
            
            if b1split[1] == dsplit[1]:
                number=True
            else:
                number=False
            
            if colour or number == True:
                b1play=b1card
            else:
                b1fail=b1fail+1
        
        if b1fail == len(b1hand):
            b1hand.append(master[random.randint(0,39)])
            time.sleep(0.5)
            print("Bot 1 drew a card")
            b1turn=True
        else:
            deck=b1play
            b1hand.remove(b1play)
            time.sleep(0.5)
            print("Bot 1 played",b1play)
            
            if b1split[1] == "+2":
                b2hand.append(master[random.randint(0,44)])
                b2hand.append(master[random.randint(0,44)])
                time.sleep(0.5)
                print("Bot 2 drew 2 cards")
                    
            b1turn=True
            
    if len(b1hand) == 1:
        time.sleep(0.5)
        print("Uno!")
    elif len(b1hand) == 0:
        time.sleep(0.5)
        print("Bot 1 wins!")
        sys.exit()

    time.sleep(1)
    print("")
    time.sleep(0.5)
    print("It is bot 2's turn")
    time.sleep(0.5)
    print("Bot 2 has",len(b2hand),"cards")
    
    while b2turn == False:
        for x in range(0,len(b2hand),1):
        
            b2card=b2hand[x]
            b2split=b2card.split()
            dsplit=deck.split()
        
            if b2split[0] == dsplit[0]:
                colour=True
            else:
                colour=False
                
            if b2split[1] == dsplit[1]:
                number=True
            else:
                number=False

            if colour or number == True:
                b2play=b2card
            else:
                b2fail=b2fail+1
        
        if b2fail == len(b2hand):
            b2hand.append(master[random.randint(0,39)])
            time.sleep(0.5)
            print("Bot 2 drew a card")
            b2turn=True
        else:
            deck=b2play
            b2hand.remove(b2play)
            time.sleep(0.5)
            print("Bot 2 played",b2play)
            
            if b2split[1] == "+2":
                b3hand.append(master[random.randint(0,44)])
                b3hand.append(master[random.randint(0,44)])
                time.sleep(0.5)
                print("Bot 3 drew 2 cards")
                    
            b2turn=True
    
    if len(b2hand) == 1:
        time.sleep(0.5)
        print("Uno!")
    elif len(b2hand) == 0:
        time.sleep(0.5)
        print("Bot 2 wins!")
        sys.exit()
        
    time.sleep(1)
    print("")
    time.sleep(0.5)
    print("It is bot 3's turn")
    time.sleep(0.5)
    print("Bot 3 has",len(b3hand),"cards")
    
    while b3turn == False:
        for x in range(0,len(b3hand),1):
        
            b3card=b3hand[x]
            b3split=b3card.split()
            dsplit=deck.split()
        
            if b3split[0] == dsplit[0]:
                colour=True
            else:
                colour=False
            
            if b3split[1] == dsplit[1]:
                number=True
            else:
                number=False

            if colour or number == True:
                b3play=b3card
            else:
                b3fail=b3fail+1
        
        if b3fail == len(b3hand):
            b3hand.append(master[random.randint(0,39)])
            time.sleep(0.5)
            print("Bot 3 drew a card")
            b3turn=True
        else:
            deck=b3play
            b3hand.remove(b3play)
            time.sleep(0.5)
            print("Bot 3 played",b3play)
            
            if b3split[1] == "+2":
                hand.append(master[random.randint(0,44)])
                hand.append(master[random.randint(0,44)])
                time.sleep(0.5)
                print("You drew 2 cards")
                    
            b3turn=True
    
    if len(b3hand) == 1:
        time.sleep(0.5)
        print("Uno!")
    elif len(b3hand) == 0:
        time.sleep(0.5)
        print("Bot 3 wins!")
        sys.exit()

    b1turn=False
    b2turn=False
    b3turn=False
    b1fail=0
    b2fail=0
    b3fail=0

