MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_check(coffee):
    if MENU[coffee]['ingredients']['water'] < resources['water'] and MENU[coffee]['ingredients']['milk'] < resources['milk'] and MENU[coffee]['ingredients']['coffee'] < resources['coffee']:
        print("sufficient")
        return True
    else:
        print("Not enough resources")
        make_coffee()
        return False


def process_coins():
    print("Please Insert Change")
    num_of_quarter = float(input("Quarters: "))
    num_of_dimes = float(input("Dimes: "))
    num_of_nickles = float(input("Nickles: "))
    num_of_pennies = float(input("Pennies: "))
    return num_of_quarter * .25 + num_of_dimes * .10 + num_of_nickles * .05 + num_of_pennies * .01


def report():
    print(resources)


def make_coffee()
    sufficient_resources = True
    # TODO: Prompt User "What would you like to Make?"

    coffee = input("What would you like to make? Expressor/Latte/Cappucino: ").lower()

    # TODO: Turn coffee machine off by entering the "off" prompt
    # There will be a "return" line at the end of the coffee function

    # TODO: Print the report if requested

    if coffee == 'report':
        globals()[coffee]()

    # TODO: Check Resource Sufficiency when making coffee

    sufficient_resources = resource_check(coffee)

    # TODO: Process Coins

    change = process_coins()
    print(change)

    # TODO: Check if transaction is successful

    if 

    # TODO: Make Coffee