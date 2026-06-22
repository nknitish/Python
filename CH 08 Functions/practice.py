
# -------------------------------------------------------------------------   
# Write a program using functions to find greatest of three numbers

def maxNum(n1,n2,n3) :
    max =n2;
    if n1 > n2 :
        max =n1;
    
    if n3 >max :
        max=n3
            
    return max        
        

# print (maxNum(1,2,3))
# print (maxNum(3,2,1))
# print (maxNum(1,3,2))

# -------------------------------------------------------------------------  
# Write a python program using function to convert Celsius to Fahrenheit.
# Function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# celsius = float(input("Enter temperature in Celsius: "))
# print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")

# ------------------------------------------------------------------------- 
# Write a recursive function to calculate the sum of first n natural numbers.

def recursiveSum(n) :
    if(n==1) :return 1
    return n + recursiveSum(n-1)

# num= int(input("Enter numner : "))
# print(f"Sum of {num} is {recursiveSum(num)}")

 
# -------------------------------------------------------------------------  
#Write a python function to remove a given word from a list 

def removeWord (list, word):
    newList=[]
    for item in list :
        if not(item ==word) :
            newList.append(item)        
    return newList

list =["apple","boy","cat","dog","egg","fish"]

# print(removeWord(list, "cat"))


# -------------------------------------------------------------------------  
#Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i} ")

table(5)
# -------------------------------------------------------------------------  
# -------------------------------------------------------------------------  
# -------------------------------------------------------------------------  


         