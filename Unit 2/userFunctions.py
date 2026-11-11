import random

# Functions - Code instructions for the 
# computer to follow. 

# ! EVERYTHING IS A FUNCTION !

# Functions have 2 phases 
# phase 1: function definition
# phase 2: function invocation

# Function definition - the actual instructions
# telling the computer how you want something to be
# done step-by-step

# function def syntax (how it is written)
def goodMorning():
    print("gooding morning") # STEP 1
    name = input("whats your name: ") # STEP 2
    print("welcome "+ name) # STEP 3

# function invocation/ call 
# when we write functions name it will run the program
# goodMorning()




















def rpsGame():
    print("welcome to RPS")
    userMove = input()
    cpuMove = random.randint(1,3)
    turns = 0

    while turns < 3:
        if cpuMove == 1:
            print('rock')
            turns +=1 
        elif cpuMove== 2:
            print('paper')
            turns +=1 
        else: 
            print('scissor')
            turns +=1 
    print("game over")

rpsGame()