# Interview Questions: Sets and Dictionaries

## Core concepts

- Dictionary key-value pairs
- Set operations and uniqueness
- Hashing and lookup cost
- Membership checks
- Nested dictionaries and sets

## Frequently asked interview questions with answers

### 1. What is a dictionary in Python?

Answer: A dictionary stores data as key-value pairs. Keys are unique and used to access values quickly.

### 2. What is the difference between a list and a dictionary?

Answer: A list is accessed by index, while a dictionary is accessed by key. Dictionaries are ideal for lookup-based data.

### 3. Why does a set not allow duplicate values?

Answer: A set is based on unique hash values. Duplicate elements are automatically removed because the set tracks each unique item once.

### 4. What is the difference between `dict.get()` and direct indexing?

Answer: `dict[key]` raises a `KeyError` if the key is missing, while `dict.get(key)` returns `None` (or a default value) instead.

### 5. What are `keys()`, `values()`, and `items()`?

Answer: These methods return the dictionary keys, values, and key-value pairs respectively. They are useful when iterating over data.

### 6. How can set operations help in interviews?

Answer: `union`, `intersection`, and `difference` are common operations for comparing datasets or removing duplicates.

## Quick viva tasks

- Count word frequency using a dictionary.
- Remove duplicates from a list using a set.
- Find common elements between two lists using set intersection.
