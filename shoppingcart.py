#shopping cart with dscount above $100
cart = {} #empty dictionary to store item names and prices
total = 0
print("Welcome to Simple Shopping Cart!")
print("Add items one at a time. Type 'done' when finished.\n")
while True:
    item= input("Enter items:\n")
    if item.lower() == 'done': #ifser types done the loop exits 
        break
    price =float(input(f"enter price of the {item}=$")) #converts into float value
    cart [item] = price#stores items and price in cart dictonary
    total += price
    
if total > 100:#prints Lists all items and their prices
    discount = total*0.10
    final_total= total-discount
    for item, price in cart.items():
        print(f"{item}= ${price:.2f}")   
    print(f"Total= ${total:.2f}")
    print(f"Discount=${discount:.2f}")
    print(f"Final total= ${final_total:.2f}")
else:
    for item, price in cart.items():
        print(f"{item}=${price:.2f}")
    print(f"\nTotal={total:.2f} (No Discount Applied)")
    