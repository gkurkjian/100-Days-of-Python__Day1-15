### Easy Version

# import random
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# empty_basket = []
#
# for user_nbr_letter in range(nr_letters):
#     empty_basket.append(random.choice(letters))
#
# for user_nbr_symbol in range(nr_symbols):
#     empty_basket.append(random.choice(symbols))
#
# for usr_nbr_number in range(nr_numbers):
#     empty_basket.append(random.choice(numbers))
#
# print(empty_basket)
# final_output = ''.join(empty_basket)
# print(f"Your password is: {final_output}")



### Hard Part

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

empty_basket = []

for user_nbr_letter in range(nr_letters):        
    empty_basket.append(random.choice(letters))

for user_nbr_symbol in range(nr_symbols):
    empty_basket.append(random.choice(symbols))

for usr_nbr_number in range(nr_numbers):
    empty_basket.append(random.choice(numbers))

print(empty_basket)   ## Printing the list ['A', '@'] etc.
random.shuffle(empty_basket)  ## Shuffling the all things together
final_output = ''.join(empty_basket)  ## Making it to Join to the String
print(f"Your password is: {final_output}")
