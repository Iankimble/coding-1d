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
def check_Water_Depth(depth):
    print(depth)
    print(depth > 10) # true if depth is greater than 10 feet
    # return depth

# Function Arguments- This is the REAL DATA that we pass into
# the function call. 
# memory trick- if you make a REAL world argument with a person
# you need to come with REAL facts (data)
check_Water_Depth(3)
