from datetime import datetime

currentYear = datetime.utcnow().year
birthYear = int(input("please enter your birth year: "))
ageInMonths = (currentYear - birthYear) * 12

print(ageInMonths)