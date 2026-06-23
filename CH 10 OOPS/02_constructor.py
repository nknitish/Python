class Employee : 
    # constructor method
    def __init__(self, name, age=26):   #dunder method 
        self.name=name
        self.age=age
   
    def getInfo(self):
        print(f"Name is = {self.name} Age is = {self.age}")
       

# Creating object
emp1= Employee("Nk",27)
emp1.getInfo()




