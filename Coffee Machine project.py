
MENU = {"espresso": {"ingredients": {"water": 50,"coffee": 18,},"cost": 1.5,},
    "latte": {"ingredients": {"water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino": {"ingredients": { "water": 250,"milk": 100,"coffee": 24, },"cost": 3.0,}
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def print_resources():
    print("\nHere is your resources:\n")
    for key in resources:
        print(f"{key}: {resources[key]}")

def process_coins(user):
    print(f"Please Insert the required coins {MENU[user]['cost']}")
    quarters = float(input("No.of of quarters : "))
    dimes = float(input("No.of of dimes : "))
    nickles = float(input("No.of of nickles : "))
    pennys = float(input("No.of of pennies : "))
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennys*0.01

    if total < MENU[user]['cost']:
        print(f"Sorry , Need more for {user}. Money Refunded !")
        return
    elif total >= MENU[user]['cost']:
        diff = total - MENU[user]['cost']
        if diff == 0:
            print("You have paid successfully.")
        else:
            print("You have paid Successfully , Here is the change - ", diff)
    else:
        print("\n.......... Invalid Error ............\n")
    return

def resource_check(user):
    if user != "espresso":
        if MENU[user]["ingredients"]['milk'] > resources['milk']:
            print(f"Sorry , Insufficient milk for {user}")
            next_1 = False
    if MENU[user]["ingredients"]['water'] > resources['water']:

        print(f"Sorry , Insufficient water for {user}")
        next_1 = False
    elif MENU[user]["ingredients"]['coffee'] > resources['coffee']:

        print(f"Sorry , Insufficient coffee for {user}")
        next_1 = False
    else:
        next_1 = True
    return next_1
next_1 = True
while next_1:
    user_input = input("What would you like?(Espresso, Latte, Cappuccino): ").lower()
    if user_input == "report":
        print_resources()
    if user_input == "off":
        print("\nSwitching off\n")
        next_1 = False
    elif user_input == "espresso":
        next_1 = resource_check("espresso")
        if next_1:
            process_coins("espresso")
    elif user_input == "latte":
        next_1 = resource_check("latte")
        if next_1:
            process_coins("latte")
    elif user_input == "cappuccino":
        next_1 = resource_check("cappuccino")
        if next_1:
            process_coins("cappuccino")
    else:
        print("Sorry , Incorrect Input !")

    if next_1:
        resources['water'] -= MENU[user_input]["ingredients"]['water']
        resources['coffee'] -= MENU[user_input]["ingredients"]['coffee']
        if user_input != "espresso":
            resources['milk'] -= MENU[user_input]["ingredients"]['milk']

        print("Your coffee has been served. Enjoy it !\n")
        print("Remaining resources:\n")
        print_resources()

