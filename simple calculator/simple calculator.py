# simple calculator

operator = input("enter an operator, ( + - * / ): ")

num5 = float(input("enter 1st number: "))
num6 = float(input("enter 2nd number: "))

if operator == "+":
    result = num5 + num6
    print(f"{num5} + {num6} = {round(result, 2)}")   
elif operator == "-":
    result = num5 - num6
    print(f"{num5} - {num6} = {round(result, 2)}")
elif operator == "*":
    result = num5 * num6
    print(f"{num5} * {num6} = {round(result, 2)}")
elif operator == "/":
    result = num5 / num6
    print(f"{num5} / {num6} = {round(result, 2)}")
else:
    print(f"{operator} is not a valid operator")