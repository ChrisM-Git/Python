# age: int
# name: string
# height: float
# is_human = bool

# specify the data type in a function to describe errors later in code
# USe the arrow with bool to expect an output of True or False, which th the return atatement below does
def policechcck(age: int) -> bool:
  if age > 18:
    can_drive = True
  else:
    can_drive = False
  return can_drive

if policechcck(19):
  print("You cvan drive")
else:
  print("Not old enough")


