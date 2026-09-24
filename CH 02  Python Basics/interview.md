# Interview Questions: Python Basics

## Core concepts

- Variables and identifiers
- Data types and type conversion
- Operators and precedence
- Input and output
- Mutability vs immutability

## Frequently asked interview questions with answers

### 1. What is the difference between a variable and a constant in Python?

Answer: A variable stores data that can change during execution. Python does not have true constants in the strict sense, but uppercase names like `PI` are treated as constants by convention.

### 2. What is dynamic typing in Python?

Answer: Python does not require you to declare variable types explicitly. The type is assigned at runtime based on the value.

### 3. What is the difference between `==` and `is`?

Answer: `==` compares values, while `is` checks whether two variables point to the same object in memory.

### 4. What are mutable and immutable objects?

Answer: Mutable objects can be changed after creation, such as lists and dictionaries. Immutable objects cannot be changed once created, such as strings, tuples, and integers.

### 5. What is type conversion?

Answer: Type conversion changes one data type into another, such as `int("10")` or `str(5)`. It is useful when reading user input or performing calculations.

### 6. What is the difference between local and global variables?

Answer: A local variable is defined inside a function and is only available there. A global variable is defined outside functions and can be accessed throughout the module.

## Quick viva tasks

- Write a program to swap two numbers without a temporary variable.
- Take user input, convert it to `int`, and validate it.
- Explain the execution order of a mixed expression with arithmetic and comparison operators.
