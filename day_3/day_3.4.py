# Day 3-4

print("Welcome to @philipsinnott Pizza!")
print("--------------------------------")

size = input("Pizza size? [S]mall, [M]edium or [L]arge: ")
pepperoni = input("Pepperoni? [Y] or [N]: ")
extra_cheese = input("Extra cheese? [Y] or [N]: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y" and size == "S":
    bill += 2
elif pepperoni == "Y" and size != "S":
    bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")