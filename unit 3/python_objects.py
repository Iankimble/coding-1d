# Python objects are digital representations of things
# that can interact with one another

# Objects are collections of data that we use to 
# characterize things

# Example - A car is a object/ "Thing"
# characteristics of a car: engine, tires, battery, seats, 
# color, model, doors

# object Syntax
# when we want to make an object, we need to use a class
# class keyword = object maker

# the class name ALWAYS is capitalized / Pascal Case

# we ALWAYS have to have def __init__(self)
# this code tells the computer how the object works and what it does
# class RaceCar:
#     def __init__(self, tire, ):

        # Attributes - Characteristic data. data used to desribe our
        # object. This can be changed or intereacted with.

        # Methods - Functions (*that exist inside of a object)
        # These functions are designed EXCLUSIVELY for the object
        # they exist in.
        # Methods represent the behavior of the object
  
class TikTokUser:
    def __init__(self, username, email, following, followers):
        self.username = username
        self.email = email
        self.following = following
        self.followers = followers  # fixed spelling

account_1 = TikTokUser("Kimble", "kimble@gmail.com", 10, 10)

print(account_1.username)   # Kimble
print(account_1.followers)  # 10   



# my character object will have several attributes and methods.
# some attributes Im considering for the player character is a speed
# attribute, a health Attribute
# for my methods for this object i would to a attack method 