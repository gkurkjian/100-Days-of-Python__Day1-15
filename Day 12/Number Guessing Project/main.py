import random
from my_art import logo

EASY_DIFFICULTY_CHOICE = 10
HARD_DIFFICULTY_CHOICE = 5

def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        ## TODO's: 6. prompt 'Make a guess: ', calculate if it's too low or too high, reduce the lifespan
        if level == 'easy':
            return EASY_DIFFICULTY_CHOICE
        elif level == 'hard':
            return HARD_DIFFICULTY_CHOICE
        else:
            print('Wrong input. Choose only between "easy" or "hard"')

def check_answer(user_guess, actual_number, turns):
    if user_guess > actual_number:
        print("Too high.")
        return  turns -1
    elif user_guess < actual_number:
        print("Too low.")
        return  turns -1
    else:
        print(f"You got it! The answer was {actual_number}.")
        return 0

def game():
    ## TODO's: 1. show the user logo/welcome
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    ## TODO's: 2. choose random number between 1 to 100
    actual_number = random.randint(1, 100)
    print(f"pst, correct answer is: {actual_number}")

    ## TODO's: 3. prompt the difficulty option 'easy', 'hard'
    turns = set_difficulty()

    while turns > 0:

        ## TODO's: 4. prompt user to guess the number, after guess check if is right
        print(f"You have {turns} attempts remaining to guess the number.")
        user_input = int(input("Make a guess: "))

        turns = check_answer(user_input, actual_number, turns)

        if turns == 0:
            ## TODO's: 7. give the output if the user loses or wins. End the game
            print("You've run out of guesses. Refresh the page to run again.")
            return
        else:
            ## TODO's: 5. if guess not right calculation the life span remain and prompt the option guess again
            print("Guess again.")

game()
