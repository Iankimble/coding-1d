# PROBLEM #1
# Create a function that will take in 2 inputs and 
# compare them.

# Your inputs should be numbers. 

# The function should compare if the first input is 
# less than the second input
# If it is less than the second input it 
# should print true. If it is not, it should print false.

def compareValue():
    print("PROGRAM RUNNING")
    valA= int(input()) 
    valB= int(input())
    print(valA < valB)

# compareValue()

#PROBLEM #2
# Create a funtion that will compare if a student
# has made honor roll.

# The student should be able to input 2 pieces of data
# the first should be their grade and the second should
# be the number of days they have been absent.

# If the student's grade is above a 90 and the number
# of absenses is less than 5, the program should print
# true, otherwise it should print false.

def honorRollCheck():
    print("PROGRAM RUNNING")
    grade= int(input()) 
    absenses= int(input())
    print(grade > 90 and absenses < 5)

honorRollCheck()























# def honorRollChecker():
#     print("PROGRAM IS RUNNING: please type in your grade: ")
#     grade= int(input())
#     print("please type in your absenses: ")
#     absenses= int(input())
#     print(grade > 90 and absenses < 5)