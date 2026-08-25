# A setter runs whenever someone assigns a value, so you can do many things.
# Validate Data
# Logging / Auditing
# Type Checking


# _salary is a private variable, which means it should not be accessed directly from outside the class. Instead, we use getter and setter methods to access and modify the value of _salary.

class Employee:
    def __init__(self):
        self._salary = 0

    # Getter
    @property
    def salary(self):
        return self._salary

    # Setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative")
        else:
            self._salary = value


e = Employee()

e.salary = 5000
print(e.salary)



"""
e.salary = 50000
      │
      ▼
   Setter
      │
 Validate value
      │
      ▼
 self._salary = 50000


print(e.salary)
      │
      ▼
   Getter
      │
      ▼
 return self._salary

"""
