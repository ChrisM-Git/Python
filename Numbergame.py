logo = """
___  _                           _                                      _                                   _ 
|_ _|| |_  ___  ._ _  _ _ ._ _ _ | |_  ___  _ _   ___  _ _  ___  ___ ___<_>._ _  ___   ___  ___ ._ _ _  ___ | |
 | | | . |/ ._> | ' || | || ' ' || . \/ ._>| '_> / . || | |/ ._><_-<<_-<| || ' |/ . | / . |<_> || ' ' |/ ._>|_/
 |_| |_|_|\___. |_|_|`___||_|_|_||___/\___.|_|   \_. |`___|\___./__//__/|_||_|_|\_. | \_. |<___||_|_|_|\___.<_>
                                                 <___'                          <___' <___'                    
"""


import random



easylives = 10
hardlives = 5


def answercheck(guess,number,lives):

  if guess > number:
    print(f"You guessed to high, you have {lives} tries left")
    return lives - 1

  if guess < number:
    print(f"You guessed to low,you have {lives} tries left")
    return lives - 1
  else:
    print("Wow, you guessed the right number!")


def difficulty():
  option = input("Choose a difficulty, e for easy or h for hard:\n").lower()
  if option == "e":
    return easylives
  else:
    return hardlives

def numbergame():
  number = random.randint(1, 50)
  print(logo)
  print("Welcome to the number guessing game!")
  print("I am thinking of a number between 1 and 50")
  lives = difficulty()
  print(f"You get {lives} tries!")
  guess = 55
  while guess != number:
    guess = int(input("Guess a number between 1 and 50: \n"))
    lives = answercheck(guess,number,lives)
    if lives == 0:
      print(f"you didnt guess the number, it was {number}")
      guess = number


while input("Do you want to play guess the number game? (y or n)") == "y":
  numbergame()










