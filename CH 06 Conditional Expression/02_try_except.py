# Try / Except in Python
# Python uses try and except for error handling.
# This is the Python version of try-catch.

# Example 1: Basic try/except
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# Example 2: Handling division by zero
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Division result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter numeric values only.")


# Example 3: Multiple exceptions
try:
    marks = int(input("Enter your marks: "))
    if marks < 0:
        raise ValueError("Marks cannot be negative.")
    print("Your marks are:", marks)
except ValueError as e:
    print("ValueError:", e)


# Example 4: else and finally
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid age.")
else:
    print("Your age is:", age)
finally:
    print("This always runs.")


# Example 5: Safe program using try/except
try:
    file = open("sample.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program finished.")

# Try/Except is used to prevent the program from crashing when an error occurs.
# It helps us handle errors gracefully and continue the flow of the program.
