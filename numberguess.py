import random

number_range=input("Enter a number: ")      
guess=0

if number_range.isdigit():                  #returns true if all the characters in the strings are digits
    number_range=int(number_range)
    if number_range <=0:
        print("Invalid" ",","Enter a number greater than 0")
        quit()
        
else:
    quit()
     


random_number=random.randint(0,number_range)

while True:
    guess+=1
    user_guess=input("Guess a number: ")
    if user_guess.isdigit():                  
            user_guess=int(user_guess)
    else:
         print("enter a valid number")
         continue
#nested if
    if user_guess==random_number:
        print("You guessed the random number correctly")
        break
    elif user_guess >random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You made it in",guess,"guesses") 
        
