
# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

# Creating a dictionary of Hindi words with their English translations
# hindi_dict = {
#     "Namaste": "Hello",
#     "Dhanyavad": "Thank you",
#     "Kripya": "Please"
# }

# input_word = input("Enter a Hindi word to look up its English translation: ")
# print(hindi_dict.get(input_word)) 


#Write a program to input eight numbers from the user and display all the unique numbers

# myset = set()  # Creating an empty set to store unique numbers
# for i in range(8):
#     num = int(input(f"Enter a number {i+1}  : "))
#     myset.add(num)

# print("The unique numbers are:", myset)  # Output: The unique numbers are: {unique numbers}


# Can we have a set with 18 (int) and '18' (str) as a value in it?
print({18, '18'})  # Output: {18, '18'} 

# Print type of {}
s={}
print(type(s))

# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

myFriends={}

for i in range(4):
    name= input("Enter Your Name :") 
    age= int(input("Enter Your Age: "))       
    myFriends.update({name:age})

print(myFriends)    


