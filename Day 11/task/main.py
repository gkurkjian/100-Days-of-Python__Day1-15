from art import logo
import random

def deal_card():
    """Returns a random card from a deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

## This function will calculate the score everytime
##We can use it both for User & Computer's cards
def calculate_score(cards):
    ## Or short way you can right
    ##if sum(cards) == 21 and len(cards) == 2:
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0

    ## Step 8 to handle BlackJack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# def compare(the_user_score, the_computer_score):
#     """Compares the user score the_user_score against the computer score the_computer_score."""
#     if the_user_score == the_computer_score:
#         return "Draw 🙃"
#     elif the_computer_score == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif the_user_score == 0:
#         return "Win with a Blackjack 😎"
#     elif the_user_score > 21:
#         return "You went over. You lose 😭"
#     elif the_computer_score > 21:
#         return "Opponent went over. You win 😁"
#     elif the_user_score > the_computer_score:
#         return "You win 😃"
#     else:
#         return "You lose 😤"

def compare(the_user_score, the_computer_score):
    """Compares the user score the_user_score against the computer score the_computer_score."""
    # If scores are equal, it's a draw
    if the_user_score == the_computer_score:
        return "Draw 🙃", 0

    # If the computer has a Blackjack (score is 0), the user loses
    elif the_computer_score == 0:
        return "Lose, opponent has Blackjack 😱", -1

    # If the user has a Blackjack (score is 0), the user wins
    elif the_user_score == 0:
        return "Win with a Blackjack 😎", 1

    # If the user goes over 21, they lose
    elif the_user_score > 21:
        return "You went over. You lose 😭", -1

    # If the computer goes over 21, the user wins
    elif the_computer_score > 21:
        return "Opponent went over. You win 😁", 1

    # If the user's score is greater than the computer's, the user wins
    elif the_user_score > the_computer_score:
        return "You win 😃", 1

    # In all other cases, the user loses
    else:
        return "You lose 😤", -1

def play_game():
    print(logo)
    if_game_over = False
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not if_game_over:
        user_score = calculate_score(user_cards)  ## find the sum of user's cards
        computer_score = calculate_score(computer_cards)  ## find the sum of computer's cards
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            if_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                if_game_over = True

    ## Handle Computer's hand after second attempt
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())  ## will get another card
        computer_score = calculate_score(computer_cards)  ## will calculate after adding new card

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
    print("\n" * 20)
    play_game()
