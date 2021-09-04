import random

#global constants
Easy_level_turns=10
Hard_level_turns=5

#function to check against guess and actual answer
def check_answer(guess,answer,turns):
    """checks guess answer against answer and returns the number of turns remaining"""
    if guess>answer:
        print("Too high")
        return turns-1
    elif guess<answer:
        print("Too low")
        return turns-1
    else:
        print(f"You got it!,The answer was {answer}")

def check_difficulty():
    user_input=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_input =="easy":
      return Easy_level_turns
    else:
      return Hard_level_turns 

def game():
    print("Welcome to the number guessing game! ")
    print("I'm thiniking of a number between 1 to 100 ")
    answer=random.randint(1,100)

    turns=check_difficulty()
   
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number")

        guess=int(input("Make a Guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You have ran out of guesses, You lose ")
            return                                                           #this return keyword exits the function and stops so the bug will be fixed 
game()


