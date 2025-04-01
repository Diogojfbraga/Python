print("Welcome to the secret auction program.")

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""

    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")

bids = {}
while True:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if should_continue == 'no':
        find_highest_bidder(bids)
        break
    elif should_continue == 'yes':
        print("\n" * 50)  # Clears the screen (simulated)
