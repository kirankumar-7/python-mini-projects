print("Welcome to the tip calculator ")
bill=float(input("What was the total bill: $"))
tip=int(input("What pecentage tip you like to give? 10, 12: "))
number_of_people=int(input("How may people to split the bill: "))

tip_as_percent=tip/100

total_tip_amount= bill*tip_as_percent

total_bill= bill+total_tip_amount

bill_per_person=total_bill/number_of_people

final_amount=round(bill_per_person,2)                                 #rounding off to 2 decimal places
print(f"Each person should pay {final_amount} dollars ") 
    
