# Learning Range() while using For Loops
from functools import total_ordering

### First Practice
# for number in range(1, 10):
#     print(number)  ## this will print from 1, 2, 3, ... 9


### Second Practice
# for number in range(1, 11):
#     print(number)  ## this will print from 1, 2, 3, ... 10


### Third Practice
# for number in range(1, 11, 3):
#     print(number)  ## the output will be 1, 4, 7. Basically will step by 3 while ranging it



### PAUSE 1 - The Gauss Challenge
##Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

total = 0
for number in range(1, 101):
    print(f"The value of total = {total}", " The value of number =", number)  ## This print is;
    total += number                                              ## for my understanding.

print(f"The sum of numbers between 1 and 100 inclusive is = {total}.")
