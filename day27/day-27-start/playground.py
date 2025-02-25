# 

def add(*args): # Allows you to pass in any number of positional arguments.
    return sum(args)

# print(add(3, 5, 6, 7, 8, 9))

def calculate(n, **kwargs): # Allows you to pass in any number of keyword arguments as a dictionary.
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5) # You can pass in as many keyword arguments as you like.

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # Using the get method to set a default value (None) if the key does not exist.
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
        