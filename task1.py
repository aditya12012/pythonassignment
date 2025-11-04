# Task 1: Perform Basic Mathematical Operations

# Step 1: Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform basic mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else None  # Handle division by zero

# Step 3: Display the results
print("\nResults of Mathematical Operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)

if division is not None:
    print("Division:", division)
else:
    print("Division: Undefined (cannot divide by zero)")