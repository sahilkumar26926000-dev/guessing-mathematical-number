# guessing-mathematical-number
start


step-1 initialize the number
import the random library
generate random integer between 1 & 50 and store it in a variable called number_to_guess



step-2 enter the game loop
Input handling
prompt the user to enter a guess.
check if the input is a valid integer.
if != integer
raise ValueError


step-3 comparison logic:
if, elif and else statement use to implement the logic
after that break the loop


End


final Display of the project
<img width="1912" height="1020" alt="guessing mathematical integer" src="https://github.com/user-attachments/assets/a4c1c99b-4603-4a5e-b6d7-7c0e4631c2df" />


Code implemented by the users to access the project

[Guess number.py](https://github.com/user-attachments/files/26313640/Guess.number.py)

# Generate a RAndom integer

import random 

number_to_guess =random.randint(1,50)

while True:

    try:
    
        #ask the user to guess the number
        
        guess = int(input("guess the number between 1 & 50: "))
        
        # check is user close to the guessing number
        
        if guess< number_to_guess:
        
            print("too low!")
            
        elif guess>number_to_guess:
        
            print("too high")
            
        # it shows return to final statement
        
        else:
        
            print("congratulation! you guessed the right integer,")

            print("see you again next time>>>")
            
            break # to break from the loop
        
    except ValueError:
    
        print("Please! Type a valid number ")














