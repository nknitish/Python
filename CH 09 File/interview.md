# Interview Questions: File Handling

## Core concepts

- Opening files in different modes
- Reading and writing text files
- `with open()` pattern
- File path handling
- File errors and newline behavior

## Frequently asked interview questions with answers

### 1. How do you open a file in Python?

Answer: Use `open()` and specify a mode such as `'r'` for read, `'w'` for write, or `'a'` for append. The `with` statement is preferred.

### 2. Why is `with open()` recommended?

Answer: It automatically closes the file after the block ends, which prevents resource leaks and file lock issues.

### 3. What is the difference between `'r'`, `'w'`, and `'a'` modes?

Answer: `'r'` reads existing content, `'w'` overwrites the file, and `'a'` appends new content without deleting old data.

### 4. How do you read a file line by line?

Answer: Use a loop like `for line in file:` or call `.readline()`. This is memory efficient for large files.

### 5. How do you handle a missing file?

Answer: Use `try` and `except FileNotFoundError` to handle the error gracefully instead of crashing the program.

### 6. What is the difference between text and binary mode?

Answer: Text mode is used for normal text files and handles encoding automatically. Binary mode is used for non-text files such as images and executable data.

## Quick viva tasks

- Read a text file line by line.
- Write content into a file using `with open()`.
- Handle a missing file using exception handling.
