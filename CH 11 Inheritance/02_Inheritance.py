# Multiple Inheritance means a class inherits from more than one parent class.
# Example: Programmer + Manager → TeamLead

class Employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

class Programmer:
    def code(self):
        print("Can write Python code")


class TeamLead(Employee, Programmer):
    pass


lead = TeamLead("Nitish")

lead.show_name()
lead.code()