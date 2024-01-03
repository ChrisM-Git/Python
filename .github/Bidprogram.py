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

print(logo +"\n Welcome to the Auction program")

bidend = False

bids : {}

"""
def findhighbid(bidamount):
    highbid = 0
    for bidder in bidamount:
    if bidamount > highbid:
      highbid = bidamount
"""

while not bidend:
  name = input("Enter your name: \n")
  bid = float(input("Enter your bid: \n $"))
  bids[name] = bid
  other = input("Are there more bidders? \n").lower()

  if other == "yes":
    clear()
  elif other == "no":
    bidend = True


print(bids)







