# BLIND AUCTION$
'''
Each person inputs their bid
Using a dictionary, add a name (key) and their bid (value) for each person (3 people), and clear() the prompt after each one. 

When the last person is finished, loop through the dictionary and reveal the winner with the highest bid. 

ISSUES: I didn't want to refactor into a list after going from nested dictionaries, but realized that bidders.update overwrites current dictionary, so I'll have to eventually modify it to keep the full list, rather than just the highest bidder (even though that solves the problem)
'''
import clear

bidders = {}


def add_bidders(first_name, bid_amount):
    new_bidder = {
        'bidder': {
            'first_name': first_name,
            'bid': bid_amount
        }
    }
    bidders.update(new_bidder)

# loop through nested list to pull values (this works with static dictionary values)


def highest_bidder():
    winning_bidder = ""
    winning_bid = 0
    for k in bidders:  # identify the keys
        val = bidders[k].get('bid')  # get bid value
        wb = bidders[k].get('first_name')  # get first name
        if val > winning_bid:  # compare bid value
            winning_bid += val  # add higher value to var
            winning_bidder = wb  # add winner to var
    print(f"{winning_bidder} wins with a bid of {winning_bid}!")


def start_bidding():
    first_name = input("Please enter your first name: ")
    bid_amount = int(input("Please enter your bid: $"))
    next_bidder = int(
        input("Is there another bidder? Enter 0 for Yes, and 1 for No: "))
    if next_bidder == 0:
        add_bidders(first_name, bid_amount)
        start_bidding()
    else:
        highest_bidder()
        print(bidders)


start_bidding()
