#A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

words = ["apple", "boy", "egg"]

# Open the file in write mode
with open("CH 09 File/practice2.txt", "r") as f:
    content = (f.read()).lower()

# Update content
for word in words:
    content= content.replace(word,  "#" * len(word) )   

# Update file
with open("CH 09 File/practice2.txt", "w") as f:
    f.write(content) 

print(content)    

