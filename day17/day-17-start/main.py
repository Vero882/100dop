# Creating your own class (Instagram example)

class User: # 117. PascalCase is used for class names. 
    # 117. pass # The pass keyword will allow the class to be empty without causing an error.
    # 118. You can also create a class with a constructor method (also called an initializer) that allows you to create objects with attributes in one go.
    def __init__(self, user_id, username): 
        # print("New user being created...") # This will cause this message to be printed every time a new object is created from this class.
        self.id = user_id # 118. Utilizing this method allows you to create objects with attributes at the time of creation.
        self.username = username
        self.followers = 0 # 118. You can also set default values for attributes without requiring them to be passed in.
        self.following = 0 # 119. You can also add methods (function) to a class.

    # 119. You can also add methods (function) to a class.
    def follow(self, user): # Methods always require a self parameter first.
        user.followers += 1 # 119. This method will increase the followers of the user that is being followed.
        self.following += 1 # 119. This method will increase the following of the user that is following another user.

# 117. Even though the class is empty, it can still be used to create objects.
user_1 = User("001", "optimus_prime")

# 117. user_1.id = "001" # You can add attributes to objects after they have been created. Attributes are just variables that belong to an object.
# 117. user_1.username = "optimus_prime"

# print(user_1.username) # You can access object attributes using dot notation.

# Original long-hand method
# 118. This will error out because the class has no attributes that are required by the __init__ method.

# 117. user_2 = User()
# 117. user_2.id = "002"
# 117. user_2.username = "megatron"

# Updated short-hand method for user_2
user_2 = User("002", "megatron")

# print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)