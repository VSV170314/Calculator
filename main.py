print("Welcome to the calculator"))
num1 = float(input("Enter your first number: "))
num2 = float(input("enter your second number: "))
operator = input("choose an operator(+ - * /)")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Somthing is not valid")
