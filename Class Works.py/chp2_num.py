#Prompt the user to enter their name
name = input("Enter your name: ")
# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Perform arithmetic operations
addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2
# Check if num2 is not zero to avoid division by zero error
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Undefined (division by zero)"