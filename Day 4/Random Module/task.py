## In this lesson we'll work on Modules
## What are the Modules? Watch the video Day4 31. Random Module min 7:22
## Basically it's a set/divided tasks between people. For example, if we're going to build a car,
## people can collaborate and work together in different tasks such as wheel, axles, chassi etc.,
## rather than 1 person build the entire car by himself.


# ###### First practice #######
#
# import random  ## Importing random from Python Module
# ## here I'm importing my_favourite_number from my_module
# import my_module
#
# ## Setting a var to random.randint(1, 10) will give a number from 1-10
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# print(my_module.my_favourite_number)  ## importing my_favourite_number


# ##### Second practice  ######
# import random
#
#
# random_number_0_to_1 = random.random() ## random.random() Return the next random floating-point number in the range 0.0 <= X < 1.0
# print(random_number_0_to_1)  ## here will show 0.07349862313325461 some number
#
#
# random_number_0_to_1_by_multiplied_10 = random.random() * 10
# print(random_number_0_to_1_by_multiplied_10)  ## here will show 6.315050930273309 some number
#
# random_float = random.uniform(1, 10)
# print(random_float)


###### Third practice ######

# PAUSE 1 - Heads or Tails
# Create a coin flip program using what you have learnt about randomisation in Python.
# It should randomly print "Heads" or "Tails" everytime it is run.

import random
print("Hello to Flip Coin Game")

coin = random.randint(1, 2)

if coin == 1:
    print("Heads")
else:
    print("Tails")
