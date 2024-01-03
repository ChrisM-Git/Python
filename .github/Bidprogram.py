logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

import os

print(logo +"\n Welcome to the Auction program")

bidend = False

bids = {}


def findhighbid(bidamount):
    highbid = 0
    winner = ""

    for bidder in bidamount:
      amountofbid = bidamount[bidder]
      if amountofbid > highbid:
        highbid = amountofbid
        winner = bidder
    print(f"The highest bidder is {winner}, with the amount of ${highbid}")



while not bidend:
  name = input("Enter your name: \n")
  bid = float(input("Enter your bid: \n $"))
  bids[name] = bid
  other = input("Are there more bidders? \n").lower()

  if other == "yes":
    os.system('clear')
  elif other == "no":
    findhighbid(bids)
    bidend = True








