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



is_on = True
profit = 0

# (2)                     {'water': 200, 'milk': 150, 'coffee': 24}
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are sufficient4"""
    is_enough = True
#Looping through each key in drink[ingredients which is = order_ingredients-> {'water': 200, 'milk': 150, 'coffee': 24}
    for item in order_ingredients:


#                                           {  "water": 300,"milk": 200, "coffee": 100,}
#                                              👆             👆             👆
#Getting hold of the key   || If the value >= resources[keys in resources]
#E.G       dictionary['water']=200 VAL >=     resources['water] = 300
        if order_ingredients[item] >= resources[item]:

#                                                   'water'
            print(f"Sorry there is not enough water{item}.")
            return False
    return is_enough



def process_coins():
    '''Returns total cal from inserted coins'''
    print("Please insert coins.")

    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the arguement is accepted or False if money is insufficient."""

    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return  True
    else:
        print("Sorry that's not enough money. Money refunded")

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")

while is_on :
    choice = input("What would you like?: (espresso/ latte / cappuccino)").lower()
    if choice == "off":
        is_on = False

    elif choice == "report":
# value = dictionary['key']
        print(f"Water:{resources['water']} ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
#      variable dictionary    key

#               MENU[input(.....)]
        drink = MENU[choice]
#(1)This is being passed over on (2) because we didn't define order_ingredients
        if is_resource_sufficient(drink["ingredients"]) :# drink["ingredients"] = {'water': 200, 'milk': 150, 'coffee': 24}
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])






