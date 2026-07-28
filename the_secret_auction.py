# 1. Initialize dictionary OUTSIDE the loop so data isn't overwritten
auction_data = {}

ask_if_there_are_other_users_who_want_to_bid = "Yes"

while ask_if_there_are_other_users_who_want_to_bid.lower() == "yes":
    print("\n" * 100)  # Clear the screen
    print("Welcome to the secret auction program.")
    
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    # 2. Store Name as key, Bid as value
    auction_data[name] = bid
    
    ask_if_there_are_other_users_who_want_to_bid = input("Are there any other users who want to bid? Yes/No: ")

# 3. Find the highest bidder once the loop finishes
highest_bidder = max(auction_data, key=auction_data.get)
highest_bid = auction_data[highest_bidder]

print(f"\nThe winner is {highest_bidder} with a bid of ${highest_bid}!")