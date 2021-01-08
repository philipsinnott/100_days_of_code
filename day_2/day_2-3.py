# Day 2-3
years = int(input("Enter how many years you wish to live and we will convert it into days, weeks and months:\n "))

days = round(years * 365)
weeks = round(years * 52)
months = round(years * 12)


print(f"You have {days} days, {weeks} weeks, and {months} months left.")