# import random
# import my_module
#
# random_num = random.randint(1, 10)
# print(f"1. random.randint(a: 1, b: 10): {random_num}")
#
# print(f"2. This is coming from costume module: {my_module.my_favourite_number}")
#
# random_number_0_to_1 = random.random()
# print(f"3. random_number_0_to_1 = random.random():  {random_number_0_to_1}")
#
# random_number_0_to_1 = random.random() * 10
# print(f"4. random_number_0_to_1 = random.random() * 10:  {random_number_0_to_1}")
#
# random_float = random.uniform(1, 10)
# print(f"4. random_float = random.uniform():  {random_float}")


### 1. Pause ###
# Create a coin flip program using what you have learnt about randomisation in Python.
# It should randomly print "Heads" or "Tails" everytime it is run.

import random

coin = random.randint(0, 1)
if coin == 0:
    print("heads")
else:
    print("tails")