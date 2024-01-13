
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

"""

import random


def dealcards():
    #return a random card value from cards list, the 10 represnt 10,J,Q,K, and 11 is Ace
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = random.choice(cards)
    return card

def calculatecards(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(playertotal, dealertotal):
  if playertotal == dealertotal:
    print("Push")
  elif dealertotal == 0:
    print("Dealer Wins!")
  elif playertotal == 0:
    print ("You won")
  elif playertotal > 21:
    print("You busted")
  elif dealertotal > 21:
    print("Dealer Busts!, you win!")
  elif playertotal == 21:
    print("You got 21, you win!")
  elif playertotal > dealertotal:
    print("You won")
  else:
    return "Dealer wins"


def playgame():
    print(logo)
    print("Dealing the cards \n")
    playercards = []
    dealercards = []

    for _ in range(2):
      playercards.append(dealcards())
      dealercards.append(dealcards())
    endgame = False
    while not endgame:
      #calculate the total sum of player and dealer cards
      playertotal = calculatecards(playercards)
      dealertotal = calculatecards(dealercards)

      print(f"You have {playercards} with a total of {playertotal}")
      print(f"The Dealer is showing a {dealercards[0]}")


      if playertotal == "BlackJack!" or dealertotal == "BlackJack!" or playertotal > 21:
        endgame = True
      else:
        option = input("Do you want to hit or stay? (type h or hit or s for stay\n")

        if option == "h":
          playercards.append(dealcards())
        else:
          endgame = True

        # while loop for the computer to now play!

    while dealertotal != "BlackJack!" and dealertotal < 17:
        dealercards.append(dealcards())
        dealertotal = calculatecards(dealercards)


    print(f"The Dealer has {dealercards} for a total of {dealertotal}")

    print(compare(playertotal,dealertotal))

while input("Do you want to play Blackjack?, y or n?").lower() == "y":
  playgame()












