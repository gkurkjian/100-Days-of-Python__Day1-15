from art import logo
import random

game_on = True


while game_on:
    user_input = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    if user_input == 'y':
        print(logo)

        ## User's first hand will be given Two cards
        user_cards = [random.choice(cards) for _ in range(2)]
        user_num = sum(user_cards)

        ## Computer first hand will be give One card
        computer_card = [random.choice(cards)]

        print(f"Your cards: [{user_cards[0]},{user_cards[1]}], current score: {user_num}")
        print(f"Computer's first card: {computer_card}")


