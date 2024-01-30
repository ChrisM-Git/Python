logo = """
  ___        _    _                  ___        _            _        _             
 | _ \ _  _ | |_ | |_   ___  _ _    / __| __ _ | | __  _  _ | | __ _ | |_  ___  _ _ 
 |  _/| || ||  _|| ' \ / _ \| ' \  | (__ / _` || |/ _|| || || |/ _` ||  _|/ _ \| '_|
 |_|   \_, | \__||_||_|\___/|_||_|  \___|\__,_||_|\__| \_,_||_|\__,_| \__|\___/|_| 
 
"""
print(logo)


def add(a1,a2):
  return a1 + a2

def subtract(s1,s2):
  return s1 - s2

def multiply(m1,m2):
  return m1 * m2

def divide(d1,d2):
  return d1 / d2


""" add a function wthin a function"""

def calculator(n1,n2,func):
  return func(n1,n2)

result = calculator(2,3,multiply)
print(result)



operations = {

  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
"""
Below is the code for calculator without embedded functions


def calculator():
  should_continue = True
  num1 = int(input("whats the first number: \n"))
  while should_continue:
    print("\n")
    for sym in operations:
      print(sym)
    calc = input("Pick an operation: \n")
    num = int(input("Whats the next number: \n"))
  
    answer = operations[calc](num1,num)
  
    print(f"{num1} + {num} is equal to {answer}")
    cont = input(f"Continue calculating with {answer} or stop? (yes or stop)\n")

    if cont == "stop":
      should_continue = False

    elif cont == "yes":
      num1 = answer


calculator()


"""
    
