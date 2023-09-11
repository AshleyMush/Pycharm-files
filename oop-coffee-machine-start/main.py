import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



"""
class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Accessing object attributes What it has
print(student1.name)  # Output: Alice
print(student2.age)   # Output: 22

# Calling object methods What it does
student1.display_info()  # Output: Name: Alice, Age: 20
student2.display_info()  # Output: Name: Bob, Age: 22

"""
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
