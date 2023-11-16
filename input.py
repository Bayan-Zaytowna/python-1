# Function to perform the calculation
def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':

        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

num1 = float(input("Enter the first number: "))

operator = input("Enter the operation (+, -, *, /): ")


num2 = float(input("Enter the second number: "))

result = calculate(num1, operator, num2)

print(f"The result of {num1} {operator} {num2} is: {result}")


