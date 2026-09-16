# Generators and Decorators in Python
# Generators are functions that yield values one at a time.
# Decorators are functions that modify another function.

# ------------------
# Generator Example
# ------------------

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("Generator example:")
for value in countdown(5):
    print(value)

# A generator does not store all values in memory at once.
# It produces values one by one when needed.

# ------------------
# Decorator Example
# ------------------

def decorate_message(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@decorate_message
def say_hello():
    print("Hello from the function")

print("\nDecorator example:")
say_hello()

# Explanation:
# - A decorator takes a function as input.
# - It adds extra behavior before and after the original function.
# - The @decorate_message syntax is a shortcut for calling the decorator.

# ------------------
# Another generator example using range-like behavior
# ------------------

def squares(limit):
    for i in range(1, limit + 1):
        yield i * i

print("\nSquares generator:")
for num in squares(5):
    print(num)

# Notes:
# - Generators are memory efficient.
# - Decorators help modify function behavior without changing the function body.
