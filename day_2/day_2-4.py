# Day 2-4

print("TIP CALCULATOR")
print("--------------")

bill = float(input("What was the total bill?\n $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

split_amount = int(input("How many people to split the bill?\n"))

tip_as_percent = tip / 100
total_tips = bill * tip_as_percent
total_bill = bill + total_tips
bill_per_person = total_bill / split_amount
bill_per_person_final = round(bill_per_person, 2)

print(f"Each person should pay: {bill_per_person_final}")
