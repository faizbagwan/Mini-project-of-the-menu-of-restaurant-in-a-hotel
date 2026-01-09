

# Define the menu of restaurant in a hotel
menu = {
    "Pizza": 100,
    "Burger": 80,
    "Pasta": 120,
    "Salad": 60
}

# Greet the customer
print("Welcome to our Hotel Restaurant!")
print("Pizza : Rs.100\nBurger : Rs.80\nPasta : Rs.120\nSalad : Rs.60")

order_total = 0

# First order
item_1 = input("Enter the name of the first item you want to order: ")

# Normalize input (so 'pizza' or 'PIZZA' still works)
item_1 = item_1.capitalize()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Current total: Rs.{order_total}")
else:
    print(f"Sorry, we don't have {item_1} on the menu.")

# Ask if they want another order
another_order = input("Do you want to order another item? (yes/no): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item you want to order: ")
    item_2 = item_2.capitalize()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} added to your order. Current total: Rs.{order_total}")
    else:
        print(f"Sorry, we don't have {item_2} on the menu.")

print(f"Your final order total is: Rs.{order_total}")

#this code is written by me.
#hi
#hello
