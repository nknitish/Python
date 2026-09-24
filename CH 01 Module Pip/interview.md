# Interview Questions: Module, Pip, Virtual Environment

## Core concepts

- Python modules and packages
- pip install, upgrade, uninstall
- virtual environments
- requirements.txt
- import path and Python environment

## Frequently asked interview questions with answers

### 1. What is a Python module?

Answer: A module is a single Python file that contains functions, classes, or variables. It helps organize code into reusable pieces. Example: `math`, `os`, or your own `utils.py`.

### 2. What is the difference between a module and a package?

Answer: A module is one file, while a package is a folder with one or more Python files and usually an `__init__.py` file. Packages help group related modules together.

### 3. What is `pip` used for?

Answer: `pip` installs, updates, and removes Python packages from PyPI or other package sources. It is the standard dependency manager for Python.

### 4. Why do we use a virtual environment?

Answer: A virtual environment keeps project dependencies isolated from the global Python installation. This prevents version conflicts between different projects.

### 5. What is `requirements.txt`?

Answer: It is a file listing all project dependencies and versions. It helps recreate the same environment using `pip install -r requirements.txt`.

### 6. What is the difference between `import module` and `from module import function`?

Answer: `import module` loads the whole module, while `from module import function` imports only the specific function/class. The second is shorter, but the first avoids name collisions.

## Quick viva tasks

- Create a virtual environment and install one package in it.
- Show how to freeze dependencies into `requirements.txt`.
- Explain why two projects may need different versions of the same library.
