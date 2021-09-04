#difficult level
import random

import random
print("Welcome to the random password generator! ")

letters=[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['!','@','$','%','^']
numbers=['0','1','2','3','4','5','6','7','8','9']

no_letters=int(input("How many letters you want in your password?\n"))
no_symbols=int(input("How many symbols  you want in your password?\n"))
no_numbers=int(input("How many numbers you want in your password\n"))

#creating a list
password_list=[] 

for char in range(1,no_letters+1):                 
    password_list.append(random.choice(letters))

for char in range(1,no_symbols+1):                          
    password_list.append(random.choice(symbols))                

for char in range(1,no_numbers+1):                            
    password_list.append(random.choice(numbers))

#to reorder a list 
random.shuffle(password_list)

#to change the list in the form of order
password=""
for char in password_list:
    password+=char

print(f"The password is:{password}")
