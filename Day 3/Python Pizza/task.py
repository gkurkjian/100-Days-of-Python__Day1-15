print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

## First todo
the_bill = 0

if size == 'S':
    the_bill += 15
elif size == 'M':
    the_bill += 20
elif size == 'L':
    the_bill += 25
else:
    print("Wrong input")

## Second todo
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == 'Y':
    if size == 'S':
        the_bill += 2
    else:
        the_bill += 3

## Third todo
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == 'Y':
    the_bill += 1

print(f"Your final bill is: ${the_bill}.")


