import random as r
import moneybag
def deckOfCards():    
    #storage
    #list
    cardDeck = []
    #tuple(s)
    cardPlace = ()
    suitsOfCards = ()
    
    #Building the decks
    
    #cardPlace string names
    for cardPlace in range(1,14):   
        #cardPlace string faces
        for suitsOfCards in range(0,4):    
            #Placement of card in the cut
            placement = ""          
            #Face value of the card
            face = ""               
            #Creating a list to place 14 cards with and assigning string names for 'face' cards
            if cardPlace == 1:      
                placement = "Ace"
            elif cardPlace == 11:
                placement = "Jack"
            elif cardPlace == 12:
                placement = "Queen"
            elif cardPlace == 13:
                placement = "King"
            else:
                placement = str(cardPlace)
            #Creating a list for Suit placement and assigning a string value
            if suitsOfCards == 0:          
                suit = "of Spades"
            elif suitsOfCards == 1:
                suit = "of Clubs"
            elif suitsOfCards == 2:
                suit = "of Hearts"
            elif suitsOfCards == 3:
                suit = "of Diamonds"
            else:
                suit = str(suitsOfCards)
            #Trying to create the cardStack list and append tuple values into it
            cardStack = []          
            cardStack.append(placement)
            cardStack.append(suit)
            #This keeps the place but adds an INT value of 10
            if(cardPlace >= 10):    
                cardStack.append(10)
            elif(cardPlace == 1):
                #cardStack.append(1)
                cardStack.append(11)
            else:
                cardStack.append(cardPlace)
            
            cardDeck.append(cardStack)
    #print(cardDeck)
    return cardDeck
#deckOfCards()

def receiveCard(deck):
    received = r.randint(0, len(deck) -1)
    card = (deck[received])
    del deck[received]
    return card



