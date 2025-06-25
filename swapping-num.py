#swapping two numbers without using a temporary variable 
a = int(input("Enter the first number:"))
b = int(input("Enter second number:"))
print(f"Numbers before swapping: {a},{b}")
a = a+b
b = a-b
a = a-b
print(f"Numbers after swapping: {a},{b}")


#swapping two numbers with using temporray variable
'''a = float(input("Enter the first number:"))
b = float(input("Enter second number:"))
print(f"Numbers before swapping: {a},{b}")
temp = a 
a = b
b = temp
print(f"Numbers after swapping: {a},{b}")'''
