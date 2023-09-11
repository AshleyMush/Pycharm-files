from inventory import MENU, resources


def report(Machine_milk, Machine_water, Machine_coffee):
    '''This function returns the Machine milk, water and coffee, it also prints the balance of ingredients '''

    print(f"You have {Machine_water}water, {Machine_milk} milk, {Machine_coffee} coffee left.")
    return Machine_milk, Machine_water, Machine_coffee


Machine_water = resources["water"]
Machine_milk = resources["milk"]
Machine_coffee = resources["coffee"]

# ACESSING A DICTIONARY IN A DICTIONARY

Espresso_water = MENU["espresso"]["ingredients"]["water"]
Espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]

Latte_water = MENU["latte"]["ingredients"]["water"]
Latte_milk = MENU["latte"]["ingredients"]["milk"]
Latte_coffee = MENU["latte"]["ingredients"]["coffee"]

Cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
Cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
Cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

Cost_espresso = MENU["espresso"]["cost"]
Cost_latte = MENU["latte"]["cost"]
Cost_cappuccinno = MENU["cappuccino"]["cost"]

report(Machine_milk, Machine_water, Machine_coffee)




def power_off():
    """This functions returns nothing and ends the program"""
    print("Powering off")
    return


def user_money(quarters, dimes, nickels, pennies):
    """This function returns the sum of quarters, dimes, nickels and pennies as Deduct a var"""
    Deduction = quarters + dimes + nickels + pennies

    return Deduction

def want_another_coffee(balance):
    '''This function returns takes the user's inputs and returns them too the starting page, turns off, gives a report or exits'''

    another_coffee = input("😊Would you like another coffee?\nType 'y' for Yes or 'n' to exit.").lower()

    if another_coffee == "y":
        print(f"Here's your change ${balance}")

        starting_page()

    elif another_coffee == 'n':
        return "Enjoy your coffee, Bye-bye!"
    elif another_coffee == "report":
        report(Machine_milk, Machine_water, Machine_coffee)

    elif another_coffee == "off":
        power_off()

    else:
        print("Invalid input\nType 'y' for Yes or 'n' to exit.")
        want_another_coffee(balance)


def calculations(coffee_type, quarters, dimes, nickels, pennies):
    """This function takes the coffee type and subtracts the ingredients and money"""

    global Machine_milk, Machine_water, Machine_coffee, Cost_cappuccinno, Cost_latte, Cost_espresso
    balance = 0


#Calculating the cost of the latte and deducting money and ingredients
    if coffee_type == "a":
        if Machine_coffee > Espresso_coffee and Machine_water > Espresso_water :
            if user_money(quarters, dimes, nickels, pennies) > Cost_espresso:
                # Deduction of ingredients
                Machine_water -= Espresso_water
                Machine_coffee -= Espresso_coffee
                # Deduction of money
                balance = user_money(quarters, dimes, nickels, pennies) - Cost_espresso
                # Give coffee
                print(f"{user_money(quarters,dimes, nickels, pennies)} - {Cost_espresso}\nHere's your espresso☕")
                #Option for another coffee
                want_another_coffee(balance)
            else:
                print(f"Insufficient funds. Here's your change {balance}")
        elif Machine_coffee < Espresso_coffee or Machine_water < Espresso_water:
            return f"Please refill water, milk or coffee."


#TODO ADD ELSE STATEMENT "insufficient balance"  to break while loop to all if statements
    elif coffee_type == "b":
        if Machine_coffee > Latte_coffee and Machine_milk > Latte_milk and Machine_water > Latte_water:
            if user_money(quarters, dimes, nickels, pennies) > Cost_latte:
                # Deduction of ingredients
                Machine_water -= Latte_water
                Machine_coffee -= Latte_coffee
                Machine_milk -= Latte_milk
                # Deduction of money
                balance = user_money(quarters, dimes, nickels, pennies) - Cost_latte
                #Give coffee
                print(f"{user_money(quarters,dimes, nickels, pennies)} - {Cost_latte}\nHere's your latte☕")

                # Option for another coffee
                want_another_coffee(balance)


            else:
                print(f"Insufficient funds. Here's your change {balance}")

        elif Machine_coffee < Latte_coffee or Machine_milk < Latte_milk or Machine_water < Latte_water :
            return f"Please refill water, milk or coffee."

    elif coffee_type == "c":
        if Machine_coffee > Cappuccino_coffee and Machine_water > Cappuccino_water and Machine_milk > Cappuccino_milk:
            if user_money(quarters, dimes, nickels, pennies) > Cost_cappuccinno:
                # Deduction of ingredients
                Machine_water -= Cappuccino_water
                Machine_coffee -= Cappuccino_coffee
                Machine_milk -= Cappuccino_milk
                # Deduction of money
                balance = user_money(quarters, dimes, nickels, pennies) - Cost_cappuccinno
                # Give coffee
                print(f"{user_money(quarters,dimes, nickels, pennies)} - {Cost_cappuccinno}\nHere's your cappuccino☕")
                # Option for another coffee
                want_another_coffee(balance)
            else:
                print(f"Insufficient funds. Here's your change {balance}")
        elif Machine_coffee < Cappuccino_coffee or Machine_water < Cappuccino_water or Machine_milk < Cappuccino_milk:
            return f"Please refill water, milk or coffee."


    # elif coffee_type == "report":

    else:
        print("Invalid input")
        starting_page()


def starting_page():
    """This function takes the type of coffee and amount of money and dsiplays cxurrent balance"""
    print(f"😎Welcome to Ashley's coffee machine😎!\nHere's what's on the menu:\nEspresso ${Cost_espresso}\nLatte ${Cost_latte}\nCappuccino ${Cost_cappuccinno}\n ")

    coffee_type =input('What would you like? (A.☕espresso/ B.☕latte / C.☕cappucino)').lower()
    #Powering off option
    if coffee_type == 'off':

        return power_off()
    elif coffee_type == "report":
        return report(Machine_milk, Machine_water, Machine_coffee)

    print(f"Please insert coins:\n")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies =int(input("How many pennies?: ")) * 0.01

    print(f"Your Current Balance💰:${user_money(quarters, dimes, nickels, pennies)}")

    calculations(coffee_type, quarters, dimes, nickels, pennies)


starting_page()
