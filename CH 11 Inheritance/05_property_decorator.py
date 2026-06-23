
# @property Decorators
# The @property decorator lets you access a method like an attribute.

class Employee:
    @property
    def salary(self):
        return 50000

e = Employee()

print(e.salary) # Even though salary is a method, it behaves like a variable.

# Real-World Example

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


r = Rectangle(10, 5)
print(r.area) # 50

# area is calculated dynamically.
# If length or width changes, area updates automatically.

r.length = 20
print(r.area)



#The real benefit appears later
#Suppose Version 1 of your class is:


"""

class Employee:
    def __init__(self, salary):
        self.salary = salary

#Usage:
emp= Employee (1000)
emp.salary

# Now later you decide salary should be computed:

class Employee:
    @property
    def salary(self):
        return self.basic + self.bonus

#The user code stays exactly the same:

emp.salary

No need to change:
emp.get_salary()

everywhere in your application.

"""







