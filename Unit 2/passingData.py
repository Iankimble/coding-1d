# When we are building complex programs, we need a 
# way to pass in data that is NOT always 
# from the user. 

# Function arguments and parameters are ways to
#  pass in data to a function from possibly 
# another function. 

# Function Parameters- this is PLACEHOLDER DATA for 
# a function. variables inside the curly brackets

# memory trick - PARAMETER AND PLACEHOLDER BOTH
# START WITH THE LETTER P
def check_Water_Depth(depth, volume, acidic, temparature):
    print(depth)
    print(volume)
    print(acidic)
    print(temparature)
    print(depth > 10) # true if depth is greater than 10 feet
    # return depth

# Function Arguments- This is the REAL DATA that we pass into
# the function call. 
# memory trick- if you make a REAL world argument with a person
# you need to come with REAL facts (data)
# check_Water_Depth(7, 100, False, 78)  

# return - this keyword allows us to pass data from INSIDE 1 function
# into another function

def username():
    name = input("please type in user name: ")
    return name 

def confirmLogin():
    name = username()
    print(name)

# username()
confirmLogin()








# def robloxProfile(username, dob, location, currency, creditCard):
#     print("roblox profile created")
#     print(username, dob, location, currency, creditCard)

# ip= "1293.22.3.23343.23433.45"


# robloxProfile("Kimble", "10/9/100","1992.3383.9283.23",0, "1223-2343-222-233-2332", )
# robloxProfile("Brandon", "10/9/2002","1992.3383.9283.23",0, "1223-2343-222-233-2332", )
# robloxProfile("Ryan", "11/01/1991","1992.3383.9283.23",0, "1223-2343-222-233-2332", )
