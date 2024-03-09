from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# user_drink = MenuItem()
user_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    choice = input(f"What would you like to make? {user_menu.get_items()}: ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:    
        drink = user_menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)