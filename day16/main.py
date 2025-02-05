from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create initial objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# menu_item = MenuItem()



is_on = True

while is_on:

    user_choice = input(f"What would you like? ({menu.get_items()})): ")

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"Please insert coins: {drink.cost}")
            if money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)
                print(f"Here is your {user_choice}. Enjoy!")
    else:
        print("Invalid selection. Please try again.")