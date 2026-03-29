# Generate a random number
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




