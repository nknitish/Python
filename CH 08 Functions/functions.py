
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

