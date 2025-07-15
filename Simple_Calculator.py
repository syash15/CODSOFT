# Simple Calculator

# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display available operations
print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user's choice
choice = input("Enter operation (1/2/3/4): ")

# Perform the selected operation
if choice == '1':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed.")
else:
    print("\nInvalid operation choice.")

# Hold the output window
input("\nPress Enter to exit...")
