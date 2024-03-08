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
def resource_check(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] >= resources[item]:
         print(f"Not enough {item}")
         machine_on() 
    return


def process_coins():
    print("Please Insert Change")
    total = int(input("Quarters: ")) * .25
    total += int(input("Dimes: ")) * .10
    total += int(input("Nickels: ")) * .02
    total += int(input("Pennies: ")) * .01
    return total


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
    for item in MENU[coffee]['ingredients']:
        resources[item] = resources[item] - MENU[coffee]['ingredients'][item]
    print(f"Here is your {coffee}!")


def machine_on():

    coffee = input("What would you like to make? Expresso/Latte/Cappucino: ").lower()

    if coffee == 'report':
        print(resources)
        machine_on()
    if coffee == 'off':
        return

    resource_check(MENU[coffee]['ingredients'])

    change = process_coins()
    
    check_transaction(change, coffee)
    
    make_coffee(coffee)

    machine_on()

machine_on()