# example of list comprehension

# numbers = [1,2,3]
# newlist = []
# for n in numbers:
#     num = n + 1
#     newlist.append(num)
#
#
# # With list comprehension
# newlistcomp = [n + 1 for n in numbers]
# print(newlistcomp)


# example with names
#
# name = "Chris"
# newnamelist = [letter for letter in name]
# print(newnamelist)
#
# newrangelist = [n * 2 for n in range(1,5)]
# print(newrangelist)

# comprehension format

# newlist = [ new_item for item in list  if test]

# dictionary comprehension
# new_dict  = {new_key: new _value for item in list}
# comprehension on an existing dictionary
# new_dict = {new_key:new_value for {key,value} in dict.items}

# exmple
# import random
# names = ["Ben","Bard","Chassy","Henrick","Merlin","Wong","Zabry"]
# name_scores = {name:random.randint(50,99) for name in names}
# comprehension new dictionary with a existing dictonary
# passed_names = {name:score for (name,score) in name_scores.items() if score >= 75}
# print(passed_names)

"""You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in
the given sentence and calculates the number of letters in each word.Try Googling to find out how to convert a sentence
into a list of words."""
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# newsentence = sentence.split() #puts input into a list
# newdict = {word:len(word) for word in newsentence}
# print(newdict)

# next challenge
"""You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature 
in degrees Celsius and converts it into degrees Fahrenheit.To convert temp_c into temp_f use this formula:
(temp_c * 9/5) + 32 = temp_f"""
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:(temp * 9/5) + 32 for (day,temp) in weather_c.items()}
# print(weather_f)

# loop with Panda dataframes
# dictionary
student = {
    "student": ["Tom", "Dick", "Harry"],
    "score": [67, 75, 77]
}
# for (key,value) in student.items(): #loop through the dictonary
#     print(key,value) #print the key and value, you can also just print the key or the value
# use pandas
import pandas
student_df = pandas.DataFrame(student)  # create a dataframe from student dictionary
print(student_df)
for (index,row) in student_df.iterrows(): #pandas has inbuilt loop called interrows
    print(row.student,row.score)

    if row.student == "Dick":
        print(row.score)



