import cards
import moneybag
import validationint

def mainMenu():

    # storage
    quitProgram = False
    choice = 0
    money = ''
    while quitProgram == False:
        
        # main menu loop
        showMenu()
        print("\n\nChoose an option.")
        #Validates the choices, to force only 1-4
        choice = validationint.getRangedInt("Your choice:", "Enter 1-4 only.", 1, 4)
        if choice == 1:
            # have to read or create the moneybag
            money = moneybag.createMoneyBag()
            print('You have ' + str(money) + ' dollars to bet.' )
            # assign a variable to call actualBet and to use as a parameter
            # than passes to make a bet and goes into the game menu
            if money != -1:
                storedMoney = moneybag.actualBet()
                # prevents typing invalid values
                # also gets the money to store for the win/loss
                blackJackMenu(storedMoney)
            else:
                print('Please create a moneybag to use the program.')
            # essentially the same exact thing as option 1, but does not move them to game menu
        elif choice == 2:
            money = moneybag.createMoneyBag()
            # me using -1 is just to handle errors since the moneybag cannot be -1
            if money != -1:
                print('You have ' + str(money) + ' dollars to bet.' )
        # jumps to purchasing
        elif choice == 3:
            theShop = moneybag.purchaseStuff()
        # quits the program entirely   
        elif choice == 4:
            quitProgram = True
            print("\nThanks for playing!")
            print ("\nCome back again!")

def showMenu():
    print("\nMain Menu\n\n")
    print("\t1. Bet!")
    print("\t2. Money bag!")
    print("\t3. The template store!")
    print("\t4. Quit Program")

def blackJackMenu(storedMoney):
    # storage
    quitProgram = False
    choice = 0
    
    while quitProgram == False:

        # game menu loop
        showMenuBlackjack()
        print("\n\nChoose an option.")
        choice = validationint.getRangedInt("Your choice:", "Enter 1-2 only.", 1, 2)
        # begins the game
        if choice == 1:
            cards.processingGame(storedMoney)
            # causes user to return to original menu to bet again.
            break
            # only moves user to original main menu.
        elif choice == 2:
            quitProgram = True
            
    print("\nBack to Main Menu.")

def showMenuBlackjack():
    print("\nBlackjack\n\n")
    print("\t1. Let's Play!")
    print("\t2. Go back to Main Menu")

mainMenu()
