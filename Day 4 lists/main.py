

fruits=["Strawberries","Nectarines", "Apples", "Grapes", "Peaches","Cherries", "Pears", "Tomatoes"]

vegetables = ["Spinach","Kale","Celery", "Potatoes"]


#We have combined the lists into another list

# this is a list      [this is now 0       this is now 1]
dirty_dozen         =     [fruits   ,        vegetables]

print(dirty_dozen)

#[['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes'], ['Spinach', 'Kale', 'Celery', 'Potatoes']]

print(dirty_dozen[1])

#['Spinach', 'Kale', 'Celery', 'Potatoes']

print(dirty_dozen[1][2]) #This is the 1st list in dirty dozen and the 2nd item in that list

#E.G

'''
this is a list      [this is now 0       this is now 1]
dirty_dozen         =     [fruits   ,        vegetables]


________________________________________
    THIS IS 1
['Spinach', 'Kale', 'Celery', 'Potatoes']
_________________________________________________
   0           1       2         3
['Spinach', 'Kale', 'Celery', 'Potatoes']

THEREFORE  print(dirty_dozen[1][2]) = Celery






'''

print(dirty_dozen[1][3])