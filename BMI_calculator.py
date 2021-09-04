print("What is BMI?\n ")
print("BMI is body mass index which is alternative method for measuring the body fat\n ")

name=input("Enter your name: ").upper()
Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your weight in kilograms: "))

#height in meters
Height=Height/100                                               #1meter =100cms

BMI= Weight/(Height*Height)                                        #height square we can also written as height**2
print()
print("Your body mass index is: ",BMI)

#nested if
if BMI>0:                                                   #the bmi will be always positive and would be in the range of 16-30       

    if(BMI <=16):
        print(name,"you are severly underweight: ")
    elif(BMI<=18):
        print(name,"you are underweight")
    elif(BMI<=25):
        print(name,"you are normal")
    elif(BMI<=30):
        print(name,"you are obese")
    else:
        print(f"{name} you are severly obese")

else:
    print(name,"enter the correct details")























