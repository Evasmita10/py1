#define the menu of restaurant
menu= {
    "Pizza":60,
    "Pasta":100,
    "Noodles":70,
    "Burger":60,
    "Coffee":30,
}

#Greet
print("Hii,Welcome to ROSY BREW !")
print("Pizza: Rs60\nPasta: Rs100\nNoodles: Rs70\nBurger: Rs60\nCoffe: Rs30")

order_total=0

while True:
    item_1=input("Enter item name: ")
    if item_1 in menu:
      order_total+=menu[item_1]
      print(f"your item {item_1} has been added to your order")
    else:
       print(f"item {item_1} is not available!")

    choice=input("Do you want to order anything else?(yes/no): ").lower()

    if choice=="no":
      break

print("---BILL----")
print(f"total amount to pay is Rs.{order_total}")
print("Thank you for visiting our cafe \nyour order will be ready soon!")