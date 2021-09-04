age=int(input("Enter your age: "))

#let assume you live for 90years
years_remaining= 70-age
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12

print(f"You have {years_remaining} years, {days_remaining} days, {weeks_remaining} weeks and {months_remaining} smonths left")
