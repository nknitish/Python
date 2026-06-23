class Calculator : 
    def __init__(self, num):
        self.num=num;
     
    def square(self):
        print(f"Square of {self.num} is {self.num * self.num}")
        
    def cube(self):
        print(f"Square of {self.num} is {self.num * self.num * self.num}")
        
    

cal1 = Calculator(5)
cal1.square()
cal1.cube()

