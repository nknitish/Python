
# Valid String in Python

a= 'Hello, World!' # Single Quotes String
b= "Hello, World!" # Double Quotes String   
c= '''Hello, World!''' # Triple Quotes String
d= """Hello, World!""" # Triple Quotes String    


# substring
str1 = "Hello, World!"
print(str1[0])   # Output: H
print(str1[7])   # Output: W
print(str1[-1])  # Output: !    
print(str1[0:5]) # Output: Hello 

# Last Index in not included 
print(str1[0:2]) # Output: He
print(str1[0:3]) # Output: Hel
print(str1[7:12])  # Output: World! 
print(str1[7:])  # Output: World!   

# Check value for - 
print(str1[-5: -2])  # Output: Wor
print(str1[2:5])    # Output: llo

# skipping characters
str="0123456789"
print(str[0:5:2])  # Output: 024
print(str[1:8:2])  # Output: 1357