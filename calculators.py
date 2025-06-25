#basic calculator 
a = float(input("Enter First Number:"))
b =float(input("Enter Second Number:"))
op = input("Enter Operator:")
if op == '+':
    result= a + b
elif op == '-':
    result = a- b
elif op == '*':
    result = a*b
elif op == '/':
    if b != 0:
        result = a/b
    else:
        result = 'Not Divisible'   
else:
    result = "Invalid Operator"
print(f"{a}{op}{b}= {result}") 




#discount calculator 
'''a = float(input("Enter First Number:"))
b =float(input("Enter Second Number:"))
op = input("Enter Operator:")
if op == '+':
    result= a + b
elif op == '-':
    result = a- b
elif op == '*':
    result = a*b
elif op == '/':
    if b != 0:
        result = a/b
    else:
        result = 'Not Divisible'   
else:
    result = "Invalid Operator"
print(f"{a}{op}{b}= {result}")'''



