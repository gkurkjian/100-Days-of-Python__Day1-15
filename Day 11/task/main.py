from art import logo
import random

"""Return a random card from the deck"""
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

"""Take the list of cards and return the score calculated from the cards"""
def calculate_score(cards):
    ## here we're checking for Blackjack formed with 2 cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    ## here is A's case if surpasses 21, then we'll return to 1
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


"""Compares the user score u_score against the computer score c_score."""
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    ## Here in this function we'll push the user to get 2 cards in the list
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        ## Here we're dealing straight according to the user's input
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    ## here we're limiting card intake of computer after it reached 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    ## Final print of the results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


## The first prompt for the game starts or not
game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while game_start not in ['y', 'n']:
    print("Wrong input. Please type 'y' or 'n' only.")
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if game_start == 'y':
    play_game()


