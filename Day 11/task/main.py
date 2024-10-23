from art import logo
import random

def deal_card():
    """Returns a random card from a deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

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

if_game_over = False

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

