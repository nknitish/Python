# Scope in Python
# Python follows LEGB rule:
# L - Local
# E - Enclosing
# G - Global
# B - Built-in

# ------------------
# 1. Global Scope
# ------------------

value = "global value"

print("Before function call:", value)


def update_global():
    global value
    value = "updated from inside function"
    print("Inside function:", value)


update_global()
print("After function call:", value)

# ------------------
# 2. Nonlocal Scope
# ------------------

print("\nNonlocal example:")


def outer():
    number = 10

    def inner():
        nonlocal number
        number += 5
        print("Inside inner:", number)

    inner()
    print("Inside outer:", number)


outer()

# ------------------
# 3. LEGB Scope Rule
# ------------------

print("\nLEGB example:")

msg = "global message"


def outer_function():
    msg = "enclosing message"

    def inner_function():
        msg = "local message"
        print("Local variable:", msg)

    inner_function()
    print("Enclosing variable:", msg)


outer_function()
print("Global variable:", msg)

# ------------------
# 4. Closure Example using nonlocal
# ------------------

print("\nClosure example:")


def make_counter(start):
    count = start

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


counter = make_counter(10)
print(counter())
print(counter())
print(counter())

# Explanation:
# - Global variables are defined outside any function.
# - Nonlocal variables belong to the enclosing function.
# - LEGB tells Python where to look for a name: Local, Enclosing, Global, Built-in.
# - A closure remembers variables from its outer scope.
