# Interview Questions: Loops

## Core concepts

- `for` loop and `while` loop
- `range()` and iteration
- `break`, `continue`, and `pass`
- Nested loops
- Loop optimization and enumeration

## Frequently asked interview questions with answers

### 1. What is the difference between a `for` loop and a `while` loop?

Answer: A `for` loop is used when you know the number of iterations or are iterating over a sequence. A `while` loop runs as long as a condition is true.

### 2. What is `range()` used for?

Answer: `range()` generates a sequence of numbers, commonly used in `for` loops to repeat code a fixed number of times.

### 3. What is the role of `break` and `continue`?

Answer: `break` exits the loop completely. `continue` skips the remaining code in the current iteration and moves to the next iteration.

### 4. Why do infinite loops happen?

Answer: Infinite loops happen when the loop condition never becomes false, often because the variable controlling it is not updated correctly.

### 5. What is `enumerate()`?

Answer: `enumerate()` gives both the index and the value while iterating. It is cleaner than using `range(len(...))` in many cases.

### 6. How do you iterate over a dictionary?

Answer: You can iterate over `.keys()`, `.values()`, or `.items()`. For example, `for key, value in dict.items():` is the most common pattern.

## Quick viva tasks

- Print the Fibonacci series using a loop.
- Find the average of numbers in a list.
- Use `enumerate()` to print index and value together.
