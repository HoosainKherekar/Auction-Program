import art
print(art.logo)
print ("Welcome to The Silent Auction program")

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of R{highest_bid}")

bids = {}
continue_bid = True
while continue_bid:
    name = input("What is your name?: ").lower()
    bid = int(input("What's your bid?: R")) 
    bids[name] = bid
    continue_bid = input("Are there any other bidders? Type 'yes' or'no'. ").lower()

    if continue_bid == "no":
        continue_bid = False
        find_highest_bidder(bids)
    elif continue_bid == "yes":
        print("\n" *100)
