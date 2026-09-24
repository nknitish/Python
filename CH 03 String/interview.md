# Interview Questions: Strings

## Core concepts

- String creation and indexing
- Slicing and substring extraction
- String methods
- Immutability of strings
- Escape sequences and formatting

## Frequently asked interview questions with answers

### 1. Is a string mutable or immutable?

Answer: Strings are immutable. Once a string is created, you cannot change its characters in place. Any operation like `replace()` or concatenation creates a new string.

### 2. What is slicing in Python?

Answer: Slicing extracts a part of the string using indexes like `text[1:5]`. It is very useful for substrings and reversing values.

### 3. What is the difference between `split()` and `join()`?

Answer: `split()` turns a string into a list of parts based on a separator. `join()` combines a list of strings back into one string.

### 4. Why are f-strings preferred?

Answer: f-strings make string formatting cleaner and more readable. Example: `f"Hello {name}"` is easier than `%` formatting or `.format()`.

### 5. How do you remove spaces from both ends of a string?

Answer: Use `.strip()` to remove spaces from both ends. Use `.lstrip()` or `.rstrip()` to remove spaces from one side only.

### 6. How do you check if a string contains a substring?

Answer: Use `in`, such as `if "python" in text:`. This is a simple and commonly used pattern in interviews.

## Quick viva tasks

- Reverse a string without using slicing.
- Count vowels in a sentence.
- Find the longest word in a string.
