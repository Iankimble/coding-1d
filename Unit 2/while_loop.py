# Loop - a loop is a construct (special function) that repeats itself. 
# In programming, a loop allows to repeat code instructions. 

# There are two types of loops: For loop and While loop

# While loop - a type of loop where so long as a condition is equal 
# to TRUE it will keep running "forever". 

# the keyword is while --> do while 

# syntax
# num = 4 
# while 2+2 == num: # Condition --> Operations - must be TRUE
#     print("the program is running...")
#     num = int(input("Please type in any number but 4 to stop the program"))

# While loops will ALWAYS run unless you change the condition!
# we can do this by writing instructions to manually change it. 
# The computer must ALWAYS complete their tasks before moving to the 
# next step


def guessingGame():
    correctAnswer=  8
    attempts = 0
    print("WELCOME TO THE GUESSING GAME")
    print("Please type in a number betwen 1 and 10")
    userGuess = int(input("Please type in a number: "))
    while userGuess != correctAnswer:
        print("Sorry, incorrect. Guess again.")
        attempts+= 1 
        print(attempts)
        userGuess =int(input("please try another number: "))
        print("Congrats! you guessed correctly. game over")
 
# guessingGame()






# Question 1
# password reset function. Your function should take in a 
# user password as an input. within the function there should be a 
# variable that contains the correct password.
# the user should be able to attempt to enter the password 4 times. 
# On the fourth attempt of getting the password inccorect, 
# it should print out a message telling the user that 
# their account has been locked. If the user gets the password 
# correct it should print out a message telling them 
# they can access their account.


def pwReset():
    correctPw = '123abc'
    attempts = 4

    print("Welcome please enter your login password: ")
    userPw = input()

    while userPw != correctPw and attempts > 0:
        print("sorry incorrect pw")
        print("please try again")
        attempts -= 1
        print("number of attempts left: " + str(attempts))
        userPw = input("please try again")

    print(" you are locked out...")

    print("Welcome you have access...")

pwReset()

  





































