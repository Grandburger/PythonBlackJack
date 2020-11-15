def createMoneyBag():
    # return error code when problem of file/variable not existing
    money = -1
    # makes sure there is a money.txt file to be read, if not creates one.
    try:
        moneyBag = open('moneyBag.txt', 'r')
        money = moneyBag.readline()
        moneyBag.close()
    except:
        print('\nYou have no money bag, would you like to create one? (If not you'+
        '\ncannot play the game!)')
        print('\n----------------------')
        choice = input('\nSo here\'s the deal bro, Option 1 creates a money bag,'+
                       '\notherwise, anything else goes back to main menu.'+
                       '\nOption: ')
        # simply creates and writes string value 5 later to be read as an int.
        if choice == '1':
            moneyBag = open('moneyBag.txt', 'w')
            moneyBag.write('5')
            moneyBag.close()
            moneyBag = open('moneyBag.txt', 'r')
            money = moneyBag.readline()
            moneyBag.close()
    return money
# concept behind this was I had a 'fake' bet that would lead to an actual bet            
def actualBet():
    # this just reads the moneybag since moneybag is already created and has to be
    money = createMoneyBag()
     # Makes it so only valid input and money player actually has in txt file.
     # also changes str to int for it to be able to be actually functional
    while True:
        bet = input('\nHow much do you want to bet? ')
        try:
            if int(bet) <= int(money) and int(bet) %5 == 0 and int(bet) >= 5:
                print('\nYou bet ' + bet + ' dollars')
                break
            else:
                print('\nMinimum bet must be 5 and multiples of 5')
                print('And please enter money you actually have.')
        except:
            print('Please type a valid number.')
    return bet
# just reads the money
def readMyMoney():
    moneyBag = open('moneyBag.txt', 'r')
    money = moneyBag.readline()
    moneyBag.close()
    return money

def purchaseStuff():
    money = createMoneyBag()
    # while moneybag exists
    while True:
        # checks if you even have enough to attempt to buy
        if int(money) >= 20:
            purchase = input('\nWould you like to spend 20 dollars on an html template or a CSS template?'+
                             '\nEnter 1 to purchase an HTML template' +
                             '\nEnter 2 to purchase a CSS template' +
                             '\nEnter literally anything else to return to main menu.'+
                             '\nOption: ')
            if purchase == '1':
                fee = int(money) - 20
                saveMoney(fee)
                money = createMoneyBag()
                # reads the number and assigns the new number to new file
                # that way no duplicates! AND actually gives new files!
                htmlnumber = readHtmlNumber()
                html = open('mypurchasedhtml' + str(htmlnumber) + '.html', 'w')
                # in here I build the template only using it once
                # and is standard for all of them
                html.write('<!DOCTYPE html>\n' +
                           '<html lang="en">\n' +
                           '\t<head>\n\t\t<title>YOUR TITLE</title>\n' +
                           '\n\t\t<meta charset="UTF-8">'
                           '\n\t\t<meta name="viewport"' +
                           'content="width=device-width,' +
                           'initial-scale=1.0">'
                           '\n\t</head>\n\t<body>' +
                           '\n\t\t<div>CONTENT' +
                           '</div>\n\t</body>\n</html>')
                html.close()
                # adding the html number up one to the name of file from the .txt
                htmlnumber += 1
                saveHtmlNumber(htmlnumber)
                print('\nYou purchased an HTML template.')
                print('\nYou now have ' + money + ' dollars.')
                break
            elif purchase == '2':
                fee = int(money) - 20
                saveMoney(fee)
                money = createMoneyBag()
                cssnumber = readCSSNumber()
                css = open('mypurchasedcss' + str(cssnumber) + '.css', 'w')
                # building the css template
                css.write('* {\n\tmargin: 0;\n\tpadding:0;' +
                          '\n}\n\nbody {\n\twidth: 90%;' +
                          '\n\tmargin: 0 auto;\n\t' +
                          'background-color: gold;\n}')
                css.close()
                # adding the cssnumber up one to the name of file from the .txt
                cssnumber += 1
                saveCSSNumber(cssnumber)
                print('\nYou purchased a CSS template.')
                print('\nYou now have ' + money + ' dollars.')
                break
            else:
                break
        else:
            print("You don't have enough money, play some more to spend some more \n: ^ )")
            break
    return
            
def saveMoney(storedMoney):
    # makes it so money will always be 5, even if you get to 0 the existing
    # text file will be overwritten to 5 again.
    if storedMoney < 5:
        storedMoney = 5
        
    moneyBag = open('moneyBag.txt', 'w')
    moneyBag.write (str(storedMoney))
    moneyBag.close()
    return
# the following functions only exist to keep looping and creating files with the same name
def readHtmlNumber():
    try:
        html = open('html.txt', 'r')
        htmlnumber = int(html.readline())
        html.close()
        return htmlnumber
    except:
        # This will write in 1 on the file if it does not exist.
        html = open('html.txt', 'w')
        html.write('1')
        html.close()
        htmlnumber = 1
        return htmlnumber
    # this code will increase the number
def saveHtmlNumber(htmlnumber):
    html = open('html.txt', 'w')
    html.write(str(htmlnumber))

def readCSSNumber():
    try:
        css = open('css.txt', 'r')
        cssnumber = int(css.readline())
        css.close()
        return cssnumber
    except:
        # This will write in 1 on the file if it does not exist.
        css = open('css.txt', 'w')
        css.write('1')
        css.close()
        cssnumber = 1
        return cssnumber

def saveCSSNumber(cssnumber):
    css = open('css.txt', 'w')
    css.write(str(cssnumber))
        
    

