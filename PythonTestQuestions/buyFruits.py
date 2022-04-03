Carts = [{"UserID": "123", "Name": "Mike", "Buy": {"Apple": 1, "Banana": 3}}, {"UserID": "456", "Name": "Linda",
                                                                               "Buy": {"Orange": 2}}]

PriceList = [{"Item": "Apple", "Price": 6}, {"Item": "Banana", "Price": 15}]

UserMoney = {"123": {"Money": 247}}

apple_number = Carts[0]["Buy"]["Apple"]
banana_number = Carts[0]["Buy"]["Banana"]

apple_price = PriceList[0]["Price"]
banana_price = PriceList[1]["Price"]

total_price = apple_number * apple_price + banana_number * banana_price

user_money = UserMoney["123"]["Money"]

print("Fruits total price is " + str(total_price))

print("This user has money " + str(user_money))

if total_price > user_money:
    print("This user can not buy fruits")
else:
    print("This user can buy fruits.")





    