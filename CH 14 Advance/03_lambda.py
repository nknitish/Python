# Lambda in Python
# A lambda is a small anonymous function.
# It is useful when we need a quick function for a short task.
# Syntax:
# lambda arguments: expression

# Example 1: simple lambda
square = lambda x: x * x
print("Square of 5:", square(5))

# Example 2: lambda with two arguments
add = lambda a, b: a + b
print("Sum of 3 and 4:", add(3, 4))

# Example 3: using lambda with map()
numbers = [1, 2, 3, 4, 5]
print("Squares:", list(map(lambda x: x * x, numbers)))

# Example 4: using lambda with filter()
print("Even numbers:", list(filter(lambda x: x % 2 == 0, numbers)))

# Example 5: sorting with lambda
names = ["apple", "Banana", "grape", "mango"]
print("Sorted names:", sorted(names, key=lambda x: x.lower()))

# Note:
# lambda is used for short, one-line functions.
# It is not always better than a normal def function.
# Use lambda when the function is simple and temporary.
