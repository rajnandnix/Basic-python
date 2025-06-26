#inventory system using dictionaries and lists to take input from user for adding and deleting things from store
inventory ={}
def add_item():
    item_name = input("Enter the item name: ").strip()
    if item_name in inventory:
        print(f"{item_name} already exists in the inventory.")
    else:
        quantity = int(input(f"Enter the quantity of {item_name}: "))
        inventory[item_name] = quantity
        print(f"{item_name} added with quantity {quantity}.")
def update_item():
    item_name = input("Enter the item name to update: ").strip()
    if item_name in inventory:
        quantity = int(input(f"Enter the new quantity for {item_name}: "))
        inventory[item_name] = quantity
        print(f"{item_name} updated with new quantity {quantity}.")
    else:
        print(f"{item_name} does not exist in the inventory.")
def display_inventory():
    if inventory:
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    else:
        print("Inventory is empty.")
#calling def add, def update, def display
while True:
    print("\nInventory System")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Display Inventory")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_item()
    elif choice == '2':
        update_item()
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        print("Exiting the inventory system.")
        break
    else:
        print("Invalid choice, please try again.")
