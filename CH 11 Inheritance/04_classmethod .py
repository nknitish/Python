# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.

class Employee :
    name = "Employee"
    @classmethod
    def show(cls):
        print(f"Name : {cls.name}")
       
       
e1= Employee();

# Crate Object attribute
e1.name="New Name"
e1.show()  # After @classMethod it wil show Employee



