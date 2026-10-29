# What is a Loops --> Code thats repeats.  

# While loops = a block code that repeats itself until the triggering
# condition is no longer TRUE. CAN BE INFINITE

# For loops = a type of loop (code block that repeats itself) BUT  
# it only repeats itself upto a certain number of times.
# IT IS FINITE

# THINK OF FOR LOOPS AS THE COUNTING LOOP

# FOR LOOP SYNTAX
# i stand for itertator = programmers decided make this the universal
# symbol for a placeholder for counting

for number in range(1,5):
    print(number / 2)

# LIST --> a collection type that acts as a container for
# multiple data types

foodItem_1 = "apple"

groceryList = ["apples", "oranges","water","chips","ground beef"]

print(groceryList)

for i in groceryList:
    print("I need to buy " + i)

grades = [100, 98, 75, 77, 89, 80]

for grade in grades:
    # Show me the grades lower than 85
    if grade < 85:
        print(grade)

# we can include multiple data types in a list, including
# variable and other lists
fighter_A= ["Johnny Bravo", 100, 50]
fighter_B= ["Dexter Lab", 120, 40]

fighters = [fighter_B, fighter_A]

for fighterName in fighters:
    print("name of fighters: " +str(fighterName[0]))
    print("health of fighters: " +str(fighterName[1]))
























