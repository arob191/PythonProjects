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

#Global functions
def resource_check(coffee):
    if MENU[coffee]['ingredients']['water'] < resources['water'] and MENU[coffee]['ingredients']['milk'] < resources['milk'] and MENU[coffee]['ingredients']['coffee'] < resources['coffee']:
        print("sufficient")
    else:
        print("Not enough resources")
        machine_on()


def process_coins():
    print("Please Insert Change")
    num_of_quarter = float(input("Quarters: "))
    num_of_dimes = float(input("Dimes: "))
    num_of_nickles = float(input("Nickles: "))
    num_of_pennies = float(input("Pennies: "))
    print(f"total = ${num_of_quarter * .25 + num_of_dimes * .10 + num_of_nickles * .05 + num_of_pennies * .01}")
    return num_of_quarter * .25 + num_of_dimes * .10 + num_of_nickles * .05 + num_of_pennies * .01


def check_transaction(change, coffee):
    cost = MENU[coffee]['cost']
    if change >= cost:
        if change - cost == 0:
            print("Exact change thank you")
        else:
            print(f"Here is your change back: ${change - cost}")
    else:
        print(f"Not enough change. Returning: ${change}")
        machine_on()


def make_coffee(coffee):
    resources["milk"] = resources["milk"] - MENU[coffee]['ingredients']['milk']
    resources["water"] = resources["water"] - MENU[coffee]['ingredients']['water']
    resources["coffee"] = resources["coffee"] - MENU[coffee]['ingredients']['coffee']
    print(f"Here is your {coffee}!")


def machine_on():

    coffee = input("What would you like to make? Expressor/Latte/Cappucino: ").lower()

    if coffee == 'report':
        print(resources)
        machine_on()
    if coffee == 'off':
        return

    resource_check(coffee)

    change = process_coins()
    
    check_transaction(change, coffee)
    
    make_coffee(coffee)

    machine_on()

machine_on()

#my controbutions are not showing up properly in GitHub