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

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.



profit = 0

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def check_resources(drink_ingredients):
    for item, amount in drink_ingredients.items():
        if resources[item] < amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies

def make_coffee(drink_name, drink_ingredients):
    for item, amount in drink_ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")

def coffee_machine():
    global profit
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Shutting down the coffee machine...")
            break
        elif choice == "report":
            print_report()
        elif choice in MENU:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                payment = process_coins()
                if payment < drink["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    change = round(payment - drink["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    profit += drink["cost"]
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid input. Please select a valid option.")

coffee_machine()







