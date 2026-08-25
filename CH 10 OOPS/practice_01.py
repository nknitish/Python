class Programmer :
    company = "Microsoft"
    def __init__(self, name, salary,pin):
        self.name=name;
        self.salary= salary
        self.pin=pin
        
    

emp1= Programmer("Nitish", "30L" , 504841)

print(emp1.company, emp1.name, emp1.salary, emp1.pin)
