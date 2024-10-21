# Leap Year
# 💪 This is a difficult challenge! 💪
#
# Write a program that returns True or False whether a given year is a leap year.
#
# A normal year has 365 days, while leap years have 366, with an extra day in February.
# The reason we have leap years is fascinating, and this video does it more justice.
#
# This is how you determine whether a particular year is a leap year:
#
# - On every year divisible by 4 with no remainder
# - Except every year that is evenly divisible by 100 with no remainder
# - Unless the year is also divisible by 400 with no remainder
#
# If English is not your first language or if the above logic is confusing, try using this flow chart.
#
# Example:
# The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So, the year 2000 is a leap year.
#
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)
#
# Warning:
# Your return should be a boolean and match the Example Output format exactly, 
# including spelling and punctuation.
#
# Example Input 1:
# 2400
#
# Example Return 1:
# True
#
# Example Input 2:
# 1989
#
# Example Return 2:
# False
#
# How to test your code and see your output?
# Udemy coding exercises do not have a console, so you cannot use the input() function.
# You will need to call your function with hard-coded values like this:
#
def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2000))
