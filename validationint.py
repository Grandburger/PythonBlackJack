def getRangedInt (message, errorMessage, low, high):
    
    #Storage
    
    isValidInt = False
    test_input = ""
    IntToReturn = 0

    #input - see parameters

    while isValidInt == False:
        try:
            test_input = input(message + " ")

    #processing
            
            IntToReturn = int(test_input) #unsafe code
            if (IntToReturn < low or IntToReturn > high):
                raise ValueError()
            isValidInt = True
        except:
            print(errorMessage)
            input("Press <enter> to try again.")

    #output
    return IntToReturn

