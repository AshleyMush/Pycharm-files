# 🚨 Don't change the code below 👇
import  random


row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

'''

Your job is to write a program that allows you to mark a square on the map using a two-digit system. 

The first digit in the input will specify the column (the position on the horizontal axis).

The second digit in the input will specify the row number (the position on the vertical axis). 

So an input of 23 should place an X at the position shown below:


'''

#Write your code below this row 👇


horizontal = int(position[0])

vertical = int(position [1])

selected_row =(map[vertical-1])
selected_row[horizontal-1] = "🏴"





'''

#Change the number into two separate digits

First_value = position_int// 10
Second_value = position_int % 10

)





if First_value >3 or Second_value > 3:
    print("Invalid Co-ordinate.")

else:




    position_on_map = map[Second_value][First_value]






#IMPORTANT


    When the user enter their input e.g, 23
    
    2 is the row to them and 3 is the column
    BUT
    
    It must be flipped over because
                             1                             2                         3        
                      
    map = [row1[0], row1[1],         row2[2],row2[0], row2[1], row2[2],     row3[0], row3[1], row3[2]]
    
    
   


#mark = "🏴‍☠️"




'''


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")