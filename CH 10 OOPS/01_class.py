class Employee :
    name = "Nk"
    lang= "Python"
    
    #Methods
    def getInfo(self) :
        print(f"My Name is {self.name} and lang is {self.lang}")
    
    def greeting(self):
        print("Good Morning !")
    
    @staticmethod
    def greet():
        print("Good Evening !")    
    

# Creating object
emp1= Employee()
emp2= Employee()
emp3= Employee()

# Updaing object
emp1.salary= "$2,00,000"
emp3.name="Naveen"

# Accessing properties 
print(emp1.name, emp1.salary)
# print(emp2.name, emp2.salary) # AttributeError emp2.salary

# Accessing methods
emp3.getInfo()
Employee.getInfo(emp1)

# Use Self in method 
emp1.greeting()

# staticmethod
emp1.greet()



