from art import logo

## TODO: Write out the calculating procedures (add, subtract, multiply, divide)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

## TODO: Add these 4 functions into a dictionary as the values. Key = "+", "-", "*", "/".
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}

## TODO: Use the dictionary operations to perform the calculation.
## This is just a printing to check the access of the operations
# procedure = operations["*"](5, 4)
# print(procedure)

def calculator():
    print(logo)
    first_input = float(input("What's the first number?: "))

    continue_calculation = True
    while continue_calculation:

        user_pick_operation = input("+\n-\n*\n/\nPick an operation: ")

        second_input = float(input("What's the next number?: "))

        operations_function = operations[user_pick_operation]
        result = operations_function(first_input, second_input)

        print(f"{first_input} {user_pick_operation} {second_input}: {result}")

        prompt_to_continue = input("Type 'y' to continue calculating with 100.0, or type 'n' to start a new calculation: ")

        if prompt_to_continue == 'y':
            first_input = result
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()

calculator()  ## running the program here
