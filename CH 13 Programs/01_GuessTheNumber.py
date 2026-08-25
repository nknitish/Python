import random;

random_number = random.randint(1, 100)
attempts = 0

userNum =-1
while(userNum != random_number):
    userNum=  int(input("Guess the Number :"))
    attempts+=1
    if(userNum>random_number):
        print("Enter Lower Number")
    else :
        print("Enter Higher Number")


print(f"You have sucessfully found random number in {attempts} Attempts")        
