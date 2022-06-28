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
    "money": 0
}


def res_avail(resources_needed):
    for item in resources_needed:
        if resources_needed[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_trans_successful(amount_paid, cost):
    if amount_paid >= cost:
        change = round(amount_paid - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
profit = 0
is_on = True

while is_on:
    user_selection = input("What would you like? (espresso/latte/cappuccino):")
    if user_selection == "off":
        is_on = False
    elif user_selection == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        coffee = MENU[user_selection]
        if res_avail(coffee["ingredients"]):
            money_paid = process_coins()
            if is_trans_successful(money_paid, coffee["cost"]):
                make_coffee(coffee["ingredients"])
                print(f"Here is your ☕ {user_selection}")




