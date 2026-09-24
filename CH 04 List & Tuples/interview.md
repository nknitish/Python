# Interview Questions: Lists and Tuples

## Core concepts

- List creation and indexing
- Slicing and list methods
- List comprehension
- Tuple basics and immutability
- Packing and unpacking

## Frequently asked interview questions with answers

### 1. What is the difference between a list and a tuple?

Answer: A list is mutable and can be changed after creation. A tuple is immutable and is better for fixed collections of values.

### 2. What is list slicing?

Answer: Slicing extracts a subset of a list using indexes, such as `arr[1:4]`. It makes it easy to work with parts of a list.

### 3. What is the difference between `append()` and `extend()`?

Answer: `append()` adds one element as a single item, while `extend()` adds multiple items from another iterable.

### 4. Why is list comprehension useful?

Answer: It gives a short and readable way to create new lists from existing ones, such as `[x for x in nums if x % 2 == 0]`.

### 5. What is tuple unpacking?

Answer: Tuple unpacking assigns values from a tuple to multiple variables in one line, such as `a, b = (10, 20)`.

### 6. What is the main difference between shallow copy and deep copy?

Answer: A shallow copy copies the outer structure, while a deep copy copies nested objects as well. Deep copy is safer when nested data is involved.

## Quick viva tasks

- Find the second largest number in a list.
- Remove duplicates while preserving order.
- Use tuple unpacking to swap two values.
