# ## Quiz number 1
#
# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
#
# result = odd_or_even(3)
# print(result)

#####################################################################

## Quiz number 2
## This is how you work out whether if a particular year is a leap year.
##
## - on every year that is divisible by 4 with no remainder
## - except every year that is evenly divisible by 100 with no remainder
## - unless the year is also divisible by 400 with no remainder

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

######################################################################

## Quiz number 3

# The code needs to print the solution to the FizzBuzz game.
#
# - Your program should print each number from 1 to x where x is the input number.
# - However when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# - When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# - And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it
# should print "FizzBuzz".

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])

fizz_buzz(15)
