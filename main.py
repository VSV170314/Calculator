print("Welcome to the Calculator")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Choose an operator (+, -, *, /): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Somthing is wrong")
