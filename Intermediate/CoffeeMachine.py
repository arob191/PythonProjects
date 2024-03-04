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


# TODO: Prompt User "What would you like to Make?"

coffee = input("What would you like to make? Expressor/Latte/Cappucino: ").lower()

# TODO: Turn coffee machine off by entering the "off" prompt
# There will be a "return" line at the end of the coffee function

# TODO: Print the report if requested

def report():
    print(resources)

globals()[coffee]()

# TODO: Check Resource Sufficiency

# TODO: Process Coins

# TODO: Check if transaction is successful

# TODO: Make Coffee