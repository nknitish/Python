# Interview Questions: Conditional Expressions and Exception Handling

## Core concepts

- `if`, `elif`, and `else`
- Nested conditions
- Ternary operators
- `try`, `except`, `finally`
- Error handling and exception flow

## Frequently asked interview questions with answers

### 1. What is the purpose of `if`, `elif`, and `else`?

Answer: They allow a program to make decisions based on conditions. `elif` checks additional conditions when the earlier ones are false.

### 2. What is a ternary operator?

Answer: It is a compact conditional expression. Example: `result = "Even" if num % 2 == 0 else "Odd"`.

### 3. What is the difference between a syntax error and a runtime error?

Answer: A syntax error happens when code is invalid. A runtime error occurs when the program runs and something unexpected happens, such as division by zero.

### 4. Why do we use `try` and `except`?

Answer: They help handle errors gracefully without crashing the program. This is especially useful when reading user input or files.

### 5. What is `finally` used for?

Answer: `finally` always runs after `try`/`except`, whether or not an exception occurs. It is commonly used for cleanup tasks.

### 6. What is the difference between `ValueError` and `TypeError`?

Answer: `ValueError` means the value is the wrong type but the type is correct. `TypeError` means the operation is being performed on an incompatible type.

## Quick viva tasks

- Write a program to check if a number is positive, negative, or zero.
- Validate user age input and raise an error for invalid values.
- Explain the flow of `try`, `except`, and `finally` with a real example.
