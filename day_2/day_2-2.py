# Day 2-2
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#
# You should convert the result to a whole number.
print("-----------------------")
print("| Calculate your BMI! |")
print("-----------------------")

height = float(input("Enter your height in meters (I.E. 1.83): \n"))
weight = int(input("Enter your weight in kilograms (kg): \n"))

bmi = int(weight / height ** height)

print("Your BMI is: " + str(bmi))

#    if bmi < 18.5:
#        print("You are underweight.")
#    elif bmi > 18.5 & bmi < 25:
#        print("You are of normal weight.")
#    elif bmi > 25 & bmi < 30:
#        print("You are overweight.")
#    elif bmi > 30:
#        print("You are obese.")


