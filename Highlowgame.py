logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import os
import random
from highlowgamedata import data



def compare(choicea,choiceb,choice):
  if choicea > choiceb and choice == "a":
    return True
  elif choicea < choiceb and choice == "a":
    return False
  if choiceb > choicea and choice == "b":
    return True
  elif choiceb < choicea and choice == "b":
    return False

score = 0

endgame = False
os.system('clear')
while not endgame:

  randomA = random.choice(list(data))
  randomB = random.choice(list(data))
  choicea = randomA['follower_count']
  choiceb = randomB['follower_count']
  print(f"{randomA["name"]} a {randomA['description']} from {randomA['country']}")
  print(vs)
  print(f"{randomB["name"]} a {randomB['description']} from {randomB['country']}")

  choice = input("Who has more followers, A or B?").lower()
  result = compare(choicea,choiceb,choice)
  if result == True:
    score += 1
    print(f"Thats right! your score is {score}")
    os.system('clear')
  elif result == False:
    print(f"No, thats not right, game over!, your total score ia {score}")
    endgame = True




