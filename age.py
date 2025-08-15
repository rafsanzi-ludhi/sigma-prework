import datetime

day = int(input("Enter day of birth: "))
month = int(input("Enter month of birth: "))
year = int(input("Enter year of birth: "))

today = datetime.date.today()

age = today.year - year

print(age)
