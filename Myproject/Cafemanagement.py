menu ={
    'Pizza': 40,
    'Pasta': 50,
    'Samosa': 20,
    'French Fries': 30,
    'Burger': 60,
    'Coffee': 80,
    'Cold Coffee': 90,
    'Milk shake': 70,
    'Icecream': 10,
    'Chocolate': 5,
}

print("Welcome to SACHIN'S COFFEE POINT")
print("Pizza: Rs40\nPasta: Rs50\nSamosa: Rs20\nFrench Fries: Rs30\nBurger: Rs60\nCoffee: Rs80\nCold Coffee: Rs90\nMilk shake: Rs70\nIcecream: Rs10\nChocolate: Rs05\n")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been addedto your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to order another item?")
if another_order == "Yes":
    item_2 = input("Enter thename of second item= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount of item to pay is {order_total}")