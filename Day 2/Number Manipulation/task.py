# bmi = 84 / 1.65 ** 2
# print(bmi)  # 30.85399449035813
#
# print(int(bmi)) # 30
#
# print(round(bmi))  # 31
#
# print(round(bmi, 2)) # this will display flouting number up to two digit which is: 30.85

#########################################

### Assignment Operators
### Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
#
# +=
#
# -=
#
# *=
#
# /=

# score = 0
#
# # User scores a point
# score += 1
# print(score)

##############################################

# f-Strings
# In Python, we can use f-strings to insert a variable or an expression into a string.

age = 12

print(f"I am {age} years old")

# Will output I am 12 years old.

score = 0
height = 1.8
is_winning = True

## If we're going to print all of them and diguard what type of they are;
# we can use f-string{}
print(f"Your score is = {score}, and your height is. {height}, you are winning = {is_winning}")

