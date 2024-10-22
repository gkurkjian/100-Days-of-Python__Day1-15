from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiple(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": division,
}

def calculator():
    print(logo)
    first_num = float(input("What's the first number?: "))

    continue_calculation = True

    while continue_calculation:
        user_operation_choice = input("+\n""-\n""*\n""/\nPick and operation: ")
        second_num = float(input("What's the next number?: "))

        operation_function = operations[user_operation_choice]

        result = operation_function(first_num, second_num)

        print(f"{first_num} {user_operation_choice} {second_num} = {result}")

        check_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ")

        # ##Mine
        # if check_continue == 'y':
        #     first_num = result
        # elif check_continue == 'n':
        #     calculator()
        # else:
        #     calculator()

        ##Angela's way
        if check_continue == 'y':
            first_num = result
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()

calculator()
