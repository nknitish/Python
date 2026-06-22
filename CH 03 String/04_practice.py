# Program to display a user entered name followed by Good Afternoon using input() function.

name = input("Enter your name: ")
print(f"Good Afternoon, {name}!")


# Write a program to fill in a letter template given below with name and date

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Nitish").replace("<|Date|>", "2024-06-30"))


#Write a program to detect double space in a string.
text = "This is a string with  double spaces."
print("Double space detected:", text.find("  ") != -1)

# Replace the double space from problem 3 with single spaces
text = text.replace("  ", " ")
print("Text after replacing double space:", text)


# Write a program to format the following letter using escape sequence characters.
letter = "\"Dear Harry, this python course is nice. Thanks!\""
print(letter)
