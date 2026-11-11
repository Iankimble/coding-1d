# What is a Loops --> Code thats repeats.  

# While loops = a block code that repeats itself until the triggering
# condition is no longer TRUE. CAN BE INFINITE

# For loops = a type of loop (code block that repeats itself) BUT  
# it only repeats itself upto a certain number of times.
# IT IS FINITE

# THINK OF FOR LOOPS AS THE COUNTING LOOP = for --> 4 = number of loop

# FOR LOOP SYNTAX
# i stand for itertator = programmers decided make this the universal
# symbol for a placeholder for counting

for i in range(1, 5):
    print(i)

for i in "school": 
    print(i)

# LIST --> A collection type that acts as a container for
# multiple data types and pieces of data.

# List Syntax 
# A list is written like a variable BUT after the equal assignment 
# symbol we use SQUARE BRACKETS and put all of the datas inside of 
# them.
 
fooditem1= "popcorn" # we can only store 1 piece of data in 1 variable

groceryList = ["popcorn", "apples", "water", "chips", "fish", "celery"]
print(groceryList)

for groceryItem in groceryList:
    print("I need to buy " + str(groceryItem))

itemPrices = [10.00, 20.00, 13.25, 7.95, 349.00]
tax = 0.07
 
for i in itemPrices:
    # I want to know how much in taxes i need to pay on each item
    print(tax * i)

semesterGrades = [90, 100, 78, 76, 74, 82, 84]

for i in semesterGrades:
    # I want to find ALL the grades lower than 85.
    if i < 85:
        print(i)


# List are collection types for storing multiple pieces of data
# Key elements and purpsoses for lists: 
# Lists are organized and structured
# Lists can be manipulated and modified - mutable (means changable)
# Lists items are accessible and useable 

# When we want access an item in a list we use the indexing system
# every item in a list is numbered. 
# a list index always starts at zero (0)

inventory= ["sword","shield","healing potion","armor"]

print(inventory[0]) # indicated im going to first position in the list

# When we want add an item to our list, we use the append() method
inventory.append("knife")
print(inventory)

# Use a method to remove the "healing potion" from the list
inventory.remove("healing potion")
# inventory.pop(2)
print(inventory)

# use a method to add a "war hammer" to the end of the list
inventory.append("war hammer")

# Use a method to add a new "healing potion" to index 4 of the list
inventory.insert(4,"healing potion")







































# # Lists - Containers that allows us to store multiple pieces of data
# # (data types, variables, other lists, etc)

# # Lists keep our data structured and organized

# drinks = []
# sandwichs = []
# soups = []
# wawa_kisosk = drinks, sandwichs, soups

# # When select an item, we use the indexing system of a list
# inventory = [ "weapon","healing kit","armor","grenade" ]

# # lists are 0 based indexing systems, MEANING- the first item
# # in a list starts with 0. 
# print(inventory[0])

# # Lists are also changable and manipulatable (mutable)

# # when we want to add items we use the append() method

# inventory.append("knife")  
# print(inventory)

# # Remove an item from a list, specifically remove the 
# # healing kit from the list

# inventory.remove("healing kit")
# # inventory.pop(1)
# # print(inventory)

# # Add a new healing kit to the list, specifically at index 3
# inventory.insert(3,"healing kit")
# print(inventory)






























# book_1 = "math"
# book_2 = "social studies"

# book_for_school = book_2, book_1

# # lists are collection types for us to store multiple peieces of
# # data in one location

# # one benefit of using lists is that they can be manipulated 
# # (change/mutable)

# # we use list methods to modify our lists 

# inventory = ["weapons", "healing potion", "sheild", "armor"]

# # When we want to add an item to a list we use the append() method
# inventory.append("spell book")
# print(inventory)

# # List are index based- meaning we can search and find values inside of
# # list because it structured 

# # To pull a specific value from a list, use the list index position
# # lists always start from 0. 
# print(inventory[0])

# # Find the method for removing an item from a list- specifically, 
# # remove the healing potion

# inventory.remove("healing potion")
# inventory.pop(1)

# print(inventory)

# # How do we add the healing potion back to our inventory 
# # list-specifically at index 3
# inventory.insert(3, "healing potion")




















# lists are usually used to keep track of specific data that can be 
# pull for specific cases 
# This is primarily and ORGANIZATION Tool
# char_inventory = ["weapons", "healing food", "sheild", "armor"] 

# when we want to access an itme in a list we use indexing
# meaning = each item is numbered starting from 0 and goes the 
# length of the list

# print(char_inventory[0]) # the first item in the list

# When want to add an item to a list we use the append() function
# char_inventory.append("spell book")
# print(char_inventory)


# which method would you use to remove an item from a list
# char_inventory.pop(1)
# print(char_inventory)

# we can also use insert to add items to a list. the key difference 
# with insert is that we can specificy where we want to put the item

# insert the healing food at index 3
# print(char_inventory.insert(3, "healing food"))

# which method would you use to change the value of an item on a list
# we want to change the value weapon into sword


