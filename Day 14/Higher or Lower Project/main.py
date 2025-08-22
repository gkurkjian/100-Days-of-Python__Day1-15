from art import logo, vs
from game_data import data
import random

def format_user(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc} from {account_country}"

def compare_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def user_input():
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_guess in ['a', 'b']:
        return user_guess
    else:
        print("Invalid input. Please type only 'A' or 'B'.")
        return user_input()  # Recursive call the same function for retry

def check_results(user_guess, account_a, account_b, score):
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = compare_answer(user_guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        return True, score
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        return False, score

def play_game():
    print(logo)
    score = 0
    game_should_continue = True

    ## to initialize the first comparison
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        print(f"Compare A: {format_user(account_a)}.")
        print(vs)
        print(f"Against B: {format_user(account_b)}.")

        user_guess = user_input()

        print('\n' * 20)
        print(logo)

        game_should_continue, score = check_results(user_guess, account_a, account_b, score)

play_game()
