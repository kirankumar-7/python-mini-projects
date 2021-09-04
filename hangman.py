import random
print("Welcome to the hangman game ")

word_list=["python","java","programming","coding","interview","dsa","javascript","html","css","computer"]

chosen_word=random.choice(word_list)

#creating a empty list
display=[]
word_len=len(chosen_word)
for _ in range(word_len):
    display += "_"
    print(display)

guess=input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter==guess:
        print("Right")
    else:
        print("false")
    
