def add(a,b):
    return a+ b

def sub(a,b):
    return a- b

def mul(a,b):
    return a* b

def dev(a,b):
    if b != 0:
     return a/ b
    else:
        return "Division by zero not allowed"
    
while True:
    print("/n Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 3:
        print("Exit Program")
        break
    num1 = float(input("Enter First number: "))
    num2 = float(input("Enter Second number: "))
    
    if choice == 1:
        print("Result: ",add(num1, num2))
    elif choice == 2:
        print("Result: ",sub(num1, num2))
        