#easy level

import random
print("Welcome to the random password generator! ")

letters=[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['!','@','$','%','^']
numbers=['0','1','2','3','4','5','6','7','8','9']

no_letters=int(input("How many letters you want in your password?\n"))
no_symbols=int(input("How many symbols  you want in your password?\n"))
no_numbers=int(input("How many numbers you want in your password\n"))

password="" 

for char in range(1,no_letters+1):                  #if user input is 4 then (1,3+1)-->(1,4) so in the range to get 4 we are adding plus 1 
    password+=random.choice(letters)

for char in range(1,no_symbols+1):                  #if user gives 4 for symbols           
    password+=random.choice(symbols)                #the char will have the values range(1,5) and it increments with the password 

for char in range(1,no_numbers+1):                            
    password+=random.choice(numbers)

print(password)
