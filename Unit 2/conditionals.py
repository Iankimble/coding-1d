# Conditional if/else logic- these are keywords that instruct your 
# program to do specific instructions based on specific data 
# or conditions

# condititional syntax (how it is written)
def changeMaker():
    bill_amount = int(input("Please type in a bill tender (1s ,5s, or 10s): "))
# if usually indicates that something is a possible option
    if bill_amount == 1:
        print("Here are 4 quarters")
# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
    elif bill_amount == 5:
        print("here are 20 quarters")
    elif bill_amount == 10:
        print("here are 40 quarters")
    elif bill_amount == 20:
        print("sorry we dont accept 20s.")
# else is ALWAYS your last option. 
    else:
        print("Sorry that type of bill is not accepted.")

# Using the calaulator functions from the calculator.py file,
# Create a main calculator function that uses if/else logic to 
# allow the user to select different arithmetic operations and 
# then perform those operations by running their respective functions. 

# Example: an input where if the user enter 1, it will run the addition function.
# 1= addition()
# 2= subtaction()
# 3= multiplication() 
# 4= division()

def calculate_add():
    print("Program has started: please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print( num1 + num2) 
    print("Program has ended. ")

def calculate_subtract():
    print("Program has started: please type in 2 numbers to subtract ")
    num1 = int(input())
    num2 = int(input())
    print( num1 - num2) 
    print("Program has ended. ")

def calculate_multiply():
    print("Program has started: please type in 2 numbers to multiply ")
    num1 = int(input())
    num2 = int(input())
    print( num1 * num2) 
    print("Program has ended. ")

def calculate_division():
    print("Program has started: please type in 2 numbers to divide ")
    num1 = int(input())
    num2 = int(input())
    print( num1 / num2) 
    print("Program has ended. ")

def mainCalculator():
    print("main calculator is running... ")
    selection = int(input())
    if selection == 1:
        calculate_add()
    elif selection == 2:
        calculate_subtract()
    elif selection == 3:
        calculate_multiply()
    elif selection == 4:
        calculate_division()
    else:
        print("sorry I dont understand your selection")

#mainCalculator()


# 7 and younger = 8.00
# 8 to 20 = 12.00
# 21 to 60 = 20.00
# 61 and older = free/ 0.00

def ticketPrices():
    print("welcome to the movies. Please type in your age: ")
    age = int(input())
    if age<= 2:
        print("Dont bring that baby in here.")
    elif age <= 7: 
        print("your ticket is $8.00")
    elif age >= 8 and age<= 20:
        print("your ticket $12.00")
    elif age >= 21 and age<= 60:
        print("your ticket $20.00")
    elif age >= 61:
        print("your ticket is free")
    else:
        print("Error. something went wrong.")

ticketPrices()



