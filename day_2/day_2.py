# Day 2-1
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

user_input = input("Type a two digit number\n")

first_term = user_input[0]
second_term = user_input[1]
sum = int(user_input[0]) + int(user_input[1])

second_term_modified = str(second_term)

print(first_term + " + " + second_term_modified + " = " + str(sum))