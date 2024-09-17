## Modulo Operator
## It gives the remainder of the number after division
#print(10 % 3) # remain is 1.


####### 1st Practice #########
### Write some code using what you have learnt about the modulo operator and conditional
# checks in Python to check if the number in he input area is odd or even.
# If it's odd print out the word "Odd" otherwise printout "Even". ########


# 1. First get the user input using the input() function.
# 2. Next, convert the input into an int using the int() function.
# 3. Now store the number in a variable.
# 4. Use the modulo (%) to check if the user input number can be divided cleanly by 2.
# 5. Use if/else to check if the result of the modulo check in step 4 is equal to 0 then
# that input number is even, otherwise it's odd.

user_input = int(input("Please enter a digit: "))

if user_input % 2 == 0:
    print(f"The number you've entered: {user_input} is Even.")
else:
    print(f"The number you've entered: {user_input} is Odd.")
