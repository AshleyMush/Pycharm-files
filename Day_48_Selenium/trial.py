game_is_on = True

money = 0
grandma_price = 100

cursor_price = 15

while game_is_on:
    print("cookie click")
    money += 1
    if money == cursor_price:
        print("bought cursor")
        cursor_price +=2
    if money == grandma_price:
        print("bought_grandma")
        grandma_price +=2


        
    #     print(f" money {money} == cursor price {cursor_price}")
    #
    # print(f" money balance: {money}")