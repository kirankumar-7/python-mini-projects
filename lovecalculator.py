print("welcome to the love calculator! ")
name1=input("What is your name? ").lower()
name2=input("What is their name? ").lower()

combined_name=name1+name2
t=combined_name.count("t")
r=combined_name.count("r")
u=combined_name.count("u")
e=combined_name.count("e")
true  =t+r+u+e                                                  #this stores integer value

l=combined_name.count("l")
o=combined_name.count("o")
v=combined_name.count("v")
e=combined_name.count("e")
love  =l+o+v+e                                                    #this stores integer value

'''concatenating int and int so change to string for example we get true 5 times and love 6times to get 56 we need strings
here this will be a string we can't compare it it the if that is str<int gives error so wrap the string around integer '''

love_score =int(str(true)+str(love))                      

if (love_score<10) or(love_score>90):
    print(f"Your score is {love_score},you get together like coke and mentos")  
elif(love_score>=40) and (love_score<=50):
    print(f"Your score is {love_score},you are alright together ")
else:
    print(f"Your score is{love_score}")  

