quiz=input("Shall we play the adventure game? ")
if quiz.lower()!= "yes":
    quit()
print("lets play!")

ques_1=input("Want to take left or right ")
if ques_1 == "left":
    print("you have reached miami beach  ")
else:
    print("you took a wrong way and you the lost the game ")


ques_2=input("type 'e' for enjoy there or 'n' for no need ")
if ques_2.lower() == "e":
    print("You won")
elif ques_2.lower()=="n":
    print("You lost the mood and you lost the game")



print("Thanks for the playing this game")



