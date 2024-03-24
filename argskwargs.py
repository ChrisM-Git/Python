
example of arga the * allows for any number of values
def add(*nums):
  sum = 0
  for n in nums:
    sum += n
  return sum

print(add(4,5,6,8,9,78))

# kwargs are ** and are  keywqord arguements which are dictionaries

def calculate(**kwargs):
  for key, value in kwargs.items():
   # print(key,value) # pritns the key and the value from the dictionary
  # or you can specify the key
  print(kwargs["add"]) #remeber to use list format with dictionary values
calculate(add=5,multiply=10)

# example 2 using a additional values

def calculate2(n, **kwargs):
    n += kwargs["add"]  #this will take 2 add to 5 which is 7
    n *= kwargs["multiply"] # 7 * 10 = 70
    print(n)

calculate2(2, add=5, multiply=10)

# using kwargs in  a class

class car:
  def __init__(self,**kw):
    self.make = kw["make"]
    self.model = kw.get("model")
    self.year = kw.get("year") #get will not return an error if key doesnt exist, just return none
    self.color = kw.get("color")

mycar = car(make="BMW")
print(mycar.color)



