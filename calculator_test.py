def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
user_operator = input("Enter the operator: ")
match user_operator:
    case '+':
        print("Sum of two numers: ", addition(num1, num2))
    case '-':
        print("Sum of two numers: ", subtraction(num1, num2))
    case '*':
        print("Sum of two numers: ", multiply(num1, num2))
    case '/':
        print("Sum of two numers: ", division(num1, num2))
    case _:
        print("No valid operator provided")


