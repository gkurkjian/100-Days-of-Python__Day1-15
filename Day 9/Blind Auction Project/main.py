from art import logo

print(logo)

def clear_screen():
    print("\n" * 20)  ## This will print spaces between the line

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bids_records):
    highest_bid = 0  ## set to empty int()
    name_of_winner = ""  ## set to empty string

    for bidder in bids_records:
        bid_amount = bids_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            name_of_winner = bidder
    print(f"The winner is {name_of_winner} with a bid of ${highest_bid}")

    ### This is using max() function to find-out the highest
    # name_of_winner = max(bids_records, key=bids_records.get)
    # highest_bid = bids_records[name_of_winner]
    # print(f"The winner is {name_of_winner} with a bid of ${highest_bid}")


bid_over = True

# TODO-2: Save data into dictionary {name: price}
bids = {}


# TODO-3: Whether if new bids need to be added
while bid_over:
    # TODO-1: Ask the user for input
    user_name = input("What is your name?:  ")
    user_bid_price = int(input("What is your bid?:  "))

    bids[user_name] = user_bid_price

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if more_bidders == 'yes':
        clear_screen()

    elif more_bidders == 'no':
        find_highest_bidder(bids)
        bid_over = False