def processingGame(storedMoney):
#storedmoney is the money 'stored' on the betting menu.
    deck = deckOfCards() 
    #storage
    player = ''
    cardPoolPlayer = 0   
    cpu = ''
    cpuPool = 0
    stand = ''
    hitme = ''
    choice = 0
    # just a string variable
    win = '\nYou Win'
    lose = '\nYou Lose'
    # the following code initializes the game by drawing 2 cards
    # input
    player = (receiveCard(deck))
    cpu = (receiveCard(deck))
    cardPoolPlayer += player[2]
    cpuPool += cpu[2]
    # output
    print('\nPlayer got: ', player)
    print('\nPlayer Pool: ', cardPoolPlayer)
    #print('Cpu got: ', cpu)
    #print('Dealer Pool: ', cpuPool)
    #print(deck)
    # input
    player = (receiveCard(deck))
    cpu = (receiveCard(deck))
    cardPoolPlayer += player[2]
    cpuPool += cpu[2]
    # output
    print('\nPlayer got: ', player)
    print('\nPlayer Pool: ', cardPoolPlayer)
    #print('Cpu got: ', cpu)
    #print('Dealer Pool: ', cpuPool)
    #print(deck)

    # a while loop to force both the player and cpu to draw cards UNTIL they reach 20
    while cardPoolPlayer < 21 and cpuPool < 21:
        choice = input("\n\nEnter 1 to hit, otherwise \n" +
                       "Enter 2 to stand or" +
                       "\nEnter 3 to quit and lose your bet.")
        # makes the cpu stand when cpu is greater than or equal to 17
        if choice == '1' and cpuPool >= 17:
            hitMe = input('enter to hit.')
            player = (receiveCard(deck))
            cardPoolPlayer += player[2]
            print('\nPlayer got: ', player)
            print('\nPlayer Pool: ', cardPoolPlayer)
            #print('Cpu got: ', cpu)
            #print('Dealer Pool: ', cpuPool)
            print('\nDealer Stands')
        elif choice == '1': 
            hitMe = input('enter to hit.')
            player = (receiveCard(deck))
            cpu = (receiveCard(deck))
            # this is where the player gets to decide if ace is 1 or 11
            if player[2] == 11:
                choice = input('\nYou have drawn an Ace! Would you like it be 1 <enter 1> or,'+
                            '\n11 <enter 2> : ')
                if choice == '1':
                    cardPoolPlayer += 1
                elif choice == '2':
                    cardPoolPlayer += 11
                else:
                    while choice != '1' or '2':
                        print("\nYou must enter a valid choice, 1 or 2.")
                        choice = input('\nYou have drawn an Ace! Would you like it be 1 <enter 1> or,'+
                            '\n11 <enter 2> : ')
                        if choice == '1':
                            cardPoolPlayer += 1
                            break
                        elif choice == '2':
                            cardPoolPlayer += 11
                            break
            # this exists for normal hitting
            else:                  
                cardPoolPlayer += player[2]
            cpuPool += cpu[2]
            print('\nPlayer got: ', player)
            print('\nPlayer Pool: ', cardPoolPlayer)
            #print('Cpu got: ', cpu)
            #print('Dealer Pool: ', cpuPool)
            #print(deck)
        # cpu will draw a card if less than 17 and player stands
        elif choice == '2' and cpuPool < 17:
            print('\nYou stand')
            print('\nPlayer Pool: ', cardPoolPlayer)
            cpu = (receiveCard(deck))
            cpuPool += cpu[2]
        # cpu greater or equal to 17 winner is decided
        elif choice == '2' and cpuPool >= 17:
            print('\nPlayer Stands.')
            print('\nDealer Stands.')
            #print('\nDealer Pool: ', cpuPool)
            # stuck the win loss here, very basic. added returns so money does not
            # double the stack or delete my whole wallet and back to 0 dollars
            if choice == '2' and cpuPool > cardPoolPlayer and cpuPool < 21:
                print('\nPlayer Pool: ', cardPoolPlayer)
                print('\nDealer Pool: ', cpuPool)
                print(lose)
                currentMoney = moneybag.readMyMoney()
                storedMoney = int(currentMoney) - int(storedMoney)
                moneybag.saveMoney(storedMoney)
                print('\nYou now have ' + str(storedMoney) + ' dollars.')
                return
            elif choice == '2' and cpuPool < cardPoolPlayer and cpuPool < 21:
                print('\nPlayer Pool: ', cardPoolPlayer)
                print('\nDealer Pool: ', cpuPool)
                print(win)
                currentMoney = moneybag.readMyMoney()
                storedMoney = int(currentMoney) + int(storedMoney)
                moneybag.saveMoney(storedMoney)
                print('\nYou now have ' + str(storedMoney) + ' dollars.')
                return
            else:
                choice == '2' and cpuPool == cardPoolPlayer
                print('\nPlayer Pool: ', cardPoolPlayer)
                print('\nDealer Pool: ', cpuPool)
                print(lose)
                currentMoney = moneybag.readMyMoney()
                storedMoney = int(currentMoney) - int(storedMoney)
                moneybag.saveMoney(storedMoney)
                print('\nYou now have ' + str(storedMoney) + ' dollars.')
                return          
         # this quits, returns to main and loses the bet           
        elif choice == '3':
            print('You chose to quit.')
            currentMoney = moneybag.readMyMoney()
            storedMoney = int(currentMoney) - int(storedMoney)
            moneybag.saveMoney(storedMoney)
            print('\nYou now have ' + str(storedMoney) + ' dollars.')
            break
        else:
            if choice != '1' or '2' or '3':
                print('You must enter a valid choice.')
    # all possible win loss scenarios
    # cpu = player = loss
    if cpuPool == cardPoolPlayer:
        print('\nDealer Pool: ', cpuPool)
        print(lose)
        currentMoney = moneybag.readMyMoney()
        storedMoney = int(currentMoney) - int(storedMoney)
        moneybag.saveMoney(storedMoney)
        print('\nYou now have ' + str(storedMoney) + ' dollars.')
        # player = 21 and cpu > 21 = win
    elif cardPoolPlayer == 21 and cpuPool > 21:
        print('\nDealer Pool: ', cpuPool)
        print(win)
        # the money that exists currently in txt file
        currentMoney = moneybag.readMyMoney()
        # the stored money in bet menu adds or subtracts from whatever 'CurrentMoney' is.
        storedMoney = int(currentMoney) + int(storedMoney)
        # saves the new money from stored money ontop of whatever current money was.
        moneybag.saveMoney(storedMoney)
        print('\nYou now have ' + str(storedMoney) + ' dollars.')
        # player = 21 and cpu less than 21 = win
    elif cardPoolPlayer == 21 and cpuPool < 21:
        print('\nDealer Pool: ', cpuPool)
        print(win)
        currentMoney = moneybag.readMyMoney()
        storedMoney = int(currentMoney) + int(storedMoney)
        moneybag.saveMoney(storedMoney)
        print('\nYou now have ' + str(storedMoney) + ' dollars.')
        # both cpu and player equal 21 = loss
    elif cpuPool == 21 and cardPoolPlayer == 21:
        print('\nDealer Pool: ', cpuPool)
        print(lose)
        currentMoney = moneybag.readMyMoney()
        storedMoney = int(currentMoney) - int(storedMoney)
        moneybag.saveMoney(storedMoney)
        print('\nYou now have ' + str(storedMoney) + ' dollars.')
        # player greater than 21 and cpu less than 21 = loss
    elif cardPoolPlayer > 21 and cpuPool < 21:
        print('\nDealer Pool: ', cpuPool)
        print(lose)
        currentMoney = moneybag.readMyMoney()
        storedMoney = int(currentMoney) - int(storedMoney)
        moneybag.saveMoney(storedMoney)
        print('\nYou now have ' + str(storedMoney) + ' dollars.')
        # player less or equal to 21 and cpu greater than 21 = win
    elif cardPoolPlayer <= 21 and cpuPool > 21:
        print('\nDealer Pool: ', cpuPool)
        print(win)
        currentMoney = moneybag.readMyMoney()
        storedMoney = int(currentMoney) + int(storedMoney)
        moneybag.saveMoney(storedMoney)
        print('\nYou now have ' + str(storedMoney) + ' dollars.')
        #player less than 21 and cpu == 21 = loss
    elif cardPoolPlayer < 21 and cpuPool == 21:
        print('\nDealer Pool: ', cpuPool)
        print(lose)
        currentMoney = moneybag.readMyMoney()
        storedMoney = int(currentMoney) - int(storedMoney)
        moneybag.saveMoney(storedMoney)
        print('\nYou now have ' + str(storedMoney) + ' dollars.')
        #player greater or equal to 21 and cpu greater or equal to 21 = loss
    elif cardPoolPlayer >= 21 and cpuPool >= 21:
        print('\nDealer Pool: ', cpuPool)
        print(lose)
        currentMoney = moneybag.readMyMoney()
        storedMoney = int(currentMoney) - int(storedMoney)
        moneybag.saveMoney(storedMoney)
        print('\nYou now have ' + str(storedMoney) + ' dollars.')
    


