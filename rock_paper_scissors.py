import random 

user_score=0
computer_score =0
options=["rock", "paper", "scissors"]

while True :
    user_input =input("Type Rock, Paper, Scissors or type Q to quit: ").lower()

    if user_input.lower()== "q":
        break
    if user_input not in options :
        continue        
    
    random_number=random.randint(0,2)
    computer_input= options[random_number]
    print("computer picked",computer_input+".")
    
    if user_input =="rock" and computer_input =="scissors":
     print("You won")
     user_score+=1

    elif user_input =="paper" and computer_input =="rock":
     print("You won")
     user_score+=1
     
    elif user_input =="scissors" and computer_input =="paper":
     print("You won")
     user_score+=1

    else:
        print("You lost")
        computer_score+=1

print("You won",user_score,"times")
print("Computer won",computer_score,"times")
    
print("Thanks for the playing the game!")
