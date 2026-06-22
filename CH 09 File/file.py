
# Write Files In Python

# Open the file in write mode
f = open(".gitignore", "w")

# Write a string to the file
f.write("# VS Code\n")
f.write(".vscode/")

# Close the file
f.close()



# Open the file in read mode using 'with'

with open(".gitignore", "r") as f:
# Read the contents of the file
 text = f.read()
 
# Print the contents
print(text)

# print if vscode is contained 
search =".vscode"

if(search in text):
    print(f"Yes, {search} is included")
else :
   print(f"No, {search} is not included")
   

