def vendingMachine():
    print("VENDING MACHINE")
    print("Please type in a value for the item you want: ")
    userSelection = input()

    while userSelection != 'q':
        if userSelection == 'b3':
            print("Nacho chips")
            print("Please type in a value for the item you want: ")
            userSelection = input()

        elif userSelection == 'g4':
            print("BBQ chips")
            print("Please type in a value for the item you want: ")
            userSelection = input()
        
        # remaining options... 
        
        else:
            print("Invalid code- please try again")
            print("Please type in a value for the item you want: ")
            userSelection = input()
    
    print("VENDING MACHINE IS OFF")

#vendingMachine()




import random

def diceGame():
    score = 0
    
    print("DICE GAME!!")
    print("Pleae enter R to roll or Q to quit: ")
    userSelection = input()
    while userSelection != 'q':
        if userSelection == 'r':
            diceRollValue= random.randint(1, 7)
            if diceRollValue == 7:
                print("you roll a : "+ str(diceRollValue))
                print("you win")
                score +=10
                print("your current score = " + str(score))
                print("Pleae enter R to roll or Q to quit: ")
                userSelection = input()
            else:
                print("you roll a : "+ str(diceRollValue))
                print("you lose")
                score -=5
                print("your current score = " + str(score))
                print("Pleae enter R to roll or Q to quit: ")
                userSelection = input()
        else:
            print("ERROR: key entry no recognized ")
            print("Pleae enter R to roll or Q to quit: ")
            userSelection = input()
    
    print("DICE GAME HAS BEEN STOPPED... ")
    
diceGame()
















































# def diceGame():
#     print("DICE GAME IS RUNNING...")
#     print("Please type R to roll or Q to quit: ")
#     score = 0
#     userSelection = input()

#     while userSelection != 'q':
#         if userSelection == 'r':
#             randomNumber = random.randint(1, 7)
#             if randomNumber == 7:
#                 print("your number is: "+ str(randomNumber))
#                 print("YOU WIN!!")
#                 score += 10
#                 print("score: "+ str(score))
#                 print("Please type R to roll or Q to quit: ")
#                 userSelection = input()
#             else: 
#                 print("your number is: "+ str(randomNumber))
#                 print("YOU LOSE")
#                 score -= 5
#                 print("score: "+ str(score))
#                 print("Please type R to roll or Q to quit: ")
#                 userSelection = input()
#         else: 
#             print("ERROR: Invaid input...")
#             print("Please type R to roll or Q to quit: ")
#             userSelection = input()
    
#     print("DICE GAME IS OFF...")

# def diceGame():
#     print("DICE GAME IS RUNNING...")
#     print("Please enter r to roll and q to quit: ")
#     userScore = 0
#     userSelection = input()
    
#     while userSelection != 'q':
#         if userSelection == "r":
#             randomNumber = random.randint(1, 7)
#             if randomNumber != 7:
#                 print(randomNumber)
#                 print("You lose")
#                 userScore-=5
#                 print(userScore)
#                 print("Please enter r to roll and q to quit: ")
#                 userSelection = input()
#             elif randomNumber == 7:
#                 print(randomNumber)
#                 print('YOU WIN!!!')
#                 userScore +=10
#                 print(userScore)
#                 print("Please enter r to roll and q to quit: ")
#                 userSelection = input()
#diceGame()