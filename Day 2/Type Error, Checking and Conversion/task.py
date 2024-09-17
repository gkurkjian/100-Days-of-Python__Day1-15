######## PAUSE 1. Fix the len() function so it has no more warnings or errors.
##len(12345) # this will give us error bcz len() function doesn't interpret with integers

#len("12345") # This is the correct way to print but, it'll be printed as an String
#
# # Checking the data type by using type() function
# print(type("Hello")) # <class 'str'>
# print(type(123)) # <class 'int'>
# print(type(123.45)) # <class 'float'>
# print(type(True)) # <class 'bool'>


######## PAUSE 2. Write out 4 type checks to print all 4 data types

# # Conversion or Casting
# print("123" + "456") # this simply will Concatenate String and will NOT do the Math
# print(int("123") + int("456")) # Converting to int() will do the Math # 579
#
# # Remember the 2 entities must be the same one. For example you can't do string("abc") + int(456)
# #print(int("abc") + int("456"))


########### Part 3 in the video after min 10:30
###PAUSE 3. Make this line of code run without errors
##print("Number of letters in your name: " + len(input("Enter your name")))

## Solve step-by-step
## Find the type of first print?
## Find the type of second print?

name_of_the_user = input("Enter your name") # Fetching the value from the User
length_of_the_name = len(name_of_the_user) # Assigning var and taking the len() of User's input

# Finding out what are the types
print(type("Number of letters in your name: ")) # <class 'str'>
print(type(length_of_the_name)) # <class 'int'>

## Solving it by switching into the same type and concatenate them together
## Therefore in order to concatenate together we've to make them in same type which is String
## We will add str() function to convert the integer to string

print("Number of letters in your name: " + str(length_of_the_name))

