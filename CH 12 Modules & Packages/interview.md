# Interview Questions: Modules and Packages

## Core concepts

- Python modules
- Package structure
- Relative and absolute imports
- `__init__.py`
- Package management and `requirements.txt`

## Frequently asked interview questions with answers

### 1. What is a module in Python?

Answer: A module is a Python file containing reusable code such as variables, functions, and classes.

### 2. What is a package?

Answer: A package is a directory that groups related modules together. It usually contains an `__init__.py` file.

### 3. Why is `__init__.py` important?

Answer: It marks a directory as a Python package, allowing it to be imported like a normal module namespace.

### 4. What is the difference between absolute and relative imports?

Answer: Absolute import uses the full package path, while relative import uses the current package context, like `from .utils import calc`.

### 5. Why do large projects use packages?

Answer: Packages keep code organized, easier to test, and simpler to maintain when the codebase grows.

### 6. What is `requirements.txt` and why does it matter?

Answer: It records project dependencies so another developer or system can install the exact versions needed to run the project.

## Quick viva tasks

- Import a function from another Python file in the same project.
- Create a simple package structure with `__init__.py`.
- Explain the difference between local imports and package imports.
