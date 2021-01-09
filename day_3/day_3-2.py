print("-----------------------")
print("| Calculate your BMI! |")
print("-----------------------")

height = float(input("Enter your height in meters (I.E. 1.83): \n"))
weight = int(input("Enter your weight in kilograms (kg): \n"))

bmi = int(weight / height ** height)

print("Your BMI is: " + str(bmi))

if bmi < 18.5:
    print("You are underweight.")
elif bmi > 18.5 and bmi < 25:
    print("You are of normal weight.")
elif bmi > 25 and bmi < 30:
    print("You are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
