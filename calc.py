import art
print(art.logo)


def add(a1,a2):
  return a1 + a2

def subtract(s1,s2):
  return s1 - s2

def multiply(m1,m2):
  return m1 * m2

def divide(d1,d2):
  return d1 / d2


operations = {

  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

should_continue = True

def calculator():
  
  num1 = int(input("whats the first number: \n"))
  while should_continue:
    print("\n")
    for sym in operations:
      print(sym)
    calc = input("Pick an operation: \n")
    num = int(input("Whats the next number: \n"))
  
    answer = operations[calc](num1,num)
  
    print(f"{num1} + {num} is equal to {answer}")
    cont = input(f"Continue calculating with {answer} or stop? \n")
  
    if cont == "stop":
      should_continue = False
      calculator()
    elif cont == "yes":
      num1 = answer


    
