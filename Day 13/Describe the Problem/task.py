def my_function():
    # for i in range(1, 20):
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
## Iterating and start printing from 1 to 19

# 2. When is the function meant to print "You got it"?
## In this case it won't. To fix this change the range(1, 21)

# 3. What are your assumptions about the value of i?
## The value it'll initiate from 1 to 19. But, I've fixed the range to 21, therefore
##it'll execute the line 5
