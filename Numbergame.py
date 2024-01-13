logo = """
___  _                           _                                      _                                   _ 
|_ _|| |_  ___  ._ _  _ _ ._ _ _ | |_  ___  _ _   ___  _ _  ___  ___ ___<_>._ _  ___   ___  ___ ._ _ _  ___ | |
 | | | . |/ ._> | ' || | || ' ' || . \/ ._>| '_> / . || | |/ ._><_-<<_-<| || ' |/ . | / . |<_> || ' ' |/ ._>|_/
 |_| |_|_|\___. |_|_|`___||_|_|_||___/\___.|_|   \_. |`___|\___./__//__/|_||_|_|\_. | \_. |<___||_|_|_|\___.<_>
                                                 <___'                          <___' <___'                    
"""


import random
print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 50")
number = random.randint(1, 50)

difficulty = input("Choose a difficulty, e for easy or h for hard:\n").lower()
endgame = False
lives = 0
if difficulty == "e":
  lives = 10
  print("you get 10 tries")
else:
  lives = 5
  print("you get 5 tries")


while not endgame:
  guess = int(input("Guess a number between 1 and 50: \n"))
  if guess > number:
    lives -= 1
    print(f"You guessed to high, you have {lives} tries left")
  if guess < number:
    lives -= 1
    print(f"You guessed to low,you have {lives} tries left")
  if guess == number:
    endgame = True
    print("Wow, you guessed the right number!")









