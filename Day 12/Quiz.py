# Prime Number Checker
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#
# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.
# It should return True or False.
#
# e.g.
# 7 is a primer number because it is only divisible by 1 and itself.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.
#
#
# Example Input 1
# 73
# Example Output 1
# True

# Example Input 2
# 75
# Example Output 2
# False

# Declare Global variable
is_divisible = True

def is_prime(num):
    global is_divisible  # Use the global variable (initially True)

    # Handle edge case for numbers less than 2
    if num < 2:
        is_divisible = False
        return False

    # Check divisibility from 2 to num - 1
    for n in range(2, num):
        if num % n == 0:
            is_divisible = True
            return False

    is_divisible = False
    return True

# Example usage
print(is_prime(10))  # Output: False (10 is not a prime number)
print(is_prime(73))  # Output: True (73 is a prime number)
print(is_prime(29))  # Output: True (29 is a prime number)
print(is_prime(75))  # Output: False (75 is not a prime number)

