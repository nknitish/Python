# Print the multiplication table of a number

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    

# -------------------------------------------------------------------------  
# Greet all people whose names start with 'S'

names = ["Harry", "Soham", "Sachin", "Rahul"]

for name in names:
    if name.startswith("S"):
        print(f"Hello, {name}!")
          
# ------------------------------------------------------------------------- 

# Check whether a number is prime

num = int(input("Enter a number: "))

if num < 2:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
           
# ------------------------------------------------------------------------- 
# Find the sum of first n natural numbers using while loop

num = int(input("Enter a number: "))

i = 1
total = 0

while i <= num:
    total += i
    i += 1

print(f"Sum is: {total}")   

# -------------------------------------------------------------------------  
# Calculate factorial of a number

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")
  
# -------------------------------------------------------------------------  

  
# -------------------------------------------------------------------------    
# -------------------------------------------------------------------------    
# -------------------------------------------------------------------------    
# -------------------------------------------------------------------------    