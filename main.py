# 🍽️ Python Restaurant Ordering System

menu = {
    "Pizza": 249,
    "Burger": 149,
    "Pasta": 199,
    "French Fries": 99,
    "Sandwich": 129,
    "Garlic Bread": 159,
    "Coffee": 79,
    "Cold Coffee": 119,
    "Tea": 49,
    "Ice Cream": 79
}

print("🍽️✨ Welcome to Python Restaurant ✨🍽️")
print("\n-------- 🧾 Today’s Menu 🧾 --------\n")

for item, price in menu.items():
    print(f"🍕 {item:<15} : ₹{price}")

print("\n-----------------------------------\n")

order_total = 0
ordered_items = []  # to store all ordered items

while True:
    item_name = input("📝 Enter the name of the item you want to order: ").strip()

    formatted_item = item_name.title()

    if formatted_item in menu:
        price = menu[formatted_item]
        order_total += price
        ordered_items.append((formatted_item, price))
        print(f"✅ {formatted_item} added to your order. (₹{price})\n")
    else:
        print("⚠️ Invalid item! Please choose from the menu.\n")

    while True:
        another_order = input("➕ Do you want to add another item? (yes/no): ").strip().lower()
        if another_order == "yes":
            print()
            break
        elif another_order == "no":
            print("\n🧾 Generating your bill...\n")
            break
        else:
            print("⚠️ Invalid input! Please type 'yes' or 'no' only.\n")

    if another_order == "no":
        break

# Final summary
print("---------- 🧺 Order Summary 🧺 ----------\n")

if ordered_items:
    for name, price in ordered_items:
        print(f"✅ {name:<15} : ₹{price}")
    print("\n💰 Total Amount to Pay: ₹", order_total)
else:
    print("🛒 No items were ordered.")

print("\n🙏 Thank you for visiting Python Restaurant! Come again 😄")
print("-----------------------------------------------")
