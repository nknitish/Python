
# functions in Python

# Funcitons Declare 
def average(a,b,c) :
     return (a+b+c) /3 


# Funciton calls 
print(average(4,6,8))
print(average(5,6,7))



# Factorial Funciton  // Recursion

def factorial(n) :
    if n==1 :   
        return 1
    return n * factorial(n-1)
    
num= int(input("Enter number : "))
print(f"Factorial of {num} is {factorial(num)}")

# *args and **kwargs
# *args = multiple positional arguments (stored in a tuple)
# **kwargs = multiple keyword arguments (stored in a dictionary)

def show_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_info(10, 20, 30)
show_info(name="Aman", age=21, city="Delhi")
show_info(1, 2, 3, name="Rahul", course="Python")

# Example of using *args for sum

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum:", add_numbers(2, 4, 6, 8))

# Example of using **kwargs for printing details

def display_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

display_details(name="Neha", roll=12, branch="CS")

