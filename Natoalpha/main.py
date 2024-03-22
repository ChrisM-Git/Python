# Below is example of dictionary comprehension and pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
#for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# pandas uses this format for comprehension
# {newkey: newvalue} for (index,row) in df.iterrows()

# TODO 1. Create a dictionary in this format: using the CSV file nato_phomnsic alphabet
{"A": "Alfa", "B": "Bravo"}
import pandas
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
natodf = pandas.DataFrame(nato)
natodict = {row.letter:row.code for (index,row) in natodf.iterrows()}
print(natodict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
Userinput = input("Enter your name:").upper()
# [new item for item in list]
natoname = [natodict[ltr] for ltr in Userinput]
print(natoname)
