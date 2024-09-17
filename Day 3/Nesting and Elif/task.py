## Implementing if, else nested example + elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age my dear? "))
    if age <= 12:
        print("You've to pay 5$")
    elif age <=18:
        print("You've to pay $7")
    else:
        print("You're mature enough to pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
