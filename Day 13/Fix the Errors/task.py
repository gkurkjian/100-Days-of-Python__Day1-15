### I fix the code and comment them. The issue of this code will break after 2 attempts

# try:
#     age = int(input("How old are you? "))
# except ValueError:
#     print("You've typed in an invalid number. Please try again with numerical input.")
#     try:
#         age = int(input("How old are you? "))
#     except ValueError:
#         print("You've typed in an invalid number again. Exiting program.")
#         age = None
#
# if age is not None:
#     if age > 18:
#         print(f"You can drive at age {age}.")
#     else:
#         print(f"You cannot drive at age {age}.")



### I tried to become with a code that'll not break after numerous attempts until gets
###numeric value from the user
def get_age():
    try:
        return int(input("How old are you? "))
    except ValueError:
        print("You've typed in an invalid number. Please try again with numerical input.")
        return get_age() ## Recursively call the function until valid input is given

age = get_age()

if age > 18:
    print(f"You can drive at age {age}")
else:
    print(f"You cannot drive at age {age}")
