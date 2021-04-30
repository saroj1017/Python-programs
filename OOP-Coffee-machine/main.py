"Complete control of other class models"


#importing the respective class where they perform the required task
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating objects of those classes to be worked upon 
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# Looping through to ask the user if he wants another drink or to switch off
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    # To close the machine 
    if choice == "off":
        is_on = False
    
    # To get the details of the machine at any point of time we use choice as report
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        
    # if the user selects any of the coffee type then the required process
    #happens based on the availability of resources and coin received
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
