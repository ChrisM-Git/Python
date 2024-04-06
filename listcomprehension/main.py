# berfore list comprehension

numbers = [1,2,3]
newnumbers = []
for n in numbers:
  num = n + 1
  newnumbers.append(num)


#With list comprehension
numbers = [1,2,3]
newnum = [n + 1 for n in numbers]
print(newnum)
# examples with names
name = "Chris"
newnamelist=[letter for letter in name]
print(newnamelist) # puts name in a list

#use of range in list comprehension
doublenum = [n * 2 for n in range(1,5)]
print(doublenum)

#conditional list comprehension
names = ["chris","Alex","elanor","Caroline","Dave","Freddie","Beth"]
shortnames = [ name for name in names if len(name) < 5] #remember lists start at 0 so we need len to be 5 for 4 or less lettters
print(shortnames)

#change names to upper case
names = ["chris","Alex","elanor","Caroline","Dave","Freddie","Beth"]
nameupper = [name.upper() for name in names if len(name) > 5] #uppercase names above 5 char
print(nameupper)
