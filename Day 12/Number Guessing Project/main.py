import random
from art import logo

EASY_LEVEL_GAME = 10
HARD_LEVEL_GAME = 5

## Function to check users' guess against actual answer.
def check_answer(user_guess, actual_number, life_span):
    if user_guess < actual_number:
        print("Too Low")
        return  life_span -1
    elif user_guess > actual_number:
        print("Too High")
        return life_span -1
    else:
        print(f"You got it right the number is {actual_number}")

## Function to set difficulty.
def set_difficulty():
    difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard':   ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_GAME
    else:
        return HARD_LEVEL_GAME

def game():
    print(logo)
    ## Choosing a random number between 1 and 100.
    random_num = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print(random_num)

    turns = set_difficulty()

    user_guess = 0

    ## Repeat the guessing functionality if they get it wrong.
    while not user_guess == random_num:
        print(f"You have {turns} attempts remaining to guess the number")

        user_guess = int(input("Make a guess: "))

        ## Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(user_guess, random_num, turns)

        if turns == 0:
            print("You run out of time. Game over")
            return   ## here will terminate the code if the user run out of guess
        elif user_guess != random_num:
            print("Guess again: ")

game()
