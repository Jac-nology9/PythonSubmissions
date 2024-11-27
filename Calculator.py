
# Ask the user to input two numbers
numA = float(input("Enter the first number: "))
numB = float(input("Enter the second number: "))

# Ask the user to choose a mathematical operation
operation = input("Choose your operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == "+":
    result = numA + numB
    print(f"{numA} + {numB} = {result}")
elif operation == "-":
    result = numA - numB
    print(f"{numA} - {numB} = {result}")
elif operation == "*":
    result = numA * numB
    print(f"{numA} * {numB} = {result}")
elif operation == "/":
    if numB != 0:
        result = numA / numB
        print(f"{numA} / {numB} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from these --> +, -, *, or /.")

