print("welcome to the Nightsky pizza restaurant ")

size=input("What size pizza do you want? S,M,L: ").lower()
toppings=input("Do you want toppings? Type YES or NO: ").lower()
extra_cheese=input("Do you want extra cheese? Type YES or NO: ").lower()

bill=0

if size=="s":
    bill+=10
elif size=="m":
    bill+=15
else:
    bill+=20

if toppings=="yes":
    if size=="s":
        bill+=2
    elif size=="m":
        bill+=3
    else:
        bill+=5

if extra_cheese=="yes":
    if size=="s":
        bill+=1
    elif size=="m":
        bill+=2
    else:
        bill+=3

print(f"Your total bill amount is {bill}dollars")



