# This is a simple arithmetic calculator app
num1 = int(input("Enter first number: "))

operator = input("Enter an arithmetic operator [+,-,/,* or %]: ")

num2 = int(input("Enter a second number: "))

if operator == "+":
    print(f"{num1}+{num2} = {num1+num2}")
elif operator == "-":
    print(f"{num1}-{num2} = {num1-num2}")
elif operator == "/":
    print(f"{num1} divided by {num2} = {num1/num2}")
elif operator == "*":
    print(f"{num1} multiplied by {num2} = {num1*num2}")
elif operator == "%":
    print(f"{num1} modulus {num2} = {num1%num2}")
else: 
    print(f"Please enter a valid operator")