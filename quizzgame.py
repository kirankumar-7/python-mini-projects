print("welcome to my fitness quiz :)")
quiztime=input("do you want to play my quiz? ")
if quiztime.lower()!="yes" :
	quit()                                               #for indentation(4spaces) use tabs 
print("Common let's play")
score=0
question1=input("1kg is equal to how many calories? ")
if question1.lower() =="7700":
	print("Congrats")
	score+=1
else:
	print("better luck next time")

question2=input("What is the body fat percentage to get visible abs? ")
if question2.lower() == "14":
	print("Congrats")
	score+=1
else:
	print("better luck next time")

question3=input("The rep ranges for hypertrophy? ")
if question3.lower() == "10-15reps":
	print("Congrats")
	score+=1
else:
	print("better luck next time")
question4=input("What we have to do weight gain? ")
if question4.lower() == "calorie surplus":
	print("Congrats")
	score+=1
else:
	print("better luck next time")
question5=input("What we have to do for weight loss? ")
if question5.lower() == "calorie deficit":
	print ("Congrats")
	score+=1
else:
	print("better luck next time")
print("You answered "+str(score)+" questions correctly")   #why str? because we cant concadenate the number(int) with other strings
print("Your percentage is "+str((score/5)*100)+"%")





	
