fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:  ## basically it's assigning var = fruit and iterating each item in List
#     print(fruit)  ## The output will be;  Apple
#                                         # Peach
#                                         # Pear
#                                         # Apple
#


# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")   # Apple
#                             # Apple Pie
#                             # Peach
#                             # Peach Pie
#                             # Pear
#                             # Pear Pie

for fruit in fruits:  ## The indentation it's important. Now it'll print the List on line 23
    print(fruit)
    print(fruit + " Pie")
    print(fruits)
