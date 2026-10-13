# Conditional logic- these are keywords that instruct your 
# program to do specific instructions based on specific data 
# or conditions

# condititional syntax
def college():
    grade=  int(input("please type in your grade: "))
    if grade > 90:
        templeUApp()
    else:
        ccpApp()

def ccpApp():
    print("congrats please complete the community college app with the following code")
    print("238293")

def templeUApp():
    print("congrats please complete the templa u app with the following code")
    print("a7ds78sd") 

college()

# we can use multiple if statements by using the elif keyword. 
# this allows us to have multiple program outcomes

def gtavEnding():
    characterDeath = input("who are you taking out: ")
    selection= input("press 1 for trevor, 2 for michael")
    if selection == 1:
        death_wish_mission_trevor()
    elif selection ==2:
        death_wish_mission_michael()
    elif:
        secret_ending_good()
    elif:
        secret_ending_bad()
    else:
        death_wish_mission_default()


