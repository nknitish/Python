
# If Else in Python

age= int(input("Enter your age : "))

if age < 0:
    print("Age cannot be negative.")
elif age < 18:
    print("You are not eligible.")
elif age == 18:
    print("You are eligible, and you are exactly 18.")
else:
    print("You are eligible.")


# Relational Operatior 

#OR || And

if age == 20 or age >=20 :
    print("Age is 20 Above")
  
# Exercise #1    

marks1= int(input("Enter Marks 1 Number : "))
marks2= int(input("Enter Marks 2 Number : "))
marks3= int(input("Enter Marks 3 Number : "))

sum= marks1+ marks2+ marks3

if ((sum/300) *100) > 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print(f"You are passed : {(sum/300) *100}")
else:
    print("You are failed")


# Exercise #2 - Spam comment filter
spam1 ="buy now" 
span2 ="click", 
spam3 ="link", 
spam4= "money"

comment = input("Enter a comment: ").strip()

if spam1 in comment or span2 in comment or spam3 in comment or spam4 in comment :
    print("This comment may be spam.")
else:
    print("This comment looks safe.")
    
