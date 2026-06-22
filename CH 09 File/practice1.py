
# Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old.

import os

def table(n) :    

    # Create directory if it doesn't exist
    os.makedirs("CH 09 File/tables", exist_ok=True)
    
    with open(f"CH 09 File/tables/table_{n}.txt", "w") as f:
    
        for i in range(1,11) :
            f.write (f"{n} x {i} = {n*i} \n")
    
    #Close 
    # f.close()
       

for i in range(1, 21):       
    table(i)        
        