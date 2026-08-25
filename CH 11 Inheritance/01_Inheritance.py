# Sigle Inheritance 

class Programmer :
    company= "Paypal"
    
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary
    
    def show(self):
        print(self.name, self.salary)


# Inherit Class
class Company(Programmer) :
 
    #super
    def __init__(self, company, name, salary):
        super().__init__(name, salary);
        self.company= company;
    
    def printCompany(self) :
        print(self.company)  
        
# Create a company 

com1= Company("Google", "NK","10L");
com1.printCompany()
com1.show()

