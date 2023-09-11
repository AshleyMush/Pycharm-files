class Pet_Blue_Print:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age





#Create object

my_dog = Pet_Blue_Print("Ash", 12)
print( my_dog.get_name(), my_dog.get_age())
my_girl = Pet_Blue_Print("Frankie", 20)

print(my_girl.get_name(), my_girl.get_age())


