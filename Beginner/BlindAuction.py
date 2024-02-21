import AuctionArt

import os

print(AuctionArt.logo)

Another_Bidder = True

print("Welcome to the secrete auction program.")

Bidder_dictionary = {
  
}

def New_Bidder(name, amount):
  Bidder_dictionary[name] = amount

  
def Find_Largest_Bid():
  highest_bid = 0
  winner = ""
  for bid in Bidder_dictionary:
    if Bidder_dictionary[bid] > highest_bid:
      highest_bid = Bidder_dictionary[bid]
      winner = bid
  print(f'{winner} had the highest bid of {highest_bid}!')

while Another_Bidder:
  Bidder_name = input("What is your name? ")
  Bidder_amount = float(input("What is your bid amount? "))

  New_Bidder(Bidder_name, Bidder_amount)

  user_answer = input("Are there any other bidders? Type 'yes or 'no'. " ).lower()
  if user_answer == "no":
    Another_Bidder = False
  os.system('cls')

Find_Largest_Bid()