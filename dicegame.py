import random
min=1
max=6
print("Welcome to my game! ")

#gameloop
while True:
    print()
    choice=int(input("1.Play game\n2.About game\n3.Exit\nEnter your choice here: "))
    break
if choice == 1:
    print()
    roll_choice=input("Do you wanna role the dice,(yes/no): ")
    while roll_choice.lower()=="yes":
        num1=random.randint(min,max)
        num2=random.randint(min,max)
        print("First number is:",num1)
        print("Second number is:",num2)

        if num1+num2 in(7,11):
            print()
            print("Sum of numbers:",num1+num2)
            print("You win! ")
            print()
            roll_choice=input("Do you wanna play again,(yes/no): ")

        else:
            print("Sum of numbers is:",num1+num2)
            print("You lost ")
            print()
            roll_choice=input("Do you wanna play agian,(yes/no): ")
        

elif choice==2:
    print()
    print("This is a dice rolling game ")
    print("""The user will allowed to roll the dice twice and if the sum of the two numbers in the dice is equal to 7 or 11 the user wins else he loses""")

elif choice ==3:
    print()
    print("Thanks for playing the game" )
    
 
        
        
        
        
    



