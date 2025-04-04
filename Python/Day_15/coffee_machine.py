import menu

# Global variables
money = 0
payment_money = 0

# Check if resources are low
def low_resources():
    if (menu.resources["water"] < min(
            menu.MENU["espresso"]["ingredients"].get("water", 0),
            menu.MENU["latte"]["ingredients"].get("water", 0),
            menu.MENU["cappuccino"]["ingredients"].get("water", 0))):
        print("Sorry, there is not enough water.")
    elif (menu.resources["coffee"] < min(
            menu.MENU["espresso"]["ingredients"].get("coffee", 0),
            menu.MENU["latte"]["ingredients"].get("coffee", 0),
            menu.MENU["cappuccino"]["ingredients"].get("coffee", 0))):
        print("Sorry, there is not enough coffee.")
    elif (menu.resources["milk"] < min(
            menu.MENU["latte"]["ingredients"].get("milk", 0),
            menu.MENU["cappuccino"]["ingredients"].get("milk", 0))):
        print("Sorry, there is not enough milk.")
    coffee_menu()

# Handle coin insertion
def coins_processor():
    print("Please insert payment.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01

    global payment_money
    payment_money = quarters + dimes + nickles + pennies
    print(f"Inserted: ${payment_money:.2f}")

# Process the selected drink
def process_drink(drink_name):
    global payment_money, money

    drink = menu.MENU[drink_name]
    ingredients = drink["ingredients"]
    cost = drink["cost"]

    # Check resource availability
    for item in ingredients:
        if menu.resources[item] < ingredients[item]:
            print(f"Sorry, not enough {item}.")
            coffee_menu()
            return

    coins_processor()

    if payment_money >= cost:
        change = round(payment_money - cost, 2)
        print(f"Here is ${change} in change.")
        print(f"Making {drink_name}...")

        money += cost  # Only add the cost to the money
        for item in ingredients:
            menu.resources[item] -= ingredients[item]

        print("Drink complete.")
    else:
        print("Sorry, that's not enough money. Money refunded.")
    coffee_menu()

# Turn off the machine
def switch_off():
    print("Machine switching off. Bye bye!")
    exit()

# Print resource report
def report():
    print("Resources:")
    print(f" Water: {menu.resources['water']}ml")
    print(f" Milk: {menu.resources['milk']}ml")
    print(f" Coffee: {menu.resources['coffee']}g")
    print(f" Money: ${money:.2f}")
    coffee_menu()

# User selection menu
def coffee_menu():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'espresso':
        process_drink("espresso")
    elif user_choice == 'latte':
        process_drink("latte")
    elif user_choice == 'cappuccino':
        process_drink("cappuccino")
    elif user_choice == 'off':
        switch_off()
    elif user_choice == 'report':
        report()
    else:
        print("Invalid option. Please try again.")
        coffee_menu()

# Start the program
coffee_menu()
