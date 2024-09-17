print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")  # This is type str
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")  # This is type str
extra_cheese = input("Do you want extra cheese? Y or N: ")  # This is type str
the_bill = 0

# Calculate how much they need to pay based on their size choice
if size == "S":
    the_bill = 15
elif size == "M":
    the_bill = 20
elif size == "L":
    the_bill = 25

# Calculate how much to add to their bill based on their pepperoni choice
if pepperoni == "Y":
    if size == "S":
        the_bill += 2  # Add $2 for small pizza
    else:
        the_bill += 3  # Add $3 for medium or large pizza

# Calculate how much to add for extra cheese
if extra_cheese == "Y":
    the_bill += 1  # Add $1 for extra cheese

# Print the final bill
print(f"Your final bill is: ${the_bill}.")