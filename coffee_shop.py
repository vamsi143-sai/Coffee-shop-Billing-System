print("====================================")
print("      ☕ WELCOME TO COFFEE SHOP ☕")
print("====================================")

print("\nMENU")
print("1. Espresso      - ₹120")
print("2. Cappuccino    - ₹180")
print("3. Latte         - ₹200")
print("4. Mocha         - ₹220")

choice = int(input("\nEnter your choice (1-4): "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Espresso"
    price = 120
elif choice == 2:
    item = "Cappuccino"
    price = 180
elif choice == 3:
    item = "Latte"
    price = 200
elif choice == 4:
    item = "Mocha"
    price = 220
else:
    print("Invalid choice!")
    exit()

total = price * quantity

print("\n====================================")
print("             BILL")
print("====================================")
print("Item      :", item)
print("Price     : ₹", price)
print("Quantity  :", quantity)
print("------------------------------")
print("Total Bill: ₹", total)
print("====================================")
print("Thank you! Visit Again ☕")
